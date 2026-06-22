#!/usr/bin/env python3
"""Procjena indikatora za dodatnu provjeru PDF metapodataka iz CSV izvjestaja."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

PRIVATE_HINTS = ["privat", "gmail", "outlook", "hotmail", "desktop", "pc", "laptop"]
PUBLIC_HINTS = ["grad", "opstina", "opstina", "ministar", "vlada", "uprava", "odjeljenje", "inspektorat"]


def score_row(row: dict[str, str]) -> tuple[str, str]:
    author = (row.get("author") or "").lower()
    creator = (row.get("creator") or "").lower()
    producer = (row.get("producer") or "").lower()
    status = (row.get("status") or "").lower()

    reasons: list[str] = []
    level = "low"

    if status == "no_metadata":
        return "medium", "Dokument nema sacuvane metapodatke ili su metapodaci uklonjeni."
    if status == "error":
        return "medium", f"Greska pri obradi: {row.get('error', '')}"

    if any(hint in author for hint in PRIVATE_HINTS):
        level = "high"
        reasons.append("Autor metapodataka sadrzi neinstitucionalni trag.")

    if author and not any(hint in author for hint in PUBLIC_HINTS) and any(hint in creator or hint in producer for hint in ["word", "office", "libreoffice"]):
        if level == "low":
            level = "medium"
        reasons.append("Autor nije jasno povezan sa institucijom; potrebna je rucna provjera.")

    if not author and not creator and not producer:
        level = "medium"
        reasons.append("Nedostaju kljucni metapodaci.")

    if not reasons:
        reasons.append("Nema ociglednih metapodatkovnih indikatora za dodatnu provjeru.")

    return level, " ".join(reasons)


def main() -> int:
    parser = argparse.ArgumentParser(description="Dodaj ocjenu indikatora u CSV izvjestaj PDF metapodataka.")
    parser.add_argument("input_csv", help="CSV iz pdf_batch_metadata.py")
    parser.add_argument("--output", default="metadata_risk_report.csv")
    args = parser.parse_args()

    with Path(args.input_csv).open("r", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        print("Ulazni CSV je prazan.")
        return 1

    output_fields = list(rows[0].keys()) + ["indicator_level", "indicator_reason"]
    with Path(args.output).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields)
        writer.writeheader()
        for row in rows:
            level, reason = score_row(row)
            row["indicator_level"] = level
            row["indicator_reason"] = reason
            writer.writerow(row)

    print(f"Kreiran izvjestaj: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
