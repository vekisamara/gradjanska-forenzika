#!/usr/bin/env python3
"""GFO Election Analytics — Peer Group Engine v0.1.

Builds deterministic, non-political nearest-neighbor peer groups within municipality.
No anomaly scoring and no LLM use.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "0.1.0"
REQUIRED_FEATURES = ("registered_voters_mean", "turnout_mean", "invalid_rate_mean")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        if fieldnames:
            with path.open("w", newline="", encoding="utf-8") as fh:
                csv.DictWriter(fh, fieldnames=fieldnames).writeheader()
        else:
            path.write_text("", encoding="utf-8")
        return
    fields = fieldnames or []
    if not fields:
        for row in rows:
            for key in row:
                if key not in fields:
                    fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def num(v: Any) -> float | None:
    if v in (None, ""):
        return None
    try:
        x = float(v)
        if math.isfinite(x):
            return x
    except (TypeError, ValueError):
        pass
    return None


def mean_or_none(values: list[float]) -> float | None:
    return statistics.fmean(values) if values else None


def std_or_none(values: list[float]) -> float | None:
    return statistics.stdev(values) if len(values) >= 2 else None


def round_or_none(v: float | None, digits: int = 6) -> float | None:
    return None if v is None else round(v, digits)


def robust_scale(values: list[float]) -> tuple[float, float]:
    center = statistics.median(values)
    abs_dev = [abs(v - center) for v in values]
    mad = statistics.median(abs_dev)
    scale = 1.4826 * mad
    if scale <= 0:
        scale = statistics.pstdev(values) if len(values) >= 2 else 0.0
    if scale <= 0:
        scale = 1.0
    return center, scale


def feature_vector(row: dict[str, str]) -> dict[str, float] | None:
    reg = num(row.get("registered_voters_mean"))
    turnout = num(row.get("turnout_mean"))
    invalid = num(row.get("invalid_rate_mean"))
    if reg is None or turnout is None or invalid is None or reg < 0:
        return None
    return {
        "log_registered": math.log1p(reg),
        "turnout_mean": turnout,
        "invalid_rate_mean": invalid,
    }


def distance(a: dict[str, float], b: dict[str, float], scales: dict[str, tuple[float, float]]) -> float:
    parts = []
    for key in ("log_registered", "turnout_mean", "invalid_rate_mean"):
        _, scale = scales[key]
        parts.append(((a[key] - b[key]) / scale) ** 2)
    return math.sqrt(sum(parts))


def build_metadata(rows: list[dict[str, str]], canonical_election_id: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for r in rows:
        if r.get("election_id") != canonical_election_id:
            continue
        code = (r.get("polling_station_code") or "").strip()
        if not code:
            continue
        if code not in out:
            out[code] = {
                "municipality_code": (r.get("municipality_code") or "").strip(),
                "polling_station_name": (r.get("polling_station_name") or "").strip(),
            }
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Build deterministic municipal peer groups for polling stations.")
    p.add_argument("baseline_csv")
    p.add_argument("historical_csv")
    p.add_argument("--canonical-election-id", required=True)
    p.add_argument("--output", default="./peer-group-output")
    p.add_argument("--min-peers", type=int, default=5)
    p.add_argument("--max-peers", type=int, default=15)
    a = p.parse_args()

    if a.min_peers < 1:
        raise SystemExit("--min-peers must be >= 1")
    if a.max_peers < a.min_peers:
        raise SystemExit("--max-peers must be >= --min-peers")

    baseline_path = Path(a.baseline_csv)
    historical_path = Path(a.historical_csv)
    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)

    baseline_rows = read_csv(baseline_path)
    historical_rows = read_csv(historical_path)
    metadata = build_metadata(historical_rows, a.canonical_election_id)

    flags: list[dict[str, Any]] = []
    unique: dict[str, dict[str, str]] = {}
    duplicates: set[str] = set()
    for r in baseline_rows:
        code = (r.get("canonical_polling_station_code") or "").strip()
        if not code:
            continue
        if code in unique:
            duplicates.add(code)
        else:
            unique[code] = r
    for code in sorted(duplicates):
        flags.append({"record_id": code, "rule_code": "GFO-PG-V001", "severity": "error", "message": "Duplicate canonical polling-station code in baseline input"})

    records: dict[str, dict[str, Any]] = {}
    by_municipality: dict[str, list[str]] = defaultdict(list)
    for code, row in sorted(unique.items()):
        meta = metadata.get(code)
        if not meta or not meta.get("municipality_code"):
            flags.append({"record_id": code, "rule_code": "GFO-PG-V002", "severity": "warning", "message": "Missing canonical municipality metadata"})
            continue
        vec = feature_vector(row)
        if vec is None:
            flags.append({"record_id": code, "rule_code": "GFO-PG-V003", "severity": "warning", "message": "Missing or invalid required peer-group similarity feature"})
            continue
        rec = {
            "code": code,
            "municipality_code": meta["municipality_code"],
            "polling_station_name": meta.get("polling_station_name", ""),
            "baseline": row,
            "vector": vec,
        }
        records[code] = rec
        by_municipality[meta["municipality_code"]].append(code)

    municipality_scales: dict[str, dict[str, tuple[float, float]]] = {}
    for municipality, codes in by_municipality.items():
        vecs = [records[c]["vector"] for c in codes]
        municipality_scales[municipality] = {
            key: robust_scale([v[key] for v in vecs])
            for key in ("log_registered", "turnout_mean", "invalid_rate_mean")
        }

    membership_rows: list[dict[str, Any]] = []
    group_rows: list[dict[str, Any]] = []
    feature_rows: list[dict[str, Any]] = []

    for code in sorted(unique):
        group_id = f"PG-{code}"
        rec = records.get(code)
        if rec is None:
            group_rows.append({
                "peer_group_id": group_id,
                "target_polling_station_code": code,
                "municipality_code": metadata.get(code, {}).get("municipality_code", ""),
                "status": "insufficient_peer_group",
                "available_peer_candidates": 0,
                "selected_peer_count": 0,
                "min_peer_distance": "",
                "mean_peer_distance": "",
                "max_peer_distance": "",
            })
            continue

        municipality = rec["municipality_code"]
        candidate_codes = [c for c in by_municipality[municipality] if c != code]
        if len(candidate_codes) < a.min_peers:
            flags.append({"record_id": code, "rule_code": "GFO-PG-V007", "severity": "warning", "message": f"Only {len(candidate_codes)} valid same-municipality peer candidates; minimum is {a.min_peers}"})
            group_rows.append({
                "peer_group_id": group_id,
                "target_polling_station_code": code,
                "municipality_code": municipality,
                "status": "insufficient_peer_group",
                "available_peer_candidates": len(candidate_codes),
                "selected_peer_count": 0,
                "min_peer_distance": "",
                "mean_peer_distance": "",
                "max_peer_distance": "",
            })
            continue

        scales = municipality_scales[municipality]
        ranked = sorted(
            ((distance(rec["vector"], records[c]["vector"], scales), c) for c in candidate_codes),
            key=lambda x: (x[0], x[1]),
        )
        selected = ranked[:a.max_peers]
        distances = [d for d, _ in selected]

        if len(selected) > a.max_peers:
            flags.append({"record_id": code, "rule_code": "GFO-PG-V008", "severity": "error", "message": "Selected peer count exceeds max_peers"})

        seen: set[str] = set()
        for rank, (d, peer_code) in enumerate(selected, start=1):
            if peer_code == code:
                flags.append({"record_id": code, "rule_code": "GFO-PG-V004", "severity": "error", "message": "Self-membership detected"})
            if records[peer_code]["municipality_code"] != municipality:
                flags.append({"record_id": f"{code}|{peer_code}", "rule_code": "GFO-PG-V005", "severity": "error", "message": "Peer from different municipality"})
            if peer_code in seen:
                flags.append({"record_id": f"{code}|{peer_code}", "rule_code": "GFO-PG-V006", "severity": "error", "message": "Duplicate peer member in target group"})
            seen.add(peer_code)
            membership_rows.append({
                "peer_group_id": group_id,
                "target_polling_station_code": code,
                "peer_polling_station_code": peer_code,
                "municipality_code": municipality,
                "peer_rank": rank,
                "distance": round(d, 6),
                "membership_confidence": round(1.0 / (1.0 + d), 6),
            })

        group_rows.append({
            "peer_group_id": group_id,
            "target_polling_station_code": code,
            "municipality_code": municipality,
            "status": "ok",
            "available_peer_candidates": len(candidate_codes),
            "selected_peer_count": len(selected),
            "min_peer_distance": round_or_none(min(distances) if distances else None),
            "mean_peer_distance": round_or_none(mean_or_none(distances)),
            "max_peer_distance": round_or_none(max(distances) if distances else None),
        })

        peer_baselines = [records[c]["baseline"] for _, c in selected]
        regs = [x for r in peer_baselines if (x := num(r.get("registered_voters_mean"))) is not None]
        turnouts = [x for r in peer_baselines if (x := num(r.get("turnout_mean"))) is not None]
        invalids = [x for r in peer_baselines if (x := num(r.get("invalid_rate_mean"))) is not None]
        valid_rates = [x for r in peer_baselines if (x := num(r.get("valid_vote_rate_mean"))) is not None]
        feature_rows.append({
            "peer_group_id": group_id,
            "target_polling_station_code": code,
            "municipality_code": municipality,
            "peer_count": len(selected),
            "registered_voters_mean": round_or_none(mean_or_none(regs)),
            "registered_voters_std": round_or_none(std_or_none(regs)),
            "turnout_mean": round_or_none(mean_or_none(turnouts)),
            "turnout_std": round_or_none(std_or_none(turnouts)),
            "turnout_min": round_or_none(min(turnouts) if turnouts else None),
            "turnout_max": round_or_none(max(turnouts) if turnouts else None),
            "invalid_rate_mean": round_or_none(mean_or_none(invalids)),
            "invalid_rate_std": round_or_none(std_or_none(invalids)),
            "invalid_rate_min": round_or_none(min(invalids) if invalids else None),
            "invalid_rate_max": round_or_none(max(invalids) if invalids else None),
            "valid_vote_rate_mean": round_or_none(mean_or_none(valid_rates)),
            "valid_vote_rate_std": round_or_none(std_or_none(valid_rates)),
        })

    write_csv(out / "peer_group_membership.csv", membership_rows)
    write_csv(out / "peer_groups.csv", group_rows)
    write_csv(out / "peer_group_features.csv", feature_rows)
    write_csv(out / "peer_group_validation_flags.csv", flags)

    ok_groups = sum(r["status"] == "ok" for r in group_rows)
    insufficient = sum(r["status"] == "insufficient_peer_group" for r in group_rows)
    manifest = {
        "module": "peer_group_engine_v0_1.py",
        "module_version": VERSION,
        "processed_at": datetime.now(timezone.utc).isoformat(),
        "baseline_input": str(baseline_path.resolve()),
        "baseline_input_sha256": sha256_file(baseline_path),
        "historical_input": str(historical_path.resolve()),
        "historical_input_sha256": sha256_file(historical_path),
        "canonical_election_id": a.canonical_election_id,
        "min_peers": a.min_peers,
        "max_peers": a.max_peers,
        "input_baseline_station_count": len(unique),
        "eligible_feature_station_count": len(records),
        "peer_group_count": len(group_rows),
        "ok_peer_group_count": ok_groups,
        "insufficient_peer_group_count": insufficient,
        "membership_row_count": len(membership_rows),
        "peer_group_feature_row_count": len(feature_rows),
        "validation_flag_count": len(flags),
    }
    (out / "peer_group_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Peer groups: {len(group_rows)}")
    print(f"OK peer groups: {ok_groups}")
    print(f"Insufficient peer groups: {insufficient}")
    print(f"Membership rows: {len(membership_rows)}")
    print(f"Validation flags: {len(flags)}")
    print(f"Output: {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
