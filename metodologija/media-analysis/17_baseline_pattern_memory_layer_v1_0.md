# GFO MEDIA — BASELINE & PATTERN MEMORY LAYER v1.0

**Role:** longitudinal evidence-memory and recurrence-detection support layer  
**Status:** CURRENT — CANDIDATE / FUNCTIONAL / OPTIONAL / NON-ELIMINATORY  
**Scope:** completed GFO Media analyses and published posts  
**Archive path:** `media-baselines/`  
**Case independence:** this specification contains no preloaded case conclusions and creates no retroactive pattern claims.

## 1. Purpose

The layer preserves a compact, evidence-linked baseline for qualifying media analyses so future analyses can test whether a new event is genuinely novel, thematically similar, or part of a documented recurring mechanism.

The archive is analytical memory, not authority. A prior GFO conclusion is never evidence merely because it exists in a baseline.

## 2. Two-pass rule — mandatory

Every new item is processed in this order:

`NEW CONTENT → PRIMARY CANONICAL ANALYSIS → BASELINE RETRIEVAL → PATTERN COMPARISON → SOURCE EVIDENCE RECHECK → PATTERN ASSESSMENT → SYNTHESIS → BASELINE CREATE/UPDATE`

The primary analysis MUST be completed before prior baselines are allowed to influence recurrence assessment.

Previous baselines may inform pattern detection but must not determine the primary assessment of new content.

## 3. Baseline eligibility

Create a baseline for:

1. every completed analysis designated for publication;
2. every published GFO Media post;
3. an unpublished analysis explicitly marked `SIGNIFICANT` because it contains a documented, reusable indicator or unresolved high-value verification question.

Do not create baselines for trivial, duplicate, low-signal or abandoned analyses.

## 4. Baseline is not a copy of the article

A baseline stores compact structured evidence state:

- central claim;
- verified facts;
- unresolved facts;
- key omissions;
- contradictions;
- source provenance;
- institutional/organizational actors;
- relevant dates, amounts, contracts or decisions;
- observable mechanism indicators;
- pattern fingerprint;
- confidence;
- links/references to underlying evidence;
- publication/analysis reference;
- revision history.

Narrative rhetoric and publication prose should be omitted unless necessary to preserve a framing finding.

## 5. Required evidence states

Each material baseline statement must be labeled one of:

- `VERIFIED`
- `SUPPORTED INFERENCE`
- `UNRESOLVED`
- `DISPUTED`
- `SUPERSEDED`

Pattern comparison must privilege `VERIFIED` facts. `SUPPORTED INFERENCE` may guide retrieval but cannot independently establish recurrence.

## 6. Pattern fingerprint

Each baseline may use controlled tags under these fields:

- `mechanism`
- `object`
- `institutional_level`
- `process_stage`
- `recurrence_key`

Examples of generic mechanism vocabulary include:

- omission
- framing
- source_dependency
- formalistic_response
- responsibility_fragmentation
- announcement_without_outcome
- decision_without_execution
- procurement_without_result_trace
- payment_result_gap
- unsupported_causal_claim
- repeated_deadline_shift

Tags describe mechanisms, not culpability or motive.

## 7. Retrieval keys

Future searches should use multiple independent keys where available:

- institution/organization;
- project/program;
- topic;
- location/jurisdiction;
- named contract/procurement identifier;
- relevant company/entity;
- mechanism fingerprint;
- process stage;
- date/time range;
- distinctive factual phrase.

Semantic similarity alone is not enough for a recurring-pattern claim.

## 8. Pattern levels

- `P0 — NO PRIOR PATTERN`: no relevant prior baseline evidence.
- `P1 — THEMATIC SIMILARITY`: related topic/entity but insufficient mechanism recurrence.
- `P2 — REPEATED INDICATOR`: same material indicator appears in at least two distinct documented events.
- `P3 — DOCUMENTED RECURRING PATTERN`: same material mechanism is independently evidenced in at least three distinct events/cases with adequate comparability.
- `P4 — SYSTEMIC PATTERN CANDIDATE`: recurrence spans time, subjects/projects or organizational units and supports a hypothesis of a broader process-level problem; further testing required.
- `P5 — SYSTEMIC PATTERN SUPPORTED`: strong, independently documented recurrence plus evidence supporting a system/process-level explanation rather than mere topical similarity or common administrative noise.

P4/P5 require conservative wording and explicit alternative explanations.

## 9. Evidence recheck rule

No recurring pattern may be asserted solely because previous GFO analyses reached similar conclusions.

Before a prior baseline is counted toward P2–P5, recheck the source evidence supporting the matching mechanism. Record:

- baseline ID;
- matching mechanism;
- underlying evidence reference;
- whether evidence remains accessible;
- whether later evidence superseded it;
- comparability limitation.

If the underlying evidence cannot be rechecked, the baseline may be used for retrieval/navigation but not as confirmed recurrence evidence.

## 10. Anti-confirmation-bias safeguards

1. Do not expose prior pattern labels to the primary analysis pass.
2. Search for disconfirming as well as confirming baselines.
3. Record material differences between cases.
4. Do not count multiple publications of the same originating event as separate recurrence events.
5. Do not count a later update of the same case as a new case unless it represents a distinct event/process decision.
6. Similar outcome does not prove similar cause.
7. Similar mechanism does not prove common intent, coordination or corruption.
8. Absence of a baseline is not evidence that no prior event occurred.

## 11. Baseline lifecycle

Baselines are versioned records. New evidence should update the baseline rather than silently overwrite history.

Required metadata:

- `baseline_version`
- `created_at`
- `last_updated`
- `status`
- `supersedes` where relevant

Permitted status values:

- `ACTIVE`
- `UPDATED`
- `SUPERSEDED`
- `RETRACTED`

Retraction/supersession must preserve an audit note explaining why.

## 12. Required pattern output

When baseline search is relevant, return:

- `BASELINE SEARCH: performed / unavailable / not applicable`
- `MATCHED BASELINES: n`
- `EVIDENCE-RECHECKED MATCHES: n`
- `PATTERN LEVEL: P0–P5`
- `MATCHING MECHANISM`
- `MATERIAL DIFFERENCES`
- `ALTERNATIVE EXPLANATIONS`
- `CONFIDENCE: LOW/MEDIUM/HIGH`
- `PUBLICATION-SAFE WORDING`

If no evidence-supported recurrence exists, explicitly say so.

## 13. Relationship to Narrative Selection & Omission Layer

The Baseline layer supplies longitudinal evidence for `SVD — Systemic Visibility Deficit` and may support recurrence analysis for ORS/FDS/PDS/APD/SIS findings. It does not modify those metric definitions or canonical prompt scores.

## 14. Maintenance record

### v1.0
- Introduced two-pass primary-analysis-before-memory rule.
- Introduced evidence-linked baseline archive.
- Introduced P0–P5 recurrence scale.
- Added source evidence recheck and anti-confirmation-bias safeguards.
- Specification deliberately independent of all previously analyzed cases.
