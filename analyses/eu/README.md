---
skip_file: true
---

# European Union Analyses

This directory contains the organisational index and publication guidance for English-language Civic Forensics analyses concerning EU institutions, Member States, accession countries, EU-funded programmes, public administration, rule of law, access to documents, digital rights, public-sector AI and quantitative formalism.

## WordPress publication boundary

Because Git it Write 2.0 does not reliably process deeper repository paths, all Markdown files intended for automatic WordPress import are stored in the top-level publication folder:

```text
analyses/published
```

Configure Git it Write to use exactly that folder. Repository instructions, templates, research notes, evidence registers and drafts must remain outside it. Do not place a `README.md` or internal index inside `analyses/published`.

## Published analyses

- [When an AI Label Becomes Another Cookie Banner](../published/2026-ai-transparency-labels.md)
- [Portugal's First Lobbying Law: Transparency or Self-Supervision?](../published/2026-portugal-lobbying-law.md)
- [When an EU Agency Recovers an Entire Grant: What Must the File Show?](../published/2026-cinea-grant-recovery.md)
- [When the Complaints Mechanism Is Also Under Review: The Poklečani Wind Farm Case](../published/2026-poklecani-eib-complaints-mechanism.md)
- [Strategic Project, Restricted Document: How the Jadar File Became Partly Public](../published/2026-jadar-access-to-documents.md)
- [When a Consultation Is Called a Reality Check: Does the Label Remove the Transparency Duty?](../published/2026-reality-checks-transparency.md)
- [From Duty to Encouragement: What Does the AI Omnibus Mean for AI Literacy?](../published/2026-ai-omnibus-ai-literacy.md)
- [AI Will Simplify Bureaucracy — But What Evidence Would Prove It?](../published/2026-genai-public-administration-pilots.md)
- [Accepted but Not Fully Adequate: What Does Compliance Mean in the X Action Plan?](../published/2026-x-dsa-action-plan.md)

## Current structure

```text
analyses/
├── published/
│   ├── 2026-ai-transparency-labels.md
│   ├── 2026-portugal-lobbying-law.md
│   ├── 2026-cinea-grant-recovery.md
│   ├── 2026-poklecani-eib-complaints-mechanism.md
│   ├── 2026-jadar-access-to-documents.md
│   ├── 2026-reality-checks-transparency.md
│   ├── 2026-ai-omnibus-ai-literacy.md
│   ├── 2026-genai-public-administration-pilots.md
│   └── 2026-x-dsa-action-plan.md
└── eu/
    └── README.md
```

Additional working directories may be used outside `published/`, preferably with an underscore prefix:

```text
_drafts/
_research/
_evidence/
```

## Publication standard

Each analysis should:

1. identify the authority, jurisdiction and public-interest question;
2. distinguish established facts, legal interpretation, inference and allegation;
3. identify the exact source and its status;
4. include an evidence gap or expected evidence-trace section;
5. consider alternative explanations;
6. distinguish administrative activity from effective protection or real-world outcome;
7. activate the quantitative module where a number, percentage, trend, comparison, ranking or causal claim is material;
8. state limitations and avoid conclusions unsupported by the available record;
9. record the methodology version and review status;
10. preserve the right of reply where an analysis makes a material adverse institutional finding.

## Required jurisdiction note

Every analysis must state the authority and jurisdiction concerned, the relevance of EU or national law, the applicable procedural framework and the available remedy or oversight route where established.

EU standards must not be presented as directly enforceable in a national or accession-country procedure unless the legal basis has been verified.

## Recommended metadata

```yaml
---
title: ""
jurisdiction: "European Union"
country: ""
institution: ""
topic: ""
analysis_type: "institutional | legal | quantitative | statement"
status: "draft | reviewed | final | updated | archived"
date_published: ""
date_updated: ""
methodology_version: "3.2"
language: "English"
source_status: ""
licence: "CC BY-SA 4.0"
categories:
  - "Primary WordPress category"
tags:
  - "Topic tag"
---
```

Move only reviewed or final publication files into `analyses/published`.