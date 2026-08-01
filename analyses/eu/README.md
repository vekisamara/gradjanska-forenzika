---
skip_file: true
---

# European Union Analyses

This directory contains English-language Civic Forensics analyses concerning:

- EU institutions, bodies, offices and agencies;
- EU Member States;
- candidate and potential candidate countries;
- EU-funded programmes, projects and procurement;
- implementation of EU law by national and local authorities;
- public administration reform, rule of law and democratic governance;
- access to documents, open data and public participation;
- digital rights, automated decision-making and public-sector AI;
- public spending, performance indicators and quantitative formalism.

## WordPress publication boundary

Only Markdown files inside [`published/`](published/) are intended for automatic import into WordPress.

Configure Git it Write to use:

```text
analyses/eu/published
```

Repository instructions, templates, research notes, drafts, evidence registers and supporting files must remain outside that folder. No `README.md` or internal index should be placed inside `published/`.

## Published analyses

- [When an AI Label Becomes Another Cookie Banner](published/2026-ai-transparency-labels.md) — analysis of Article 50 AI Act transparency obligations, user comprehension and the risk of label-based quantitative formalism.
- [Portugal's First Lobbying Law: Transparency or Self-Supervision?](published/2026-portugal-lobbying-law.md) — institutional test of register coverage, verification, oversight independence and enforcement.
- [When an EU Agency Recovers an Entire Grant: What Must the File Show?](published/2026-cinea-grant-recovery.md) — analysis of CINEA grant termination and full recovery through procedural fairness, proportionality and financial-control evidence.
- [When the Complaints Mechanism Is Also Under Review: The Poklečani Wind Farm Case](published/2026-poklecani-eib-complaints-mechanism.md) — open-inquiry analysis of EIB environmental accountability and the evidence expected from an internal complaints mechanism.
- [Strategic Project, Restricted Document: How the Jadar File Became Partly Public](published/2026-jadar-access-to-documents.md) — analysis of access to documents, international-relations exceptions and delayed confirmatory review.
- [When a Consultation Is Called a Reality Check: Does the Label Remove the Transparency Duty?](published/2026-reality-checks-transparency.md) — open-inquiry analysis of stakeholder selection, lobbying transparency and regulatory simplification.
- [From Duty to Encouragement: What Does the AI Omnibus Mean for AI Literacy?](published/2026-ai-omnibus-ai-literacy.md) — analysis of the accountability shift from organisational duty to public-policy promotion.
- [AI Will Simplify Bureaucracy — But What Evidence Would Prove It?](published/2026-genai-public-administration-pilots.md) — prospective evidence framework for evaluating generative AI pilots in public administration.
- [Accepted but Not Fully Adequate: What Does Compliance Mean in the X Action Plan?](published/2026-x-dsa-action-plan.md) — analysis of the distinction between an accepted remediation plan and demonstrated DSA compliance.

## Current structure

```text
analyses/eu/
├── README.md
└── published/
    ├── 2026-ai-transparency-labels.md
    ├── 2026-portugal-lobbying-law.md
    ├── 2026-cinea-grant-recovery.md
    ├── 2026-poklecani-eib-complaints-mechanism.md
    ├── 2026-jadar-access-to-documents.md
    ├── 2026-reality-checks-transparency.md
    ├── 2026-ai-omnibus-ai-literacy.md
    ├── 2026-genai-public-administration-pilots.md
    └── 2026-x-dsa-action-plan.md
```

Additional working directories may be added outside `published/`, preferably with an underscore prefix:

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

Every analysis must state:

1. the authority and jurisdiction concerned;
2. whether the matter concerns an EU institution, a Member State authority or an accession country;
3. whether EU law is directly applicable, implemented through national law or used only as a methodological reference;
4. the applicable national or institutional procedural framework;
5. the available remedy or oversight route, if established.

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

Use the templates in [`../templates/`](../templates/README.md) when opening a new analysis. Move only reviewed or final publication files into `published/`.
