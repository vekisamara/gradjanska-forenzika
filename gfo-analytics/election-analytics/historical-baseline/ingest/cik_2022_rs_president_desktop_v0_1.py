#!/usr/bin/env python3
"""Desktop-only wrapper for CIK 2022 RS President confirmed results.

Place this file in the same directory as cik_ingestor_v0_2_1.py.
It reuses the validated v0.2.1 engine without requiring the repository folder structure.

Confirmed CIK configuration:
- electionResultId: 32
- dbName: WebResult_2022GENP1_2022_4_20_14_10_43
- race code: 5 (President RS)
- languageId: 3

The internal 2022 raceId is intentionally left null until independently confirmed.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
ENGINE_PATH = SCRIPT_DIR / "cik_ingestor_v0_2_1.py"

DB_NAME = "WebResult_2022GENP1_2022_4_20_14_10_43"
ELECTION_RESULT_ID = 32
ELECTION_ID = "2022-BIH-RS-PRES-GENERAL-CONFIRMED"
RACE_CODE = "5"
LANGUAGE_ID = 3


def load_engine():
    if not ENGINE_PATH.exists():
        raise SystemExit(
            f"Missing {ENGINE_PATH.name}. Put this wrapper in the same folder as cik_ingestor_v0_2_1.py."
        )
    module_name = "gfo_cik_ingestor_v021"
    spec = importlib.util.spec_from_file_location(module_name, ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot load {ENGINE_PATH}")
    module = importlib.util.module_from_spec(spec)
    # Python 3.13 dataclasses expect the module to exist in sys.modules
    # while class decorators are being evaluated during exec_module().
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise
    return module


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

    # Prevent the 2025/26 hard-coded race metadata from leaking into the 2022 manifest.
    engine.DEFAULT_RACE_ID = None
    engine.DEFAULT_RACE_CODE = RACE_CODE

    args = argparse.Namespace(
        output=cli.output,
        election_result_id=ELECTION_RESULT_ID,
        db_name=DB_NAME,
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
    print(f"2022 historical snapshot complete: {snapshot}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
