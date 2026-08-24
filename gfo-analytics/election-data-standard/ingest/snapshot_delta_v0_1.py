#!/usr/bin/env python3
"""GFO Election Snapshot Delta Engine v0.1

Compares two immutable GFO Election Data Standard v0.2 snapshot directories.
Produces deterministic DERIVED delta files. It does not assign anomaly scores.
"""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path
from typing import Any

ENGINE_VERSION = "0.1.0"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = []
    for r in rows:
        for k in r:
            if k not in fields:
                fields.append(k)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def num(v: Any) -> float | int | None:
    if v in (None, ""):
        return None
    try:
        f = float(v)
        return int(f) if f.is_integer() else f
    except (TypeError, ValueError):
        return None


def key_station(r):
    return r.get("polling_station_code") or r.get("polling_station_id")


def key_result(r):
    return (r.get("polling_station_id"), r.get("candidate_id") or r.get("candidate_code"))


def comparable_status(m1, m2, allow_partial: bool) -> str:
    if m1.get("election_id") != m2.get("election_id"):
        return "not_comparable"
    if not allow_partial and (m1.get("completeness_status") != "complete" or m2.get("completeness_status") != "complete"):
        return "partial_snapshot"
    return "comparable"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("snapshot_from")
    p.add_argument("snapshot_to")
    p.add_argument("--output", default="./snapshot-delta")
    p.add_argument("--allow-partial", action="store_true")
    a = p.parse_args()

    s1, s2 = Path(a.snapshot_from).resolve(), Path(a.snapshot_to).resolve()
    m1, m2 = read_json(s1 / "manifest.json"), read_json(s2 / "manifest.json")
    status = comparable_status(m1, m2, a.allow_partial)
    if status == "not_comparable":
        print("ERROR: snapshots belong to different election_id values", file=sys.stderr); return 2

    st1 = {key_station(r): r for r in read_csv(s1 / "normalized" / "polling_stations.csv")}
    st2 = {key_station(r): r for r in read_csv(s2 / "normalized" / "polling_stations.csv")}
    rs1 = {key_result(r): r for r in read_csv(s1 / "normalized" / "candidate_results.csv")}
    rs2 = {key_result(r): r for r in read_csv(s2 / "normalized" / "candidate_results.csv")}

    deltas: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []

    station_fields = ["registered_voters", "total_votes", "valid_votes", "invalid_votes", "invalid_blank_ballots", "invalid_other_ballots", "turnout_percentage"]
    for k in sorted(set(st1) | set(st2), key=str):
        r1, r2 = st1.get(k), st2.get(k)
        if r1 is None or r2 is None:
            cstatus = status if status != "comparable" else ("new_record" if r1 is None else "record_missing_from_source")
            deltas.append({"election_id": m2.get("election_id"), "polling_station_id": k, "field_name": "polling_station_presence", "candidate_id": "", "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "value_from": 0 if r1 is None else 1, "value_to": 0 if r2 is None else 1, "delta": "", "comparison_status": cstatus, "processing_module": "snapshot_delta_v0_1.py", "processing_module_version": ENGINE_VERSION})
            if status == "comparable":
                events.append({"polling_station_id": k, "candidate_id": "", "event_type": "polling_station_appeared" if r1 is None else "polling_station_disappeared", "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "old_value": 0 if r1 is None else 1, "new_value": 0 if r2 is None else 1, "comparison_status": cstatus})
            continue
        for field in station_fields:
            v1, v2 = num(r1.get(field)), num(r2.get(field))
            if v1 is None and v2 is None: continue
            d = (v2 - v1) if v1 is not None and v2 is not None else None
            deltas.append({"election_id": m2.get("election_id"), "polling_station_id": k, "field_name": field, "candidate_id": "", "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "value_from": v1, "value_to": v2, "delta": d, "source_data_from_from": r1.get("source_data_from"), "source_data_from_to": r2.get("source_data_from"), "comparison_status": status, "processing_module": "snapshot_delta_v0_1.py", "processing_module_version": ENGINE_VERSION})
            if status == "comparable" and d not in (None, 0):
                et = {"registered_voters":"registered_voter_revision", "total_votes":"turnout_revision", "valid_votes":"valid_invalid_revision", "invalid_votes":"valid_invalid_revision", "invalid_blank_ballots":"valid_invalid_revision", "invalid_other_ballots":"valid_invalid_revision"}.get(field, "turnout_revision" if field == "turnout_percentage" else "status_revision")
                events.append({"polling_station_id": k, "candidate_id": "", "event_type": et, "field_name": field, "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "old_value": v1, "new_value": v2, "delta": d, "comparison_status": status})

    for k in sorted(set(rs1) | set(rs2), key=str):
        r1, r2 = rs1.get(k), rs2.get(k)
        ps, cand = k
        if r1 is None or r2 is None:
            cstatus = status if status != "comparable" else ("new_record" if r1 is None else "record_missing_from_source")
            deltas.append({"election_id": m2.get("election_id"), "polling_station_id": ps, "field_name": "votes", "candidate_id": cand, "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "value_from": None if r1 is None else num(r1.get("votes")), "value_to": None if r2 is None else num(r2.get("votes")), "delta": "", "comparison_status": cstatus, "processing_module": "snapshot_delta_v0_1.py", "processing_module_version": ENGINE_VERSION})
            if status == "comparable":
                events.append({"polling_station_id": ps, "candidate_id": cand, "event_type": "result_appeared" if r1 is None else "result_disappeared", "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "comparison_status": cstatus})
            continue
        v1, v2 = num(r1.get("votes")), num(r2.get("votes"))
        d = (v2-v1) if v1 is not None and v2 is not None else None
        deltas.append({"election_id": m2.get("election_id"), "polling_station_id": ps, "field_name": "votes", "candidate_id": cand, "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "value_from": v1, "value_to": v2, "delta": d, "source_data_from_from": r1.get("source_data_from"), "source_data_from_to": r2.get("source_data_from"), "comparison_status": status, "processing_module": "snapshot_delta_v0_1.py", "processing_module_version": ENGINE_VERSION})
        if status == "comparable" and d not in (None, 0):
            events.append({"polling_station_id": ps, "candidate_id": cand, "event_type": "candidate_vote_increase" if d > 0 else "candidate_vote_decrease", "snapshot_from": m1.get("snapshot_id"), "snapshot_to": m2.get("snapshot_id"), "old_value": v1, "new_value": v2, "delta": d, "comparison_status": status})

    out = Path(a.output).resolve(); out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "snapshot_deltas.csv", deltas)
    write_csv(out / "revision_events.csv", events)
    (out / "delta_manifest.json").write_text(json.dumps({"engine":"snapshot_delta_v0_1.py","engine_version":ENGINE_VERSION,"election_id":m2.get("election_id"),"snapshot_from":m1.get("snapshot_id"),"snapshot_to":m2.get("snapshot_id"),"comparison_status":status,"delta_row_count":len(deltas),"revision_event_count":len(events)}, indent=2), encoding="utf-8")
    print(f"Comparison: {status}")
    print(f"Delta rows: {len(deltas)}")
    print(f"Revision events: {len(events)}")
    print(f"Output: {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
