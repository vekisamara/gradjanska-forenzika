# GFO MEDIA — NARRATIVE SELECTION & OMISSION LAYER v1.0

**Role:** optional cross-prompt analytical enrichment module  
**Status:** CURRENT — CANDIDATE / FUNCTIONAL / OPTIONAL / NON-ELIMINATORY  
**Scope:** public statements, media content, institutional PR and electoral communication  
**Authority:** subordinate to GFO Media Project Control, Runtime and canonical prompts 10–13  
**Case independence:** this specification contains no case-specific facts, actors, institutions or conclusions.

## 1. Purpose

This layer tests whether a communication may create a materially incomplete or distorted overall impression through selection, omission, framing, source dependence or loss of systemic context even when individual stated facts are not shown to be false.

It supplements, never replaces, canonical analysis.

## 2. Mandatory safeguards

1. Omission is not evidence of intent by itself.
2. Ownership, financing, political proximity or institutional affiliation do not prove manipulation of a concrete item.
3. Multiple reproductions of one originating source are not independent confirmations.
4. Missing information is not concealment unless evidence supports that inference.
5. Scores describe observable properties of content/evidence structure, not motives or character of authors.
6. A missing fact must be material to the central claim before it may affect an omission assessment.
7. All material findings require an evidence reference and confidence level.
8. Canonical scores must not be averaged, overwritten or recalculated using this layer.

## 3. Novelty / Utility Gate

Run only after the canonical claim/evidence spine exists. Return `NOT APPLICABLE` when the layer would merely restate a canonical finding. Return `PARTIAL` when only some checks add material value.

## 4. Assessments

### A. Omission Risk Score — ORS (0–4)

Measures whether identified missing context materially changes interpretation of the central claim.

- 0 — no material omission identified.
- 1 — secondary context missing; central meaning substantially unchanged.
- 2 — relevant omission capable of changing assessment.
- 3 — serious omission; stated facts may be accurate but the resulting overall picture is materially different without the missing context.
- 4 — communication effect substantially depends on omission of identified key context.

A score above 0 requires identification of the concrete missing fact, document, comparison or context and an explanation of materiality.

### B. Framing Distortion Score — FDS (0–4)

Measures divergence between evidentiary support and the interpretive frame created by headline, ordering, labels, adjectives, causal wording, certainty or emphasis.

- 0 — frame proportionate to evidence.
- 1 — minor promotional/negative emphasis.
- 2 — noticeable selective framing.
- 3 — framing materially changes likely interpretation of the evidence.
- 4 — evidence is primarily organized to sustain a predetermined narrative beyond what it independently supports.

### C. Source Independence Score — SIS (0–4)

Measures independence of evidence chains. Higher is stronger.

- 0 — one originating source; reproductions only.
- 1 — multiple distributors without independent verification.
- 2 — partial independent corroboration.
- 3 — multiple genuinely independent sources.
- 4 — multiple independent sources plus inspectable primary documentary/data evidence.

Always distinguish `publication_count` from `independent_evidence_chains`.

### D. PR Dependency Score — PDS (0–4)

Measures dependence of a media item on pre-packaged communication from an interested actor.

- 0 — independently developed reporting.
- 1 — PR/official material is one of several independently developed sources.
- 2 — PR/official material is the main source but material independent checking is added.
- 3 — near-complete reproduction of the originating narrative with little independent verification.
- 4 — communication substantially functions as republished PR while presented as independent reporting.

### E. Alternative Perspective Deficit — APD (0–4)

Measures absence of materially relevant perspectives or evidence, not absence of arbitrary political balance.

Relevant alternatives may include primary documents, affected users, contracts, audit findings, technical records, financial realization, independent expertise or other evidence capable of testing the central claim.

- 0 — key relevant perspectives/evidence represented.
- 1 — minor deficit.
- 2 — one important perspective/evidence class missing.
- 3 — most relevant independent perspectives/evidence missing.
- 4 — content is almost entirely confined to the perspective of an interested actor.

### F. Systemic Visibility Deficit — SVD (0–4)

Measures whether an event is presented as isolated when documented prior evidence may show recurrence or a broader mechanism.

- 0 — no supported broader pattern.
- 1 — possible relationship requiring verification.
- 2 — multiple comparable documented events exist.
- 3 — a documented recurring mechanism exists across distinct cases.
- 4 — the item materially suppresses or contradicts a well-supported recurring/systemic context relevant to its central claim.

SVD must use the Baseline & Pattern Memory Layer when available. Prior conclusions alone are insufficient; underlying evidence must be rechecked before a recurring-pattern claim enters synthesis.

## 5. Claim classification

Where useful, distinguish:

- `FALSE CLAIM` — evidence supports that the claim is false.
- `UNSUPPORTED CLAIM` — available evidence does not adequately support the claim.
- `FRAMED CLAIM` — underlying fact may be supported but framing exceeds or redirects its evidentiary meaning.
- `OMISSION-DRIVEN CLAIM` — underlying stated facts may be supported but identified missing material context changes the overall impression.

Do not use `FALSE CLAIM` merely because ORS/FDS/APD/PDS is high.

## 6. Required output

Return module status: `USED`, `PARTIAL`, `NOT APPLICABLE`, `INSUFFICIENT EVIDENCE`, or `UNAVAILABLE`.

For each used metric report:

| Metric | Score | Evidence | Materiality | Confidence |
|---|---:|---|---|---|
| ORS | 0–4 | ... | ... | LOW/MEDIUM/HIGH |
| FDS | 0–4 | ... | ... | ... |
| SIS | 0–4 | ... | ... | ... |
| PDS | 0–4 | ... | ... | ... |
| APD | 0–4 | ... | ... | ... |
| SVD | 0–4 | ... | ... | ... |

Then state:

- `CENTRAL FINDING`
- `PRIMARY OMISSION` if supported
- `PUBLICATION COUNT`
- `INDEPENDENT EVIDENCE CHAINS`
- `ALTERNATIVE FRAME / RECONSTRUCTION`
- `EVIDENCE NEEDED TO CONFIRM OR REFUTE`
- `UTILITY ADDED`

## 7. Relationship to other layers

This layer is additive and non-eliminatory. It may be invoked by canonical public-statement, electoral, media-manipulation and institutional-PR prompts after their primary analysis. It may also call the Baseline & Pattern Memory Layer for SVD and recurrence testing.

No finding from this layer may silently change a canonical scoring/routing rule.

## 8. Maintenance record

### v1.0
- Introduced ORS, FDS, SIS, PDS, APD and SVD.
- Added publication-count vs independent-evidence-chain distinction.
- Added false/unsupported/framed/omission-driven claim classification.
- Added mandatory intent, provenance, materiality and confidence safeguards.
- Specification deliberately case-independent.
