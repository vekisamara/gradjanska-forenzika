#!/usr/bin/env python3
"""Convert one GFO v0.2 snapshot into Historical Baseline canonical long-form input."""
from __future__ import annotations

import argparse
import csv
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
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def main() -> int:
    p = argparse.ArgumentParser(description="Convert a GFO election snapshot to Historical Baseline input rows.")
    p.add_argument("snapshot_dir")
    p.add_argument("--election-id", required=True)
    p.add_argument("--election-date", required=True)
    p.add_argument("--election-type", required=True)
    p.add_argument("--source-id", required=True)
    p.add_argument("--turnout-eligible", choices=["true", "false"], default="true")
    p.add_argument("--structural-eligible", choices=["true", "false"], default="true")
    p.add_argument("--political-share-eligible", choices=["true", "false"], default="true")
    p.add_argument("--output", default="./historical_input.csv")
    a = p.parse_args()

    root = Path(a.snapshot_dir)
    stations = read_csv(root / "normalized" / "polling_stations.csv")
    results = read_csv(root / "normalized" / "candidate_results.csv")
    station_by_id = {r.get("polling_station_id", ""): r for r in stations}

    out_rows: list[dict[str, Any]] = []
    for r in results:
        s = station_by_id.get(r.get("polling_station_id", ""))
        if not s:
            continue
        out_rows.append({
            "election_id": a.election_id,
            "election_date": a.election_date,
            "election_type": a.election_type,
            "turnout_eligible": a.turnout_eligible,
            "structural_eligible": a.structural_eligible,
            "political_share_eligible": a.political_share_eligible,
            "polling_station_id": s.get("polling_station_id", ""),
            "polling_station_code": s.get("polling_station_code", ""),
            "polling_station_name": s.get("polling_station_name", ""),
            "municipality_code": s.get("municipality_code", ""),
            "registered_voters": s.get("registered_voters", ""),
            "total_votes": s.get("total_votes", ""),
            "valid_votes": s.get("valid_votes", ""),
            "invalid_votes": s.get("invalid_votes", ""),
            "candidate_id": r.get("candidate_id", ""),
            "candidate_code": r.get("candidate_code", ""),
            "candidate_name": r.get("candidate_name", ""),
            "party_id": "",
            "party_name": r.get("party_name", ""),
            "political_bloc_id": "",
            "votes": r.get("votes", ""),
            "source_id": a.source_id,
            "source_data_from": s.get("source_data_from", "") or r.get("source_data_from", ""),
        })

    write_csv(Path(a.output), out_rows)
    print(f"Historical rows: {len(out_rows)}")
    print(f"Polling stations represented: {len({r['polling_station_code'] for r in out_rows})}")
    print(f"Output: {Path(a.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
