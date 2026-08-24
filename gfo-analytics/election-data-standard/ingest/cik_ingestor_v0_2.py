#!/usr/bin/env python3
"""GFO Election Data Standard — CIK API Snapshot Ingestor v0.2

Features:
- bounded parallel polling-station retrieval;
- retry with exponential backoff;
- immutable snapshot directories;
- snapshot/record retrieval timestamps;
- completeness accounting;
- byte-preserved RAW JSON + SHA-256 provenance;
- normalized CSV outputs and validation findings.

The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import sys
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = "https://www.izbori.ba/api_2018"
DEFAULT_DB = "WebResult_2022GENP1_2025_11_19_14_41_56"
DEFAULT_LANGUAGE_ID = 3
DEFAULT_ELECTION_RESULT_ID = 39
DEFAULT_RACE_ID = 91
DEFAULT_RACE_CODE = "5"
INGESTOR_VERSION = "0.2.0"
STANDARD_TARGET = "0.2-draft"
USER_AGENT = "GFO-Election-Analytics/0.2 (+https://github.com/vekisamara/gradjanska-forenzika)"

_PRINT_LOCK = threading.Lock()


@dataclass
class ProvenanceRecord:
    dataset_id: str
    snapshot_id: str
    source_type: str
    source_name: str
    source_url: str
    retrieved_at: str
    verification_status: str
    sha256: str
    raw_file: str
    request_status: str


@dataclass
class ValidationFlag:
    record_id: str
    rule_code: str
    severity: str
    message: str
    processing_module: str
    processing_module_version: str


@dataclass
class FetchResult:
    data: Any
    raw: bytes
    url: str
    retrieved_at: str
    attempts: int


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def snapshot_id_now() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    return f"snapshot-{stamp}-{uuid.uuid4().hex[:8]}"


def safe_print(message: str) -> None:
    with _PRINT_LOCK:
        print(message, flush=True)


def endpoint(path: str) -> str:
    return f"{BASE_URL}/{path.lstrip('/')}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch_json(url: str, *, timeout: int, retries: int, backoff: float, jitter: float) -> FetchResult:
    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
            retrieved_at = utc_now()
            try:
                data = json.loads(raw.decode("utf-8-sig"))
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Endpoint did not return valid JSON: {url}") from exc
            return FetchResult(data=data, raw=raw, url=url, retrieved_at=retrieved_at, attempts=attempt)
        except (HTTPError, URLError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            if attempt > retries:
                break
            sleep_for = backoff * (2 ** (attempt - 1)) + random.uniform(0, max(0.0, jitter))
            time.sleep(sleep_for)
    raise RuntimeError(f"Request failed after {retries + 1} attempts: {url}: {last_error}")


def first_present(d: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in d:
            return d[key]
    return None


def save_raw(snapshot_dir: Path, snapshot_id: str, name: str, fetch: FetchResult) -> ProvenanceRecord:
    raw_dir = snapshot_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / name
    if path.exists():
        raise RuntimeError(f"Immutable snapshot collision: {path}")
    path.write_bytes(fetch.raw)
    return ProvenanceRecord(
        dataset_id=path.stem,
        snapshot_id=snapshot_id,
        source_type="official",
        source_name="Centralna izborna komisija Bosne i Hercegovine",
        source_url=fetch.url,
        retrieved_at=fetch.retrieved_at,
        verification_status="official",
        sha256=sha256_bytes(fetch.raw),
        raw_file=str(path.relative_to(snapshot_dir)),
        request_status="success",
    )


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


def normalize_polling_station(election_id: str, snapshot_id: str, eu: dict[str, Any], ps: dict[str, Any], basic: dict[str, Any], record_retrieved_at: str) -> dict[str, Any]:
    registered = first_present(basic, "numberOfVoters", "NumberOfVoters")
    total = first_present(basic, "totalVotes", "TotalVotes")
    turnout = first_present(basic, "percentageTotalVotes", "PercentageTotalVotes")
    if turnout is None and isinstance(registered, (int, float)) and registered and isinstance(total, (int, float)):
        turnout = round(total * 100 / registered, 6)
    return {
        "election_id": election_id,
        "snapshot_id": snapshot_id,
        "record_retrieved_at": record_retrieved_at,
        "electoral_unit_id": first_present(eu, "electoralUnitId", "ElectoralUnitId"),
        "municipality_code": first_present(eu, "code", "Code"),
        "municipality_name": first_present(eu, "name", "Name"),
        "polling_station_id": first_present(ps, "pollingStationId", "PollingStationId"),
        "polling_station_code": first_present(ps, "code", "Code"),
        "polling_station_name": first_present(ps, "name", "Name"),
        "location": first_present(basic, "location", "Location", "pollingStationLocation", "PollingStationLocation"),
        "registered_voters": registered,
        "total_votes": total,
        "valid_votes": first_present(basic, "validVotes", "ValidVotes"),
        "invalid_votes": first_present(basic, "totalInvalidVotes", "TotalInvalidVotes"),
        "invalid_blank_ballots": first_present(basic, "invalidBlankBallots", "InvalidBlankBallots"),
        "invalid_other_ballots": first_present(basic, "invalidOthersBallots", "InvalidOthersBallots"),
        "turnout_percentage": turnout,
        "number_candidates": first_present(basic, "numberCandidates", "NumberCandidates"),
        "source_data_from": first_present(basic, "dataFrom", "DataFrom"),
    }


def normalize_candidate_result(election_id: str, snapshot_id: str, polling_station_id: Any, result: dict[str, Any], record_retrieved_at: str) -> dict[str, Any]:
    candidate_code = first_present(result, "code", "Code", "candidateCode", "CandidateCode")
    return {
        "election_id": election_id,
        "snapshot_id": snapshot_id,
        "record_retrieved_at": record_retrieved_at,
        "polling_station_id": polling_station_id,
        "candidate_id": candidate_code or first_present(result, "candidateId", "CandidateId", "id", "Id"),
        "candidate_code": candidate_code,
        "candidate_name": first_present(result, "name", "Name", "candidateName", "CandidateName"),
        "votes": first_present(result, "totalVotes", "TotalVotes", "votes", "Votes", "numberOfVotes", "NumberOfVotes"),
        "vote_percentage": first_present(result, "percentage", "Percentage", "percentageVotes", "PercentageVotes"),
        "party_name": first_present(result, "politicalSubjectName", "PoliticalSubjectName", "partyName", "PartyName"),
        "source_data_from": first_present(result, "dataFrom", "DataFrom"),
    }


def validate_station(station: dict[str, Any], candidate_rows: list[dict[str, Any]]) -> list[ValidationFlag]:
    flags: list[ValidationFlag] = []
    rid = str(station.get("polling_station_code") or station.get("polling_station_id"))
    registered = station.get("registered_voters")
    total = station.get("total_votes")
    valid = station.get("valid_votes")
    invalid = station.get("invalid_votes")
    blank = station.get("invalid_blank_ballots")
    other = station.get("invalid_other_ballots")

    def add(rule: str, severity: str, message: str) -> None:
        flags.append(ValidationFlag(rid, rule, severity, message, "cik_ingestor_v0_2.py", INGESTOR_VERSION))

    if isinstance(total, (int, float)) and isinstance(registered, (int, float)) and total > registered:
        add("GFO-E-V001", "error", f"total_votes={total} exceeds registered_voters={registered}")
    if all(isinstance(x, (int, float)) for x in (valid, invalid, total)) and valid + invalid != total:
        add("GFO-E-V002", "error", f"valid_votes + invalid_votes = {valid + invalid}, total_votes={total}")
    if all(isinstance(x, (int, float)) for x in (blank, other, invalid)) and blank + other != invalid:
        add("GFO-E-V003", "warning", f"invalid components={blank + other}, invalid_votes={invalid}")
    votes = [r.get("votes") for r in candidate_rows]
    if candidate_rows and all(isinstance(v, (int, float)) for v in votes) and isinstance(valid, (int, float)):
        vote_sum = sum(votes)
        if vote_sum != valid:
            add("GFO-E-V004", "error", f"candidate vote sum={vote_sum}, valid_votes={valid}")
    if not station.get("polling_station_code"):
        add("GFO-E-V005", "error", "missing polling_station_code")
    return flags


def get_electoral_units(args: argparse.Namespace) -> FetchResult:
    url = endpoint(f"race5_electoralunit/{args.db_name}/{args.language_id}")
    return fetch_json(url, timeout=args.timeout, retries=args.retries, backoff=args.backoff, jitter=args.jitter)


def get_polling_stations(args: argparse.Namespace, electoral_unit_id: int) -> FetchResult:
    url = endpoint(f"race5_pollingstation/{args.db_name}/{electoral_unit_id}/{args.language_id}")
    return fetch_json(url, timeout=args.timeout, retries=args.retries, backoff=args.backoff, jitter=args.jitter)


def fetch_polling_station_bundle(args: argparse.Namespace, snapshot_id: str, eu: dict[str, Any], ps: dict[str, Any]) -> dict[str, Any]:
    ps_id = int(first_present(ps, "pollingStationId", "PollingStationId"))
    basic_url = endpoint(f"race5_pollingstationsbasicinfo/{args.db_name}/{ps_id}")
    result_url = endpoint(f"race5_pollingstationscandidatesresult/{args.db_name}/{ps_id}/{args.language_id}")

    basic_fetch = fetch_json(basic_url, timeout=args.timeout, retries=args.retries, backoff=args.backoff, jitter=args.jitter)
    result_fetch = fetch_json(result_url, timeout=args.timeout, retries=args.retries, backoff=args.backoff, jitter=args.jitter)
    if not isinstance(basic_fetch.data, dict):
        raise RuntimeError(f"Unexpected basic-info response for pollingStationId={ps_id}")
    if not isinstance(result_fetch.data, list):
        raise RuntimeError(f"Unexpected candidate-result response for pollingStationId={ps_id}")

    station = normalize_polling_station(args.election_id, snapshot_id, eu, ps, basic_fetch.data, basic_fetch.retrieved_at)
    candidate_rows = [normalize_candidate_result(args.election_id, snapshot_id, ps_id, row, result_fetch.retrieved_at) for row in result_fetch.data]
    return {
        "ps_id": ps_id,
        "station": station,
        "candidate_rows": candidate_rows,
        "basic_fetch": basic_fetch,
        "result_fetch": result_fetch,
    }


def compute_manifest_hash(snapshot_dir: Path) -> str:
    targets = [
        snapshot_dir / "normalized" / "polling_stations.csv",
        snapshot_dir / "normalized" / "candidate_results.csv",
        snapshot_dir / "provenance.csv",
        snapshot_dir / "validation_flags.csv",
    ]
    h = hashlib.sha256()
    for path in targets:
        if path.exists():
            h.update(path.name.encode("utf-8"))
            h.update(sha256_file(path).encode("ascii"))
    return h.hexdigest()


def run_once(args: argparse.Namespace) -> Path:
    root = Path(args.output).resolve()
    root.mkdir(parents=True, exist_ok=True)
    snapshot_id = snapshot_id_now()
    snapshot_dir = root / "snapshots" / snapshot_id
    if snapshot_dir.exists():
        raise RuntimeError(f"Snapshot already exists: {snapshot_dir}")
    snapshot_dir.mkdir(parents=True, exist_ok=False)

    started_at = utc_now()
    safe_print(f"snapshot_id: {snapshot_id}")
    safe_print(f"dbName: {args.db_name}")
    safe_print(f"workers: {args.workers}")

    provenance: list[ProvenanceRecord] = []
    validation_flags: list[ValidationFlag] = []
    normalized_stations: list[dict[str, Any]] = []
    normalized_results: list[dict[str, Any]] = []
    failed_requests: list[dict[str, Any]] = []
    request_successes = 0

    units_fetch = get_electoral_units(args)
    request_successes += 1
    if not isinstance(units_fetch.data, list):
        raise RuntimeError("Unexpected electoral unit response")
    units = units_fetch.data
    provenance.append(save_raw(snapshot_dir, snapshot_id, "electoral_units.json", units_fetch))

    if args.electoral_unit_id is not None:
        units = [u for u in units if first_present(u, "electoralUnitId", "ElectoralUnitId") == args.electoral_unit_id]
        if not units:
            raise RuntimeError(f"electoralUnitId={args.electoral_unit_id} not found")

    expected_polling_stations = 0

    for eu in units:
        eu_id = int(first_present(eu, "electoralUnitId", "ElectoralUnitId"))
        eu_code = first_present(eu, "code", "Code")
        safe_print(f"Electoral unit {eu_id} ({eu_code})")

        try:
            stations_fetch = get_polling_stations(args, eu_id)
            request_successes += 1
            if not isinstance(stations_fetch.data, list):
                raise RuntimeError("Unexpected polling station response")
            stations = stations_fetch.data
            expected_polling_stations += len(stations)
            provenance.append(save_raw(snapshot_dir, snapshot_id, f"polling_stations_eu_{eu_id}.json", stations_fetch))
        except Exception as exc:
            failed_requests.append({"scope": "electoral_unit", "electoral_unit_id": eu_id, "error": str(exc)})
            safe_print(f"  ERROR electoral unit {eu_id}: {exc}")
            continue

        completed = 0
        with ThreadPoolExecutor(max_workers=args.workers, thread_name_prefix="gfo-cik") as pool:
            futures = {pool.submit(fetch_polling_station_bundle, args, snapshot_id, eu, ps): ps for ps in stations}
            for future in as_completed(futures):
                ps = futures[future]
                ps_id = first_present(ps, "pollingStationId", "PollingStationId")
                try:
                    bundle = future.result()
                    request_successes += 2
                    provenance.append(save_raw(snapshot_dir, snapshot_id, f"polling_station_{bundle['ps_id']}_basic.json", bundle["basic_fetch"]))
                    provenance.append(save_raw(snapshot_dir, snapshot_id, f"polling_station_{bundle['ps_id']}_candidates.json", bundle["result_fetch"]))
                    normalized_stations.append(bundle["station"])
                    normalized_results.extend(bundle["candidate_rows"])
                    validation_flags.extend(validate_station(bundle["station"], bundle["candidate_rows"]))
                    completed += 1
                    safe_print(f"  {completed}/{len(stations)} pollingStationId={bundle['ps_id']}")
                except Exception as exc:
                    failed_requests.append({"scope": "polling_station", "electoral_unit_id": eu_id, "polling_station_id": ps_id, "error": str(exc)})
                    safe_print(f"  ERROR pollingStationId={ps_id}: {exc}")

    normalized_stations.sort(key=lambda r: (str(r.get("municipality_code") or ""), str(r.get("polling_station_code") or "")))
    normalized_results.sort(key=lambda r: (str(r.get("polling_station_id") or ""), str(r.get("candidate_code") or "")))

    normalized_dir = snapshot_dir / "normalized"
    write_csv(normalized_dir / "polling_stations.csv", normalized_stations)
    write_csv(normalized_dir / "candidate_results.csv", normalized_results)
    write_csv(snapshot_dir / "provenance.csv", [asdict(p) for p in provenance])
    write_csv(snapshot_dir / "validation_flags.csv", [asdict(v) for v in validation_flags])
    write_csv(snapshot_dir / "failed_requests.csv", failed_requests)

    completed_at = utc_now()
    source_times = [r.get("source_data_from") for r in normalized_stations + normalized_results if r.get("source_data_from")]
    source_time_values = sorted({str(v) for v in source_times})
    parsed_source_times: list[datetime] = []
    for value in source_time_values:
        try:
            parsed_source_times.append(datetime.fromisoformat(value.replace("Z", "+00:00")))
        except ValueError:
            pass

    completeness = "complete" if not failed_requests and len(normalized_stations) == expected_polling_stations else "partial"
    if not normalized_stations:
        completeness = "failed" if failed_requests else "unknown"

    manifest = {
        "standard": "GFO Election Data Standard",
        "standard_version": STANDARD_TARGET,
        "ingestor": "cik_ingestor_v0_2.py",
        "ingestor_version": INGESTOR_VERSION,
        "snapshot_id": snapshot_id,
        "previous_snapshot_id": args.previous_snapshot_id,
        "election_id": args.election_id,
        "election_result_id": args.election_result_id,
        "race_id": DEFAULT_RACE_ID,
        "race_code": DEFAULT_RACE_CODE,
        "db_name": args.db_name,
        "language_id": args.language_id,
        "snapshot_started_at": started_at,
        "snapshot_completed_at": completed_at,
        "retrieved_at": completed_at,
        "source_data_from_values": source_time_values,
        "source_data_from_min": min(parsed_source_times).isoformat() if parsed_source_times and len(parsed_source_times) == len(source_time_values) else None,
        "source_data_from_max": max(parsed_source_times).isoformat() if parsed_source_times and len(parsed_source_times) == len(source_time_values) else None,
        "completeness_status": completeness,
        "record_count": len(normalized_stations) + len(normalized_results),
        "polling_station_count": len(normalized_stations),
        "candidate_result_row_count": len(normalized_results),
        "expected_polling_station_count": expected_polling_stations,
        "successful_request_count": request_successes,
        "failed_request_count": len(failed_requests),
        "workers": args.workers,
        "retries": args.retries,
        "backoff_seconds": args.backoff,
        "timeout_seconds": args.timeout,
        "validation_flag_count": len(validation_flags),
    }
    manifest["dataset_hash"] = compute_manifest_hash(snapshot_dir)
    (snapshot_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    latest = root / "LATEST"
    latest.write_text(snapshot_id + "\n", encoding="utf-8")

    safe_print(f"Validation flags: {len(validation_flags)}")
    safe_print(f"Failed requests: {len(failed_requests)}")
    safe_print(f"Completeness: {completeness}")
    safe_print(f"Done. Snapshot: {snapshot_dir}")
    return snapshot_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download CIK BiH Race5 results as immutable GFO temporal snapshots.")
    parser.add_argument("--output", default="./cik-snapshots", help="Root output directory; snapshots are created below output/snapshots/")
    parser.add_argument("--election-result-id", type=int, default=DEFAULT_ELECTION_RESULT_ID)
    parser.add_argument("--db-name", default=DEFAULT_DB)
    parser.add_argument("--language-id", type=int, default=DEFAULT_LANGUAGE_ID)
    parser.add_argument("--election-id", default="2025-BIH-RS-PRES-BYELECTION-CONFIRMED")
    parser.add_argument("--electoral-unit-id", type=int, help="Limit download to one electoral unit; e.g. 7 for Novi Grad")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent polling-station workers (recommended 4-8)")
    parser.add_argument("--retries", type=int, default=3, help="Retries after the initial request")
    parser.add_argument("--backoff", type=float, default=1.0, help="Initial exponential backoff in seconds")
    parser.add_argument("--jitter", type=float, default=0.25, help="Random jitter added to retries")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout per request in seconds")
    parser.add_argument("--previous-snapshot-id", help="Optional explicit link to the previous snapshot")
    parser.add_argument("--watch", action="store_true", help="Repeat snapshot acquisition until interrupted")
    parser.add_argument("--interval", type=int, default=1800, help="Seconds between snapshot starts in --watch mode (default 1800)")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.workers < 1 or args.workers > 32:
        raise SystemExit("--workers must be between 1 and 32")
    if args.retries < 0:
        raise SystemExit("--retries must be >= 0")
    if args.interval < 60:
        raise SystemExit("--interval must be at least 60 seconds")

    try:
        if not args.watch:
            run_once(args)
            return 0

        previous = args.previous_snapshot_id
        while True:
            cycle_started = time.monotonic()
            args.previous_snapshot_id = previous
            snapshot_dir = run_once(args)
            previous = snapshot_dir.name
            elapsed = time.monotonic() - cycle_started
            sleep_for = max(0.0, args.interval - elapsed)
            safe_print(f"Next snapshot in {sleep_for:.1f}s")
            time.sleep(sleep_for)
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
