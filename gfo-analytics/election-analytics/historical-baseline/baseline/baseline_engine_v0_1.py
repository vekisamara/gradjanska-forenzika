#!/usr/bin/env python3
"""GFO Election Analytics — Historical Baseline Engine v0.1.

Consumes canonical historical election rows plus an explicit polling-station mapping.
Produces deterministic baseline features. No anomaly scoring and no LLM use.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "0.1.0"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    for row in rows:
        for k in row:
            if k not in fields:
                fields.append(k)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def truthy(v: Any) -> bool:
    return str(v).strip().lower() in {"1", "true", "yes", "y"}


def num(v: Any) -> float | None:
    if v in (None, ""):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def stat(values: list[float], fn: str) -> float | None:
    if not values:
        return None
    if fn == "mean": return statistics.fmean(values)
    if fn == "median": return statistics.median(values)
    if fn == "std": return statistics.stdev(values) if len(values) >= 2 else None
    if fn == "min": return min(values)
    if fn == "max": return max(values)
    raise ValueError(fn)


def round_or_none(v: float | None, digits: int = 6) -> float | None:
    return None if v is None else round(v, digits)


def main() -> int:
    p = argparse.ArgumentParser(description="Build polling-station historical baseline features.")
    p.add_argument("historical_csv")
    p.add_argument("mapping_csv")
    p.add_argument("--output", default="./baseline-output")
    p.add_argument("--min-mapping-confidence", type=float, default=0.95)
    p.add_argument("--min-election-count", type=int, default=2)
    a = p.parse_args()

    hist_path = Path(a.historical_csv)
    map_path = Path(a.mapping_csv)
    out = Path(a.output)
    out.mkdir(parents=True, exist_ok=True)

    rows = read_csv(hist_path)
    mappings = read_csv(map_path)
    mapping_index: dict[tuple[str, str], str] = {}
    mapping_meta: dict[tuple[str, str], dict[str, str]] = {}
    flags: list[dict[str, Any]] = []

    for m in mappings:
        key = (m.get("historical_election_id", ""), m.get("historical_polling_station_code", ""))
        conf = num(m.get("mapping_confidence")) or 0.0
        usable = truthy(m.get("usable_for_baseline")) and conf >= a.min_mapping_confidence
        if usable and m.get("canonical_polling_station_code"):
            if key in mapping_index and mapping_index[key] != m.get("canonical_polling_station_code"):
                flags.append({"record_id": "|".join(key), "rule_code": "GFO-B-M001", "severity": "error", "message": "Conflicting usable mappings"})
            else:
                mapping_index[key] = m["canonical_polling_station_code"]
                mapping_meta[key] = m

    # Deduplicate station totals per election/BM and validate consistency across candidate rows.
    station_groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for r in rows:
        station_groups[(r.get("election_id", ""), r.get("polling_station_code", ""))].append(r)

    station_obs: dict[tuple[str, str], dict[str, Any]] = {}
    bloc_votes: dict[tuple[str, str, str], float] = defaultdict(float)

    for key, group in station_groups.items():
        election_id, ps_code = key
        mapped = mapping_index.get(key)
        if not mapped:
            continue

        first = group[0]
        numeric_fields = ["registered_voters", "total_votes", "valid_votes", "invalid_votes"]
        values_by_field: dict[str, set[float]] = {}
        for field in numeric_fields:
            vals = {v for r in group if (v := num(r.get(field))) is not None}
            values_by_field[field] = vals
            if len(vals) > 1:
                flags.append({"record_id": f"{election_id}|{ps_code}", "rule_code": "GFO-B-V001", "severity": "error", "message": f"Inconsistent {field} across candidate rows: {sorted(vals)}"})

        reg = next(iter(values_by_field["registered_voters"]), None)
        total = next(iter(values_by_field["total_votes"]), None)
        valid = next(iter(values_by_field["valid_votes"]), None)
        invalid = next(iter(values_by_field["invalid_votes"]), None)

        if reg is not None and total is not None and total > reg:
            flags.append({"record_id": f"{election_id}|{ps_code}", "rule_code": "GFO-B-V002", "severity": "error", "message": "total_votes exceeds registered_voters"})
        if valid is not None and invalid is not None and total is not None and valid + invalid != total:
            flags.append({"record_id": f"{election_id}|{ps_code}", "rule_code": "GFO-B-V003", "severity": "error", "message": "valid_votes + invalid_votes != total_votes"})

        turnout = (total / reg) if reg not in (None, 0) and total is not None else None
        invalid_rate = (invalid / total) if total not in (None, 0) and invalid is not None else None
        valid_rate = (valid / total) if total not in (None, 0) and valid is not None else None

        station_obs[(mapped, election_id)] = {
            "canonical_polling_station_code": mapped,
            "election_id": election_id,
            "election_date": first.get("election_date", ""),
            "election_type": first.get("election_type", ""),
            "turnout_eligible": truthy(first.get("turnout_eligible")),
            "structural_eligible": truthy(first.get("structural_eligible")),
            "political_share_eligible": truthy(first.get("political_share_eligible")),
            "registered_voters": reg,
            "total_votes": total,
            "valid_votes": valid,
            "invalid_votes": invalid,
            "turnout": turnout,
            "invalid_rate": invalid_rate,
            "valid_rate": valid_rate,
        }

        if truthy(first.get("political_share_eligible")) and valid not in (None, 0):
            candidate_vote_sum = 0.0
            candidate_numeric = True
            for r in group:
                v = num(r.get("votes"))
                if v is None:
                    candidate_numeric = False
                    continue
                candidate_vote_sum += v
                bloc = (r.get("political_bloc_id") or "").strip()
                if bloc:
                    bloc_votes[(mapped, election_id, bloc)] += v
            if candidate_numeric and valid is not None and candidate_vote_sum != valid:
                flags.append({"record_id": f"{election_id}|{ps_code}", "rule_code": "GFO-B-V004", "severity": "warning", "message": f"candidate vote sum {candidate_vote_sum} != valid_votes {valid}"})

    by_station: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for (mapped, _), obs in station_obs.items():
        by_station[mapped].append(obs)

    baseline_rows: list[dict[str, Any]] = []
    for code, obs in sorted(by_station.items()):
        turnout_obs = [o for o in obs if o["turnout_eligible"] and o["turnout"] is not None]
        structural_obs = [o for o in obs if o["structural_eligible"]]
        turnouts = [float(o["turnout"]) for o in turnout_obs]
        regs = [float(o["registered_voters"]) for o in structural_obs if o["registered_voters"] is not None]
        invalid_rates = [float(o["invalid_rate"]) for o in structural_obs if o["invalid_rate"] is not None]
        valid_rates = [float(o["valid_rate"]) for o in structural_obs if o["valid_rate"] is not None]
        n = len(turnout_obs)
        if n < a.min_election_count:
            flags.append({"record_id": code, "rule_code": "GFO-B-V005", "severity": "warning", "message": f"Only {n} turnout-eligible historical elections; minimum is {a.min_election_count}"})
        baseline_rows.append({
            "canonical_polling_station_code": code,
            "historical_election_count": n,
            "structural_election_count": len(structural_obs),
            "registered_voters_mean": round_or_none(stat(regs, "mean")),
            "registered_voters_std": round_or_none(stat(regs, "std")),
            "turnout_mean": round_or_none(stat(turnouts, "mean")),
            "turnout_median": round_or_none(stat(turnouts, "median")),
            "turnout_std": round_or_none(stat(turnouts, "std")),
            "turnout_min": round_or_none(stat(turnouts, "min")),
            "turnout_max": round_or_none(stat(turnouts, "max")),
            "historical_turnout_range": round_or_none((max(turnouts) - min(turnouts)) if turnouts else None),
            "invalid_rate_mean": round_or_none(stat(invalid_rates, "mean")),
            "invalid_rate_std": round_or_none(stat(invalid_rates, "std")),
            "valid_vote_rate_mean": round_or_none(stat(valid_rates, "mean")),
        })

    bloc_group: dict[tuple[str, str], list[tuple[str, float]]] = defaultdict(list)
    for (code, election_id, bloc), votes in bloc_votes.items():
        valid = station_obs[(code, election_id)].get("valid_votes")
        if valid not in (None, 0):
            bloc_group[(code, bloc)].append((election_id, votes / float(valid)))

    bloc_rows: list[dict[str, Any]] = []
    for (code, bloc), vals in sorted(bloc_group.items()):
        shares = [v for _, v in vals]
        latest = sorted(vals, key=lambda x: x[0])[-1]
        bloc_rows.append({
            "canonical_polling_station_code": code,
            "political_bloc_id": bloc,
            "comparable_election_count": len(vals),
            "share_mean": round_or_none(stat(shares, "mean")),
            "share_median": round_or_none(stat(shares, "median")),
            "share_std": round_or_none(stat(shares, "std")),
            "share_min": round_or_none(stat(shares, "min")),
            "share_max": round_or_none(stat(shares, "max")),
            "last_historical_election_id": latest[0],
            "last_historical_share": round_or_none(latest[1]),
        })

    write_csv(out / "baseline_polling_stations.csv", baseline_rows)
    write_csv(out / "baseline_bloc_shares.csv", bloc_rows)
    write_csv(out / "validation_flags.csv", flags)

    manifest = {
        "module": "baseline_engine_v0_1.py",
        "module_version": VERSION,
        "processed_at": datetime.now(timezone.utc).isoformat(),
        "historical_input": str(hist_path.resolve()),
        "historical_input_sha256": sha256_file(hist_path),
        "mapping_input": str(map_path.resolve()),
        "mapping_input_sha256": sha256_file(map_path),
        "min_mapping_confidence": a.min_mapping_confidence,
        "min_election_count": a.min_election_count,
        "mapped_station_election_observations": len(station_obs),
        "baseline_polling_station_count": len(baseline_rows),
        "bloc_baseline_row_count": len(bloc_rows),
        "validation_flag_count": len(flags),
    }
    (out / "baseline_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Baseline polling stations: {len(baseline_rows)}")
    print(f"Bloc baseline rows: {len(bloc_rows)}")
    print(f"Validation flags: {len(flags)}")
    print(f"Output: {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
