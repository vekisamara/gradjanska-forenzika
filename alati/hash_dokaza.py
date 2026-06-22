#!/usr/bin/env python3
"""Lokalni generator SHA-256 hash vrijednosti za dokazne fajlove.

Alat ne mijenja ulazni fajl. Koristi se za dokazivanje integriteta
dokumenata u predmetima građanske forenzike.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

CHUNK_SIZE = 1024 * 1024


@dataclass
class HashRecord:
    path: str
    filename: str
    size_bytes: int
    sha256: str
    processed_at: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(targets: Iterable[Path], recursive: bool = False) -> Iterable[Path]:
    for target in targets:
        if target.is_file():
            yield target
        elif target.is_dir():
            pattern = "**/*" if recursive else "*"
            for item in target.glob(pattern):
                if item.is_file():
                    yield item
        else:
            print(f"Upozorenje: putanja ne postoji: {target}")


def build_record(path: Path) -> HashRecord:
    return HashRecord(
        path=str(path.resolve()),
        filename=path.name,
        size_bytes=path.stat().st_size,
        sha256=sha256_file(path),
        processed_at=datetime.now().isoformat(timespec="seconds"),
    )


def write_json(records: list[HashRecord], output: Path) -> None:
    output.write_text(json.dumps([asdict(r) for r in records], ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(records: list[HashRecord], output: Path) -> None:
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(records[0]).keys()))
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))


def main() -> int:
    parser = argparse.ArgumentParser(description="Izračun SHA-256 hash vrijednosti za dokazne fajlove.")
    parser.add_argument("paths", nargs="+", help="Fajlovi ili folderi za obradu")
    parser.add_argument("--recursive", action="store_true", help="Rekurzivno obradi podfoldere")
    parser.add_argument("--json", dest="json_out", help="Snimi rezultat u JSON fajl")
    parser.add_argument("--csv", dest="csv_out", help="Snimi rezultat u CSV fajl")
    args = parser.parse_args()

    records = [build_record(path) for path in iter_files([Path(p) for p in args.paths], args.recursive)]
    if not records:
        print("Nema fajlova za obradu.")
        return 1

    for record in records:
        print(f"Fajl: {record.filename}")
        print(f"Putanja: {record.path}")
        print(f"Veličina: {record.size_bytes} bytes")
        print(f"SHA-256: {record.sha256}")
        print(f"Datum obrade: {record.processed_at}")
        print("-" * 60)

    if args.json_out:
        write_json(records, Path(args.json_out))
    if args.csv_out:
        write_csv(records, Path(args.csv_out))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
