#!/usr/bin/env python3
"""Kalkulator rokova za FOI zahtjeve, predstavke, inicijative i urgencije."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, datetime, timedelta

DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%Y."]


@dataclass
class DeadlineResult:
    datum_podnosenja: date
    rok_dana: int
    datum_isteka: date
    danas: date
    status: str
    kasnjenje_dana: int
    preostalo_dana: int


def parse_date(value: str) -> date:
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise argparse.ArgumentTypeError("Datum mora biti YYYY-MM-DD ili DD.MM.YYYY.")


def calculate(start: date, days: int, today: date | None = None) -> DeadlineResult:
    today = today or date.today()
    deadline = start + timedelta(days=days)
    delta = (today - deadline).days
    if delta > 0:
        status = "ROK PROBIJEN"
        late = delta
        remaining = 0
    elif delta == 0:
        status = "ROK ISTIČE DANAS"
        late = 0
        remaining = 0
    else:
        status = "U ROKU"
        late = 0
        remaining = abs(delta)
    return DeadlineResult(start, days, deadline, today, status, late, remaining)


def fmt(d: date) -> str:
    return d.strftime("%d.%m.%Y.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Izračun isteka rokova u građanskoj forenzici.")
    parser.add_argument("--datum", required=True, type=parse_date, help="Datum podnošenja: YYYY-MM-DD ili DD.MM.YYYY.")
    parser.add_argument("--rok", required=True, type=int, help="Rok u kalendarskim danima")
    parser.add_argument("--danas", type=parse_date, help="Opcioni kontrolni datum")
    args = parser.parse_args()

    result = calculate(args.datum, args.rok, args.danas)
    print(f"Datum podnošenja: {fmt(result.datum_podnosenja)}")
    print(f"Rok: {result.rok_dana} dana")
    print(f"Datum isteka: {fmt(result.datum_isteka)}")
    print(f"Danas: {fmt(result.danas)}")
    print(f"Status: {result.status}")
    if result.kasnjenje_dana:
        print(f"Kašnjenje: {result.kasnjenje_dana} dana")
    else:
        print(f"Preostalo: {result.preostalo_dana} dana")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
