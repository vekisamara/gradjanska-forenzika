#!/usr/bin/env python3
"""GFO Historical Baseline — CIK 2022 RS President ingest wrapper v0.1

Uses the validated CIK Race5 snapshot engine from Election Data Standard v0.2.1
with the confirmed configuration for the 2022 General Election confirmed results.

Confirmed from CIK frontend/API inspection:
- electionResultId / resId: 32
- dbName: WebResult_2022GENP1_2022_4_20_14_10_43
- race code: 5 (Predsjednik RS)
- Race5 endpoint family confirmed

The 2022 internal raceId is intentionally left null until independently confirmed.
It is not required by Race5 acquisition endpoints.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ENGINE_RELATIVE = Path(__file__).resolve().parents[3] / "election-data-standard" / "ingest" / "cik_ingestor_v0_2_1.py"


def load_engine():
    spec = importlib.util.spec_from_file_location("gfo_cik_engine_v021", ENGINE_RELATIVE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load engine: {ENGINE_RELATIVE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="CIK 2022 confirmed RS President historical snapshot ingest")
    p.add_argument("--output", default="./cik-2022-rs-president")
    p.add_argument("--electoral-unit-id", type=int)
    p.add_argument("--workers", type=int, default=6)
    p.add_argument("--retries", type=int, default=3)
    p.add_argument("--backoff", type=float, default=1.0)
    p.add_argument("--jitter", type=float, default=0.25)
    p.add_argument("--timeout", type=int, default=30)
    return p


def main() -> None:
    a = build_parser().parse_args()
    engine = load_engine()

    # Prevent the 2025/26 default raceId from being written into a 2022 manifest.
    engine.DEFAULT_RACE_ID = None
    engine.DEFAULT_RACE_CODE = "5"

    args = argparse.Namespace(
        output=a.output,
        election_result_id=32,
        db_name="WebResult_2022GENP1_2022_4_20_14_10_43",
        language_id=3,
        election_id="2022-BIH-RS-PRES-GENERAL-CONFIRMED",
        electoral_unit_id=a.electoral_unit_id,
        workers=a.workers,
        retries=a.retries,
        backoff=a.backoff,
        jitter=a.jitter,
        timeout=a.timeout,
        watch=False,
        interval=1800,
    )
    snapshot = engine.run_once(args)
    print(f"Historical source snapshot ready: {snapshot}")
    print("Note: manifest race_id is intentionally null pending independent confirmation.")


if __name__ == "__main__":
    main()
