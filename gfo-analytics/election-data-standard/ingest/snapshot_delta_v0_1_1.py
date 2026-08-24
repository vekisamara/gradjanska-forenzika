#!/usr/bin/env python3
"""GFO Election Snapshot Delta Engine v0.1.1

Compares two immutable GFO Election Data Standard v0.2 snapshot directories.
Produces deterministic DERIVED delta files. It does not assign anomaly scores.

v0.1.1 changes:
- distinguishes compared values from changed values;
- adds --changes-only to write only substantive changes to snapshot_deltas.csv;
- records compared_value_count, changed_value_count and written_delta_row_count;
- keeps zero-delta rows by default for full auditability.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

ENGINE_VERSION = "0.1.1"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, Any]], fields_if_empty: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        if fields_if_empty:
            with path.open("w", newline="", encoding="utf-8") as fh:
                csv.DictWriter(fh, fieldnames=fields_if_empty).writeheader()
        else:
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


def num(value: Any) -> float | int | None:
    if value in (None, ""):
        return None
    try:
        f = float(value)
        return int(f) if f.is_integer() else f
    except (TypeError, ValueError):
        return None


def key_station(row: dict[str, str]) -> str | None:
    return row.get("polling_station_code") or row.get("polling_station_id")


def key_result(row: dict[str, str]) -> tuple[str | None, str | None]:
    return (row.get("polling_station_id"), row.get("candidate_id") or row.get("candidate_code"))


def comparable_status(m1: dict[str, Any], m2: dict[str, Any], allow_partial: bool) -> str:
    if m1.get("election_id") != m2.get("election_id"):
        return "not_comparable"
    if not allow_partial and (
        m1.get("completeness_status") != "complete" or m2.get("completeness_status") != "complete"
    ):
        return "partial_snapshot"
    return "comparable"


def is_changed_delta(row: dict[str, Any]) -> bool:
    status = row.get("comparison_status")
    if status in {"new_record", "record_missing_from_source"}:
        return True
    delta = row.get("delta")
    return delta not in (None, "", 0, 0.0)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare two GFO election snapshots.")
    parser.add_argument("snapshot_from")
    parser.add_argument("snapshot_to")
    parser.add_argument("--output", default="./snapshot-delta")
    parser.add_argument("--allow-partial", action="store_true")
    parser.add_argument(
        "--changes-only",
        action="store_true",
        help="Write only changed values/presence changes to snapshot_deltas.csv. Full comparison remains the default.",
    )
    args = parser.parse_args()

    s1 = Path(args.snapshot_from).resolve()
    s2 = Path(args.snapshot_to).resolve()
    m1 = read_json(s1 / "manifest.json")
    m2 = read_json(s2 / "manifest.json")
    status = comparable_status(m1, m2, args.allow_partial)
    if status == "not_comparable":
        print("ERROR: snapshots belong to different election_id values", file=sys.stderr)
        return 2

    st1 = {key_station(r): r for r in read_csv(s1 / "normalized" / "polling_stations.csv")}
    st2 = {key_station(r): r for r in read_csv(s2 / "normalized" / "polling_stations.csv")}
    rs1 = {key_result(r): r for r in read_csv(s1 / "normalized" / "candidate_results.csv")}
    rs2 = {key_result(r): r for r in read_csv(s2 / "normalized" / "candidate_results.csv")}

    all_deltas: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []

    station_fields = [
        "registered_voters",
        "total_votes",
        "valid_votes",
        "invalid_votes",
        "invalid_blank_ballots",
        "invalid_other_ballots",
        "turnout_percentage",
    ]

    for key in sorted(set(st1) | set(st2), key=str):
        r1 = st1.get(key)
        r2 = st2.get(key)
        if r1 is None or r2 is None:
            cstatus = status if status != "comparable" else ("new_record" if r1 is None else "record_missing_from_source")
            all_deltas.append({
                "election_id": m2.get("election_id"),
                "polling_station_id": key,
                "field_name": "polling_station_presence",
                "candidate_id": "",
                "snapshot_from": m1.get("snapshot_id"),
                "snapshot_to": m2.get("snapshot_id"),
                "value_from": 0 if r1 is None else 1,
                "value_to": 0 if r2 is None else 1,
                "delta": "",
                "comparison_status": cstatus,
                "processing_module": "snapshot_delta_v0_1_1.py",
                "processing_module_version": ENGINE_VERSION,
            })
            if status == "comparable":
                events.append({
                    "polling_station_id": key,
                    "candidate_id": "",
                    "event_type": "polling_station_appeared" if r1 is None else "polling_station_disappeared",
                    "snapshot_from": m1.get("snapshot_id"),
                    "snapshot_to": m2.get("snapshot_id"),
                    "old_value": 0 if r1 is None else 1,
                    "new_value": 0 if r2 is None else 1,
                    "comparison_status": cstatus,
                })
            continue

        for field in station_fields:
            v1 = num(r1.get(field))
            v2 = num(r2.get(field))
            if v1 is None and v2 is None:
                continue
            delta = (v2 - v1) if v1 is not None and v2 is not None else None
            all_deltas.append({
                "election_id": m2.get("election_id"),
                "polling_station_id": key,
                "field_name": field,
                "candidate_id": "",
                "snapshot_from": m1.get("snapshot_id"),
                "snapshot_to": m2.get("snapshot_id"),
                "value_from": v1,
                "value_to": v2,
                "delta": delta,
                "source_data_from_from": r1.get("source_data_from"),
                "source_data_from_to": r2.get("source_data_from"),
                "comparison_status": status,
                "processing_module": "snapshot_delta_v0_1_1.py",
                "processing_module_version": ENGINE_VERSION,
            })
            if status == "comparable" and delta not in (None, 0):
                event_type = {
                    "registered_voters": "registered_voter_revision",
                    "total_votes": "turnout_revision",
                    "valid_votes": "valid_invalid_revision",
                    "invalid_votes": "valid_invalid_revision",
                    "invalid_blank_ballots": "valid_invalid_revision",
                    "invalid_other_ballots": "valid_invalid_revision",
                }.get(field, "turnout_revision" if field == "turnout_percentage" else "status_revision")
                events.append({
                    "polling_station_id": key,
                    "candidate_id": "",
                    "event_type": event_type,
                    "field_name": field,
                    "snapshot_from": m1.get("snapshot_id"),
                    "snapshot_to": m2.get("snapshot_id"),
                    "old_value": v1,
                    "new_value": v2,
                    "delta": delta,
                    "comparison_status": status,
                })

    for key in sorted(set(rs1) | set(rs2), key=str):
        r1 = rs1.get(key)
        r2 = rs2.get(key)
        ps, candidate = key
        if r1 is None or r2 is None:
            cstatus = status if status != "comparable" else ("new_record" if r1 is None else "record_missing_from_source")
            all_deltas.append({
                "election_id": m2.get("election_id"),
                "polling_station_id": ps,
                "field_name": "votes",
                "candidate_id": candidate,
                "snapshot_from": m1.get("snapshot_id"),
                "snapshot_to": m2.get("snapshot_id"),
                "value_from": None if r1 is None else num(r1.get("votes")),
                "value_to": None if r2 is None else num(r2.get("votes")),
                "delta": "",
                "comparison_status": cstatus,
                "processing_module": "snapshot_delta_v0_1_1.py",
                "processing_module_version": ENGINE_VERSION,
            })
            if status == "comparable":
                events.append({
                    "polling_station_id": ps,
                    "candidate_id": candidate,
                    "event_type": "result_appeared" if r1 is None else "result_disappeared",
                    "snapshot_from": m1.get("snapshot_id"),
                    "snapshot_to": m2.get("snapshot_id"),
                    "comparison_status": cstatus,
                })
            continue

        v1 = num(r1.get("votes"))
        v2 = num(r2.get("votes"))
        delta = (v2 - v1) if v1 is not None and v2 is not None else None
        all_deltas.append({
            "election_id": m2.get("election_id"),
            "polling_station_id": ps,
            "field_name": "votes",
            "candidate_id": candidate,
            "snapshot_from": m1.get("snapshot_id"),
            "snapshot_to": m2.get("snapshot_id"),
            "value_from": v1,
            "value_to": v2,
            "delta": delta,
            "source_data_from_from": r1.get("source_data_from"),
            "source_data_from_to": r2.get("source_data_from"),
            "comparison_status": status,
            "processing_module": "snapshot_delta_v0_1_1.py",
            "processing_module_version": ENGINE_VERSION,
        })
        if status == "comparable" and delta not in (None, 0):
            events.append({
                "polling_station_id": ps,
                "candidate_id": candidate,
                "event_type": "candidate_vote_increase" if delta > 0 else "candidate_vote_decrease",
                "snapshot_from": m1.get("snapshot_id"),
                "snapshot_to": m2.get("snapshot_id"),
                "old_value": v1,
                "new_value": v2,
                "delta": delta,
                "comparison_status": status,
            })

    changed_deltas = [row for row in all_deltas if is_changed_delta(row)]
    output_deltas = changed_deltas if args.changes_only else all_deltas

    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)
    delta_fields = [
        "election_id", "polling_station_id", "field_name", "candidate_id",
        "snapshot_from", "snapshot_to", "value_from", "value_to", "delta",
        "source_data_from_from", "source_data_from_to", "comparison_status",
        "processing_module", "processing_module_version",
    ]
    event_fields = [
        "polling_station_id", "candidate_id", "event_type", "field_name",
        "snapshot_from", "snapshot_to", "old_value", "new_value", "delta", "comparison_status",
    ]
    write_csv(out / "snapshot_deltas.csv", output_deltas, delta_fields)
    write_csv(out / "revision_events.csv", events, event_fields)

    manifest = {
        "engine": "snapshot_delta_v0_1_1.py",
        "engine_version": ENGINE_VERSION,
        "election_id": m2.get("election_id"),
        "snapshot_from": m1.get("snapshot_id"),
        "snapshot_to": m2.get("snapshot_id"),
        "comparison_status": status,
        "changes_only": args.changes_only,
        "compared_value_count": len(all_deltas),
        "changed_value_count": len(changed_deltas),
        "written_delta_row_count": len(output_deltas),
        "revision_event_count": len(events),
    }
    (out / "delta_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Comparison: {status}")
    print(f"Compared values: {len(all_deltas)}")
    print(f"Changed values: {len(changed_deltas)}")
    print(f"Revision events: {len(events)}")
    print(f"Written delta rows: {len(output_deltas)}")
    print(f"Output: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
