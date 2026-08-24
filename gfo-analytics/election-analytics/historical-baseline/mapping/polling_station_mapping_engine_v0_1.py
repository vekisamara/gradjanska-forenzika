#!/usr/bin/env python3
"""GFO Election Analytics — Polling Station Mapping Helper v0.1.

Conservative helper that proposes exact-code mappings only.
It never auto-resolves split/merge/boundary changes.
"""
from __future__ import annotations

import argparse
import csv
import re
import unicodedata
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
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def norm_text(value: str | None) -> str:
    s = unicodedata.normalize("NFKD", value or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch)).upper()
    return re.sub(r"\s+", " ", s).strip()


def to_int(value: str | None) -> int | None:
    try:
        return int(float(value)) if value not in (None, "") else None
    except ValueError:
        return None


def unique_stations(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    out: dict[tuple[str, str], dict[str, str]] = {}
    for r in rows:
        key = (r.get("election_id", ""), r.get("polling_station_code", ""))
        if key[0] and key[1] and key not in out:
            out[key] = r
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Propose conservative exact-code polling-station mappings.")
    p.add_argument("historical_csv")
    p.add_argument("canonical_csv")
    p.add_argument("--canonical-election-id", required=True)
    p.add_argument("--output", default="./polling_station_mapping_proposals.csv")
    a = p.parse_args()

    hist = unique_stations(read_csv(Path(a.historical_csv)))
    canon_rows = [r for r in read_csv(Path(a.canonical_csv)) if r.get("election_id") == a.canonical_election_id]
    canon = {r.get("polling_station_code", ""): r for r in canon_rows if r.get("polling_station_code")}

    proposals: list[dict[str, Any]] = []
    for (election_id, code), h in sorted(hist.items()):
        if election_id == a.canonical_election_id:
            continue
        c = canon.get(code)
        if not c or h.get("municipality_code") != c.get("municipality_code"):
            proposals.append({
                "canonical_polling_station_code": "",
                "historical_election_id": election_id,
                "historical_polling_station_code": code,
                "mapping_type": "unmapped",
                "mapping_confidence": 0.0,
                "usable_for_baseline": "false",
                "mapping_source": f"mapping_helper_v{VERSION}",
                "notes": "No exact code+municipality match; manual review required",
            })
            continue

        hname = norm_text(h.get("polling_station_name"))
        cname = norm_text(c.get("polling_station_name"))
        hv = to_int(h.get("registered_voters"))
        cv = to_int(c.get("registered_voters"))
        voter_change_pct = None
        if hv and cv is not None:
            voter_change_pct = round((cv - hv) * 100.0 / hv, 3)

        confidence = 0.95
        notes: list[str] = ["Exact polling-station code and municipality match"]
        if hname and cname and hname == cname:
            confidence = 0.97
            notes.append("normalized names match")
        if voter_change_pct is not None:
            notes.append(f"registered-voter change {voter_change_pct:+.3f}%")
            if abs(voter_change_pct) <= 10:
                confidence = max(confidence, 0.98)
            elif abs(voter_change_pct) > 25:
                confidence = min(confidence, 0.85)
                notes.append("large voter-population change; review required")

        usable = confidence >= 0.95
        proposals.append({
            "canonical_polling_station_code": code,
            "historical_election_id": election_id,
            "historical_polling_station_code": code,
            "mapping_type": "exact_code_unverified",
            "mapping_confidence": confidence,
            "usable_for_baseline": str(usable).lower(),
            "mapping_source": f"mapping_helper_v{VERSION}",
            "historical_polling_station_name": h.get("polling_station_name", ""),
            "canonical_polling_station_name": c.get("polling_station_name", ""),
            "municipality_code": h.get("municipality_code", ""),
            "registered_voters_historical": hv if hv is not None else "",
            "registered_voters_canonical": cv if cv is not None else "",
            "registered_voter_change_pct": voter_change_pct if voter_change_pct is not None else "",
            "notes": "; ".join(notes),
        })

    write_csv(Path(a.output), proposals)
    print(f"Proposals: {len(proposals)}")
    print(f"Usable at default threshold: {sum(r['usable_for_baseline'] == 'true' for r in proposals)}")
    print(f"Output: {Path(a.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
