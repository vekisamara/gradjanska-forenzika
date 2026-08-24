#!/usr/bin/env python3
"""GFO Election Data Standard — CIK API Ingestor v0.1.1

Purpose:
- download official CIK BiH Race5 election data;
- preserve RAW JSON responses byte-for-byte;
- emit normalized CSV files compatible with the GFO Election Data Standard work-in-progress;
- record provenance and basic validation findings.

Confirmed target for the 2025 RS presidential by-election confirmed results:
- electionResultId: 39
- raceId: 91
- race code: 5
- dbName: WebResult_2022GENP1_2025_11_19_14_41_56
- languageId: 3

The script uses only Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from dataclasses import dataclass, asdict
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
INGESTOR_VERSION = "0.1.1"
USER_AGENT = "GFO-Election-Analytics/0.1.1 (+https://github.com/vekisamara/gradjanska-forenzika)"


@dataclass
class ProvenanceRecord:
    dataset_id: str
    source_type: str
    source_name: str
    source_url: str
    retrieved_at: str
    verification_status: str
    sha256: str
    raw_file: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def fetch_json(url: str, timeout: int = 30) -> tuple[Any, bytes]:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error for {url}: {exc}") from exc
    try:
        return json.loads(raw.decode("utf-8-sig")), raw
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Endpoint did not return valid JSON: {url}") from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save_raw_json(out_dir: Path, name: str, raw: bytes, source_url: str) -> ProvenanceRecord:
    raw_dir = out_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / name
    path.write_bytes(raw)
    return ProvenanceRecord(
        dataset_id=path.stem,
        source_type="official",
        source_name="Centralna izborna komisija Bosne i Hercegovine",
        source_url=source_url,
        retrieved_at=utc_now(),
        verification_status="official",
        sha256=sha256_bytes(raw),
        raw_file=str(path.relative_to(out_dir)),
    )


def endpoint(path: str) -> str:
    return f"{BASE_URL}/{path.lstrip('/')}"


def get_db_name(election_result_id: int) -> str:
    url = endpoint(f"administration_electionresultcontroller_getdatabasename/{election_result_id}")
    data, _ = fetch_json(url)
    if not isinstance(data, str):
        raise RuntimeError(f"Unexpected dbName response: {data!r}")
    return data


def get_electoral_units(db_name: str, language_id: int) -> tuple[list[dict[str, Any]], bytes, str]:
    url = endpoint(f"race5_electoralunit/{db_name}/{language_id}")
    data, raw = fetch_json(url)
    if not isinstance(data, list):
        raise RuntimeError("Unexpected electoral unit response")
    return data, raw, url


def get_polling_stations(db_name: str, electoral_unit_id: int, language_id: int) -> tuple[list[dict[str, Any]], bytes, str]:
    url = endpoint(f"race5_pollingstation/{db_name}/{electoral_unit_id}/{language_id}")
    data, raw = fetch_json(url)
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected polling station response for electoralUnitId={electoral_unit_id}")
    return data, raw, url


def get_polling_station_basic_info(db_name: str, polling_station_id: int) -> tuple[dict[str, Any], bytes, str]:
    url = endpoint(f"race5_pollingstationsbasicinfo/{db_name}/{polling_station_id}")
    data, raw = fetch_json(url)
    if not isinstance(data, dict):
        raise RuntimeError(f"Unexpected basic-info response for pollingStationId={polling_station_id}")
    return data, raw, url


def get_polling_station_candidate_results(db_name: str, polling_station_id: int, language_id: int) -> tuple[list[dict[str, Any]], bytes, str]:
    url = endpoint(f"race5_pollingstationscandidatesresult/{db_name}/{polling_station_id}/{language_id}")
    data, raw = fetch_json(url)
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected candidate-result response for pollingStationId={polling_station_id}")
    return data, raw, url


def first_present(d: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in d:
            return d[key]
    return None


def normalize_polling_station(election_id: str, eu: dict[str, Any], ps: dict[str, Any], basic: dict[str, Any]) -> dict[str, Any]:
    return {
        "election_id": election_id,
        "electoral_unit_id": first_present(eu, "electoralUnitId", "ElectoralUnitId"),
        "municipality_code": first_present(eu, "code", "Code"),
        "municipality_name": first_present(eu, "name", "Name"),
        "polling_station_id": first_present(ps, "pollingStationId", "PollingStationId"),
        "polling_station_code": first_present(ps, "code", "Code"),
        "polling_station_name": first_present(ps, "name", "Name"),
        "location": first_present(ps, "location", "Location"),
        "source_data_from": first_present(ps, "dataFrom", "DataFrom"),
        "active": first_present(ps, "active", "Active"),
        "registered_voters": first_present(basic, "numberOfVoters", "NumberOfVoters"),
        "number_candidates": first_present(basic, "numberCandidates", "NumberCandidates"),
        "total_votes": first_present(basic, "totalVotes", "TotalVotes"),
        "turnout_percentage": first_present(basic, "percentageTotalVotes", "PercentageTotalVotes"),
        "valid_votes": first_present(basic, "validVotes", "ValidVotes"),
        "invalid_votes": first_present(basic, "totalInvalidVotes", "TotalInvalidVotes"),
        "invalid_blank_ballots": first_present(basic, "invalidBlankBallots", "InvalidBlankBallots"),
        "invalid_other_ballots": first_present(basic, "invalidOthersBallots", "InvalidOthersBallots"),
    }


def normalize_candidate_result(election_id: str, polling_station_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    # Actual CIK Race5 payload observed in validation case:
    # {"name": "...", "code": "00018", "totalVotes": 121, "percentage": 55.0}
    return {
        "election_id": election_id,
        "polling_station_id": polling_station_id,
        "candidate_code": first_present(result, "code", "Code"),
        "candidate_id": first_present(result, "candidateId", "CandidateId", "id", "Id", "code", "Code"),
        "candidate_name": first_present(result, "candidateName", "CandidateName", "name", "Name"),
        "votes": first_present(result, "votes", "Votes", "numberOfVotes", "NumberOfVotes", "totalVotes", "TotalVotes"),
        "vote_percentage": first_present(result, "percentage", "Percentage", "percentageVotes", "PercentageVotes"),
        "party_name": first_present(result, "politicalSubjectName", "PoliticalSubjectName", "partyName", "PartyName"),
    }


def validate_station(station: dict[str, Any], candidate_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    flags: list[dict[str, Any]] = []
    ps_id = station.get("polling_station_id")

    def flag(code: str, severity: str, message: str) -> None:
        flags.append({
            "polling_station_id": ps_id,
            "code": code,
            "severity": severity,
            "message": message,
        })

    registered = station.get("registered_voters")
    total = station.get("total_votes")
    valid = station.get("valid_votes")
    invalid = station.get("invalid_votes")
    blank = station.get("invalid_blank_ballots")
    other = station.get("invalid_other_ballots")

    numeric = (int, float)
    if isinstance(total, numeric) and isinstance(registered, numeric) and total > registered:
        flag("TOTAL_GT_REGISTERED", "error", f"total_votes={total} > registered_voters={registered}")

    if all(isinstance(v, numeric) for v in (valid, invalid, total)) and valid + invalid != total:
        flag("VALID_INVALID_MISMATCH", "error", f"valid_votes + invalid_votes = {valid + invalid}, total_votes={total}")

    if all(isinstance(v, numeric) for v in (blank, other, invalid)) and blank + other != invalid:
        flag("INVALID_COMPONENT_MISMATCH", "warning", f"blank + other = {blank + other}, invalid_votes={invalid}")

    vote_values = [row.get("votes") for row in candidate_rows]
    if vote_values and all(isinstance(v, numeric) for v in vote_values) and isinstance(valid, numeric):
        candidate_sum = sum(vote_values)
        if candidate_sum != valid:
            flag("CANDIDATE_SUM_MISMATCH", "error", f"candidate vote sum={candidate_sum}, valid_votes={valid}")

    if station.get("polling_station_id") in (None, ""):
        flag("MISSING_POLLING_STATION_ID", "error", "polling_station_id missing")
    if station.get("polling_station_code") in (None, ""):
        flag("MISSING_POLLING_STATION_CODE", "error", "polling_station_code missing")

    return flags


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


def run(args: argparse.Namespace) -> None:
    out_dir = Path(args.output).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    provenance: list[ProvenanceRecord] = []

    db_name = args.db_name or get_db_name(args.election_result_id)
    print(f"dbName: {db_name}")

    election_id = args.election_id
    units, raw, url = get_electoral_units(db_name, args.language_id)
    provenance.append(save_raw_json(out_dir, "electoral_units.json", raw, url))

    if args.electoral_unit_id is not None:
        units = [u for u in units if first_present(u, "electoralUnitId", "ElectoralUnitId") == args.electoral_unit_id]
        if not units:
            raise RuntimeError(f"electoralUnitId={args.electoral_unit_id} not found")

    normalized_stations: list[dict[str, Any]] = []
    normalized_results: list[dict[str, Any]] = []
    validation_flags: list[dict[str, Any]] = []

    for eu in units:
        eu_id = int(first_present(eu, "electoralUnitId", "ElectoralUnitId"))
        eu_code = first_present(eu, "code", "Code")
        print(f"Electoral unit {eu_id} ({eu_code})")

        stations, raw, url = get_polling_stations(db_name, eu_id, args.language_id)
        provenance.append(save_raw_json(out_dir, f"polling_stations_eu_{eu_id}.json", raw, url))

        for index, ps in enumerate(stations, start=1):
            ps_id = int(first_present(ps, "pollingStationId", "PollingStationId"))
            basic, basic_raw, basic_url = get_polling_station_basic_info(db_name, ps_id)
            provenance.append(save_raw_json(out_dir, f"polling_station_{ps_id}_basic.json", basic_raw, basic_url))

            results, result_raw, result_url = get_polling_station_candidate_results(db_name, ps_id, args.language_id)
            provenance.append(save_raw_json(out_dir, f"polling_station_{ps_id}_candidates.json", result_raw, result_url))

            station_row = normalize_polling_station(election_id, eu, ps, basic)
            candidate_rows = [normalize_candidate_result(election_id, ps_id, row) for row in results]
            normalized_stations.append(station_row)
            normalized_results.extend(candidate_rows)
            validation_flags.extend(validate_station(station_row, candidate_rows))

            print(f"  {index}/{len(stations)} pollingStationId={ps_id}")
            if args.delay:
                time.sleep(args.delay)

    normalized_dir = out_dir / "normalized"
    write_csv(normalized_dir / "polling_stations.csv", normalized_stations)
    write_csv(normalized_dir / "candidate_results.csv", normalized_results)
    write_csv(out_dir / "provenance.csv", [asdict(p) for p in provenance])
    write_csv(out_dir / "validation_flags.csv", validation_flags)

    manifest = {
        "standard": "GFO Election Data Standard",
        "standard_version": "0.2-draft-target",
        "ingestor": "cik_ingestor_v0_1.py",
        "ingestor_version": INGESTOR_VERSION,
        "election_id": election_id,
        "election_result_id": args.election_result_id,
        "race_id": DEFAULT_RACE_ID,
        "race_code": DEFAULT_RACE_CODE,
        "db_name": db_name,
        "language_id": args.language_id,
        "retrieved_at": utc_now(),
        "polling_station_count": len(normalized_stations),
        "candidate_result_row_count": len(normalized_results),
        "validation_flag_count": len(validation_flags),
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Validation flags: {len(validation_flags)}")
    print(f"Done. Output: {out_dir}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download CIK BiH Race5 results into a GFO working dataset.")
    parser.add_argument("--output", default="./cik-output", help="Output directory")
    parser.add_argument("--election-result-id", type=int, default=DEFAULT_ELECTION_RESULT_ID)
    parser.add_argument("--db-name", default=DEFAULT_DB)
    parser.add_argument("--language-id", type=int, default=DEFAULT_LANGUAGE_ID)
    parser.add_argument("--election-id", default="2025-BIH-RS-PRES-BYELECTION-CONFIRMED")
    parser.add_argument("--electoral-unit-id", type=int, help="Limit download to one electoral unit; e.g. 7 for Novi Grad")
    parser.add_argument("--delay", type=float, default=0.15, help="Delay between polling-station requests in seconds")
    return parser


if __name__ == "__main__":
    try:
        run(build_parser().parse_args())
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
