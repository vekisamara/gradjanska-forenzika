#!/usr/bin/env python3
"""Evidencioni dnevnik dokaza za predmete građanske forenzike.

Čuva lokalni CSV registar dokumenata, hash vrijednosti, izvore i napomene.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import datetime
from pathlib import Path

FIELDNAMES = [
    "case_id",
    "document_name",
    "file_path",
    "institution",
    "document_number",
    "document_date",
    "source",
    "sha256",
    "note",
    "created_at",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_csv(path: Path) -> None:
    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDNAMES).writeheader()


def add_record(args: argparse.Namespace) -> None:
    db = Path(args.db)
    ensure_csv(db)
    file_path = Path(args.file) if args.file else None
    sha = sha256_file(file_path) if file_path and file_path.exists() else args.sha256 or ""
    document_name = args.document_name or (file_path.name if file_path else "")
    record = {
        "case_id": args.case_id,
        "document_name": document_name,
        "file_path": str(file_path.resolve()) if file_path and file_path.exists() else (args.file or ""),
        "institution": args.institution or "",
        "document_number": args.document_number or "",
        "document_date": args.document_date or "",
        "source": args.source or "",
        "sha256": sha,
        "note": args.note or "",
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    with db.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDNAMES).writerow(record)
    print(f"Dodan dokaz: {record['document_name']}")


def list_records(args: argparse.Namespace) -> None:
    db = Path(args.db)
    if not db.exists():
        print("Dnevnik ne postoji.")
        return
    with db.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if args.case_id and row.get("case_id") != args.case_id:
                continue
            print(f"[{row.get('case_id')}] {row.get('document_date')} | {row.get('institution')} | {row.get('document_name')} | {row.get('document_number')}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lokalni evidencioni dnevnik dokaza.")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Dodaj dokaz u dnevnik")
    add.add_argument("--db", default="evidencija_dokaza.csv")
    add.add_argument("--case-id", required=True)
    add.add_argument("--file")
    add.add_argument("--document-name")
    add.add_argument("--institution")
    add.add_argument("--document-number")
    add.add_argument("--document-date")
    add.add_argument("--source")
    add.add_argument("--sha256")
    add.add_argument("--note")
    add.set_defaults(func=add_record)

    ls = sub.add_parser("list", help="Prikaži evidenciju")
    ls.add_argument("--db", default="evidencija_dokaza.csv")
    ls.add_argument("--case-id")
    ls.set_defaults(func=list_records)

    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
