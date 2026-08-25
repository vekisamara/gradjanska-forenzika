#!/usr/bin/env python3
"""Desktop-only wrapper for CIK 2022 RS President confirmed results.

Place this file in the same directory as cik_ingestor_v0_2_1.py.
It reuses the validated v0.2.1 engine without requiring the repository folder structure.

Confirmed CIK configuration:
- electionResultId: 32
- dbName (canonical): WebResult_2022GENP1_2022_4_20_14_10_43
- API dbName path parameter: %22WebResult_2022GENP1_2022_4_20_14_10_43%22
- raceId: 73
- race code: 5 (President RS)
- languageId: 3
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENGINE_PATH = SCRIPT_DIR / "cik_ingestor_v0_2_1.py"

DB_NAME_CANONICAL = "WebResult_2022GENP1_2022_4_20_14_10_43"
DB_NAME_API = "%22WebResult_2022GENP1_2022_4_20_14_10_43%22"
ELECTION_RESULT_ID = 32
ELECTION_ID = "2022-BIH-RS-PRES-GENERAL-CONFIRMED"
RACE_ID = 73
RACE_CODE = "5"
LANGUAGE_ID = 3


def load_engine():
    if not ENGINE_PATH.exists():
        raise SystemExit(
            f"Missing {ENGINE_PATH.name}. Put this wrapper in the same folder as cik_ingestor_v0_2_1.py."
        )
    try:
        import cik_ingestor_v0_2_1 as engine
    except Exception as exc:
        raise SystemExit(f"Cannot import {ENGINE_PATH.name}: {exc}") from exc
    return engine


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="CIK 2022 President RS confirmed-results snapshot ingest")
    p.add_argument("--output", default="./cik-2022-rs-president")
    p.add_argument("--workers", type=int, default=6)
    p.add_argument("--retries", type=int, default=3)
    p.add_argument("--backoff", type=float, default=1.0)
    p.add_argument("--jitter", type=float, default=0.25)
    p.add_argument("--timeout", type=int, default=30)
    p.add_argument("--electoral-unit-id", type=int)
    return p


def main() -> int:
    cli = build_parser().parse_args()
    if cli.workers < 1:
        raise SystemExit("--workers must be >= 1")

    engine = load_engine()
    engine.DEFAULT_RACE_ID = RACE_ID
    engine.DEFAULT_RACE_CODE = RACE_CODE

    args = argparse.Namespace(
        output=cli.output,
        election_result_id=ELECTION_RESULT_ID,
        db_name=DB_NAME_API,
        language_id=LANGUAGE_ID,
        election_id=ELECTION_ID,
        electoral_unit_id=cli.electoral_unit_id,
        workers=cli.workers,
        retries=cli.retries,
        backoff=cli.backoff,
        jitter=cli.jitter,
        timeout=cli.timeout,
        watch=False,
        interval=1800,
    )

    snapshot = engine.run_once(args)

    # Keep manifest metadata canonical while retaining the exact API parameter used.
    manifest_path = snapshot / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["db_name"] = DB_NAME_CANONICAL
        manifest["api_db_name_parameter"] = DB_NAME_API
        manifest["race_id"] = RACE_ID
        manifest["race_code"] = RACE_CODE
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"2022 historical snapshot complete: {snapshot}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
