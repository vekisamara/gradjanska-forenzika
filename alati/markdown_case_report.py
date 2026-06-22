#!/usr/bin/env python3
"""Generator Markdown studije slucaja iz case.json i opcione CSV evidencije."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_csv(path: Path | None) -> list[dict[str, str]]:
    if not path:
        return []
    with path.open("r", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_report(case_data: dict, evidence_rows: list[dict[str, str]]) -> str:
    title = case_data.get("case_title") or case_data.get("case_id") or "Studija slucaja"
    lines = [f"# {title}", ""]
    lines.append("## Kratak opis")
    lines.append(case_data.get("summary") or "[Dodati kratak opis predmeta.]")
    lines.append("")

    lines.append("## Osnovni podaci")
    lines.append(f"- ID predmeta: `{case_data.get('case_id', '')}`")
    lines.append(f"- Institucija: {case_data.get('institution', '')}")
    lines.append(f"- Tip problema: {case_data.get('issue_type', '')}")
    lines.append(f"- Javni interes: {case_data.get('public_interest', '')}")
    lines.append(f"- Procjena rizika: {case_data.get('risk_level', '')}")
    lines.append("")

    lines.append("## Ključni dokumenti")
    if evidence_rows:
        for row in evidence_rows:
            name = row.get("document_name") or row.get("filename") or row.get("predmet") or "Dokument"
            inst = row.get("institution") or row.get("organ") or ""
            num = row.get("document_number") or row.get("id") or ""
            date = row.get("document_date") or row.get("date") or row.get("datum_slanja") or ""
            lines.append(f"- {date} — {name} ({inst}; {num})")
    else:
        lines.append("[Dodati listu dokumenata i dokazni trag.]")
    lines.append("")

    lines.append("## Hronologija")
    timeline = case_data.get("timeline") or []
    if timeline:
        for item in timeline:
            lines.append(f"- {item}")
    else:
        lines.append("[Dodati hronologiju ili generisati pomocu timeline_builder.py.]")
    lines.append("")

    lines.append("## Uočene anomalije")
    findings = case_data.get("findings") or []
    if findings:
        for item in findings:
            lines.append(f"- {item}")
    else:
        lines.append("[Dodati nalaze: formalizam, cutanje uprave, kontradikcije, metapodaci, ignorisani dokazi.]")
    lines.append("")

    lines.append("## Preporučeni naredni korak")
    lines.append(case_data.get("recommended_action") or "[Dodati preporuku: FOI, urgencija, zalba, prijava nadzoru, javna analiza.]")
    lines.append("")

    lines.append("## Napomena o privatnosti")
    lines.append(case_data.get("privacy_note") or "Prije objave ukloniti osjetljive licne podatke koji nisu nuzni za javni interes.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Napravi Markdown izvjestaj iz case.json.")
    parser.add_argument("case_json")
    parser.add_argument("--evidence-csv")
    parser.add_argument("--output", default="case_report.md")
    args = parser.parse_args()

    case_data = json.loads(Path(args.case_json).read_text(encoding="utf-8"))
    evidence = load_csv(Path(args.evidence_csv) if args.evidence_csv else None)
    report = build_report(case_data, evidence)
    Path(args.output).write_text(report, encoding="utf-8")
    print(f"Kreiran izvjestaj: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
