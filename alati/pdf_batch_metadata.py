#!/usr/bin/env python3
"""Batch ekstrakcija PDF metapodataka za folder dokaza."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit("Nedostaje biblioteka pypdf. Instalacija: pip install pypdf") from exc


@dataclass
class PdfMetadataRecord:
    filename: str
    path: str
    pages: int | None
    title: str | None
    author: str | None
    subject: str | None
    creator: str | None
    producer: str | None
    creation_date: str | None
    modification_date: str | None
    sha256: str
    status: str
    error: str | None = None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def clean(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.isoformat(timespec="seconds")
    return str(value)


def inspect_pdf(path: Path) -> PdfMetadataRecord:
    try:
        reader = PdfReader(str(path))
        meta = reader.metadata
        if not meta:
            return PdfMetadataRecord(path.name, str(path.resolve()), len(reader.pages), None, None, None, None, None, None, None, sha256_file(path), "NO_METADATA")
        return PdfMetadataRecord(
            filename=path.name,
            path=str(path.resolve()),
            pages=len(reader.pages),
            title=clean(meta.title),
            author=clean(meta.author),
            subject=clean(meta.subject),
            creator=clean(meta.creator),
            producer=clean(meta.producer),
            creation_date=clean(meta.creation_date),
            modification_date=clean(meta.modification_date),
            sha256=sha256_file(path),
            status="OK",
        )
    except Exception as exc:
        return PdfMetadataRecord(path.name, str(path.resolve()), None, None, None, None, None, None, None, None, sha256_file(path), "ERROR", str(exc))


def find_pdfs(folder: Path, recursive: bool) -> list[Path]:
    pattern = "**/*.pdf" if recursive else "*.pdf"
    return sorted(folder.glob(pattern))


def write_csv(records: list[PdfMetadataRecord], output: Path) -> None:
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(records[0]).keys()))
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))


def write_json(records: list[PdfMetadataRecord], output: Path) -> None:
    output.write_text(json.dumps([asdict(r) for r in records], ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch izvlačenje PDF metapodataka.")
    parser.add_argument("folder", help="Folder sa PDF dokumentima")
    parser.add_argument("--recursive", action="store_true", help="Pretraži i podfoldere")
    parser.add_argument("--csv", default="pdf_metadata_report.csv", help="CSV izlaz")
    parser.add_argument("--json", help="Opcioni JSON izlaz")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists() or not folder.is_dir():
        print("Greška: folder ne postoji.")
        return 1

    records = [inspect_pdf(path) for path in find_pdfs(folder, args.recursive)]
    if not records:
        print("Nema PDF fajlova za obradu.")
        return 1

    write_csv(records, Path(args.csv))
    if args.json:
        write_json(records, Path(args.json))

    print(f"Obrađeno PDF dokumenata: {len(records)}")
    print(f"CSV izvještaj: {args.csv}")
    if args.json:
        print(f"JSON izvještaj: {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
