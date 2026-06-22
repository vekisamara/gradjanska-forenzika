#!/usr/bin/env python3
"""Lokalni tracker FOI zahtjeva, rokova i statusa."""

from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path
from uuid import uuid4

FIELDNAMES = ["id", "datum_slanja", "organ", "predmet", "rok_dana", "datum_isteka", "status", "napomena"]
DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%Y."]


def parse_date(value: str) -> date:
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise argparse.ArgumentTypeError("Datum mora biti YYYY-MM-DD ili DD.MM.YYYY.")


def fmt(d: date) -> str:
    return d.strftime("%Y-%m-%d")


def ensure_csv(path: Path) -> None:
    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDNAMES).writeheader()


def read_rows(path: Path) -> list[dict[str, str]]:
    ensure_csv(path)
    with path.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def add(args: argparse.Namespace) -> None:
    db = Path(args.db)
    ensure_csv(db)
    deadline = args.datum + timedelta(days=args.rok)
    row = {
        "id": args.id or str(uuid4())[:8],
        "datum_slanja": fmt(args.datum),
        "organ": args.organ,
        "predmet": args.predmet,
        "rok_dana": str(args.rok),
        "datum_isteka": fmt(deadline),
        "status": args.status,
        "napomena": args.napomena or "",
    }
    rows = read_rows(db)
    rows.append(row)
    write_rows(db, rows)
    print(f"Dodan FOI zahtjev: {row['id']} | rok ističe {row['datum_isteka']}")


def status(args: argparse.Namespace) -> None:
    today = args.danas or date.today()
    rows = read_rows(Path(args.db))
    if not rows:
        print("Nema evidentiranih FOI zahtjeva.")
        return
    for row in rows:
        deadline = parse_date(row["datum_isteka"])
        delta = (today - deadline).days
        if row["status"].lower() in {"odgovoreno", "zatvoreno"}:
            state = row["status"]
        elif delta > 0:
            state = f"ROK PROBIJEN ({delta} dana)"
        elif delta == 0:
            state = "ROK ISTIČE DANAS"
        else:
            state = f"U ROKU ({abs(delta)} dana preostalo)"
        print(f"{row['id']} | {row['organ']} | {row['predmet']} | {row['datum_isteka']} | {state}")


def update(args: argparse.Namespace) -> None:
    db = Path(args.db)
    rows = read_rows(db)
    changed = False
    for row in rows:
        if row["id"] == args.id:
            row["status"] = args.status
            if args.napomena:
                row["napomena"] = args.napomena
            changed = True
    write_rows(db, rows)
    print("Status ažuriran." if changed else "ID nije pronađen.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Tracker FOI zahtjeva i rokova.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add")
    p_add.add_argument("--db", default="foi_tracker.csv")
    p_add.add_argument("--id")
    p_add.add_argument("--datum", required=True, type=parse_date)
    p_add.add_argument("--organ", required=True)
    p_add.add_argument("--predmet", required=True)
    p_add.add_argument("--rok", type=int, default=15)
    p_add.add_argument("--status", default="poslato")
    p_add.add_argument("--napomena")
    p_add.set_defaults(func=add)

    p_status = sub.add_parser("status")
    p_status.add_argument("--db", default="foi_tracker.csv")
    p_status.add_argument("--danas", type=parse_date)
    p_status.set_defaults(func=status)

    p_update = sub.add_parser("update")
    p_update.add_argument("--db", default="foi_tracker.csv")
    p_update.add_argument("--id", required=True)
    p_update.add_argument("--status", required=True)
    p_update.add_argument("--napomena")
    p_update.set_defaults(func=update)

    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
