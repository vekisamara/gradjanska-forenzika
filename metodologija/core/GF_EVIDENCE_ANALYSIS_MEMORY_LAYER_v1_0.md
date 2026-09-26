# GF — EVIDENCE & ANALYSIS MEMORY LAYER (GF-EAML) v1.0

**Role:** horizontal evidence-memory, continuity and recurrence support standard  
**Status:** CURRENT — CONTROLLED OPERATIONAL  
**Scope:** GF documents, cases, analyses and specialized modules  
**Principle:** memory assists retrieval and comparison; memory is never evidence by itself.

## 1. Purpose

GF-EAML preserves compact, structured and evidence-linked memory records for material GF documents and analyses. Its purpose is to help future work determine whether new material is genuinely new, related to an existing matter, a continuation or update, corroborating or contradicting evidence, a duplicate, a superseding record, or a possible recurrence of a previously documented mechanism.

The layer is horizontal. Specialized modules may define additional fields and rules. The existing GFO Media Baseline & Pattern Memory Layer remains the specialized implementation for media analysis.

## 2. Mandatory two-pass rule

Process new material in this order:

`NEW MATERIAL → PRIMARY ANALYSIS → MEMORY RETRIEVAL → RELATIONSHIP COMPARISON → ORIGINAL EVIDENCE RECHECK → SYNTHESIS → MEMORY CREATE/UPDATE`

Prior memory records MUST NOT determine the primary assessment of new material. They may be consulted only after the new material has first been assessed on its own evidence.

## 3. Three-layer model

### SOURCE
Original document, correspondence, dataset, webpage snapshot or other underlying evidence.

### MEMORY RECORD
Compact structured representation used for retrieval, continuity and comparison. It is not a substitute for SOURCE.

### ANALYSIS / CASE
Analytical product or case state that may rely on multiple sources and memory records.

## 4. Eligibility

Create or update a memory record when material is used in a completed GF analysis; part of an active GF case or institutional correspondence chain; published as a GF analytical output; significant evidence that changes, confirms, contradicts or supersedes an existing case state; an unresolved but reusable high-value verification question; or a separate event that may indicate recurrence of a documented mechanism.

Do not create independent records for trivial, abandoned or exact duplicate material unless provenance requires preservation.

## 5. Required relationship classification

Use one primary `relationship_type`:

- `NEW`
- `RELATED`
- `CONTINUATION`
- `UPDATE`
- `CORROBORATION`
- `CONTRADICTION`
- `DUPLICATE`
- `SUPERSEDES`
- `RECURRENCE_CANDIDATE`

Classification describes documentary relationship, not motive, culpability or intent.

## 6. Minimum memory record

Each record should contain, where applicable: memory ID/version, dates/status, case/source/analysis references, relationship type and linked memory IDs, jurisdiction, institutions/entities/topics/location/dates, central claim/event, verified facts, supported inferences, unresolved questions, contradictions, key omissions, process stage, mechanism, recurrence key, evidence recheck status, confidence, supersedes and revision history.

## 7. Evidence states

Use `VERIFIED`, `SUPPORTED INFERENCE`, `UNRESOLVED`, `DISPUTED`, `SUPERSEDED`.

A memory record may point to evidence but does not become evidence merely through repetition in GF outputs.

## 8. Retrieval

Search using multiple independent keys where available: case ID, institution, actor/entity, project/program, topic, location/jurisdiction, date range, decision/contract identifiers, process stage, mechanism, recurrence key and distinctive factual phrases.

Semantic similarity alone is insufficient to establish continuity or recurrence.

## 9. Original-evidence recheck

Before a prior memory record materially affects a new conclusion, recheck the relevant SOURCE whenever accessible. Record whether the evidence remains accessible, still supports the stored proposition, has been superseded/qualified, and whether events are genuinely comparable.

If evidence cannot be rechecked, memory may guide retrieval but should not independently support a material conclusion.

## 10. Continuity and recurrence safeguards

Multiple reports of the same originating event are not separate recurrence events. Later communication in the same process normally remains `CONTINUATION` or `UPDATE`. Similar outcome does not prove similar cause. Similar mechanism does not prove common intent, coordination or culpability. Search for material differences and alternative explanations. Absence of a memory record does not establish absence of prior events. Never silently overwrite earlier evidence states.

## 11. Specialized modules

Specialized GF modules may extend this standard but may not weaken source-recheck, two-pass or anti-confirmation-bias safeguards.

`metodologija/media-analysis/17_baseline_pattern_memory_layer_v1_0.md` remains the specialized Media implementation. Its P0–P5 pattern scale, fingerprint and Media-specific template remain authoritative inside GFO Media.

GF-EAML does not replace Media baselines; it provides their broader horizontal parent rule.

## 12. Lifecycle

Statuses: `ACTIVE`, `UPDATED`, `SUPERSEDED`, `RETRACTED`. Updates preserve audit history.

## 13. Standard output when memory comparison is material

Record as applicable: MEMORY SEARCH, RELATIONSHIP TYPE, RELATED RECORDS, SOURCE RECHECK, MATERIAL CONTINUITY, MATERIAL DIFFERENCES, CONTRADICTIONS/SUPERSEDING EVIDENCE, RECURRENCE STATUS, ALTERNATIVE EXPLANATIONS and CONFIDENCE.

## 14. Architectural objective

`SOURCE ↔ MEMORY RECORD ↔ CASE / ANALYSIS ↔ RELATED RECORDS`

Compact records support efficient AI retrieval; original sources remain the evidentiary authority.

## 15. Maintenance record

### v1.0
- Generalized the Media baseline-memory concept into a GF-wide horizontal standard.
- Added SOURCE / MEMORY RECORD / ANALYSIS-CASE separation.
- Added controlled relationship taxonomy.
- Preserved primary-analysis-before-memory and original-evidence-recheck rules.
- Preserved GFO Media v1.0 as specialized implementation.
