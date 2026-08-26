# GFO MEDIA — EPISTEMIC & INTENT LAYER v1.0

**Role:** optional cross-prompt analytical enrichment module  
**Status:** CURRENT — OPERATIONAL / FUNCTIONAL / OPTIONAL / NON-ELIMINATORY  
**Scope:** public statements, electoral communication, media framing and institutional PR  
**Authority:** subordinate to GFO Media Project Control, Runtime and all canonical evidence safeguards  
**Operational status:** ACCEPTED FOR PRODUCTION USE — validation completed 2026-08-26

## 1. Purpose

This module adds an evidence-based complexity layer to media analysis. It does not diagnose people, groups or institutions and does not infer hidden mental states. Concepts adapted from mentalization, epistemic trust and complexity-framing are used only as observable communication/process indicators.

The module must never replace the canonical prompt analysis. It may enrich it only where the available material supports an answer.

## 1.1 Operational acceptance

This version is accepted for operational use in GFO Media Analysis after a five-case validation sequence: three heterogeneous regression cases and two fail-open control cases. The validation confirmed that the module preserves canonical findings, introduces no parallel scoring, prevents unsupported intent inference, generates discriminating tests where useful, and can correctly return `NOT APPLICABLE` or `PARTIAL` instead of forcing output.

Operational use is subject to these conditions:
- canonical prompts `10–13` remain primary analytical instruments;
- this module is invoked only after the canonical claim/evidence spine exists;
- the Novelty / Utility Gate is mandatory;
- only supported `USED` or `PARTIAL` findings may enter synthesis;
- neutral statuses remain fail-open and non-eliminatory;
- no psychological diagnosis, hidden-motive inference or parallel scoring is permitted.

**Operational acceptance result:** PASS.

## 2. Fail-open / non-eliminatory rule

For every invocation return one module status:

- `USED` — sufficient material exists for a meaningful module finding;
- `PARTIAL` — at least one materially useful contribution exists, but only some checks can be answered;
- `NOT APPLICABLE` — the object does not materially engage this layer or the layer would only duplicate the canonical prompt;
- `INSUFFICIENT EVIDENCE` — relevant question exists but evidence is inadequate;
- `UNAVAILABLE` — the module/source cannot be executed.

`NOT APPLICABLE`, `INSUFFICIENT EVIDENCE` and `UNAVAILABLE` MUST NOT:

- terminate the canonical prompt;
- lower a canonical score;
- reduce confidence in otherwise independently supported findings;
- convert a finding to `N/P`, unsupported or failed;
- block synthesis or publication-layer drafting;
- be counted as evidence against the analyzed subject.

The canonical prompt must complete independently.

## 3. No parallel scoring

This module creates no numeric manipulation, credibility, intent or trust score. It must not merge, average, normalize or overwrite scoring systems used by canonical prompts.

## 4. Novelty / Utility Gate — mandatory before full execution

Before running the core checks, ask whether this module can add at least one **materially new and decision-useful contribution** beyond what the activated canonical prompt(s) already establish.

A materially useful contribution exists only if the module can add at least one of the following:

1. a new distinction about the **basis of trust** or inspectability of a material claim;
2. a new **intent-discipline clarification** that prevents an unsupported jump from conduct/effect to motive or demonstrated intent;
3. a plausible **alternative explanation plus a discriminating test** capable of changing the next verification step;
4. a material **complexity gap** involving actors, causes, constraints, uncertainty or trade-offs not already captured by the canonical prompt;
5. an **affective/binary framing observation** that materially changes interpretation of evidence, intent, responsibility or the next reporting action.

Do **not** return `USED` merely because one or more core checks can technically be filled in.

If the module would only restate a canonical finding, return:

`NOT APPLICABLE — no material analytical novelty beyond the canonical prompt.`

If exactly one or a limited subset of checks adds material value, return `PARTIAL` and include only those checks.

A module finding is **decision-useful** when it changes at least one of:

- what evidence should be requested next;
- how strongly an inference may be stated;
- whether an alternative explanation remains viable;
- whether a claim depends primarily on authority rather than inspectable evidence;
- how responsibility can be described without proving intent.

## 5. Core checks

### A. Epistemic trust basis

Ask: **On what basis is the audience asked to accept the claim?**

Classify the basis, where supported, as one or more of:
- inspectable evidence/document/data;
- independently reproducible method/calculation;
- official authority only;
- unnamed expertise/authority;
- reputation/status;
- emotional identification or group belonging;
- unsupported assertion;
- mixed / cannot be determined.

Do not treat trust in an official source as proof of the underlying claim.

### B. Epistemic openness

Check whether a reasonable third party can inspect:
- the primary source;
- underlying document/data;
- methodology;
- assumptions;
- uncertainty/limitations;
- correction path;
- responsible actor;
- route for independent verification.

Describe concrete access or verification gaps. Do not infer concealment from non-publication alone.

### C. Intent discipline

Maintain the chain:

`observable act → supported inference → plausible purpose hypothesis → demonstrated intent`

Do not skip levels. Timing, benefit, correlation, rhetoric, omission, anomaly or repeated pattern may justify a hypothesis but do not independently prove intent.

For each material intent claim identify:
- what is directly observed;
- what is inferred;
- evidence supporting intent;
- evidence missing for intent;
- whether a non-intent explanation remains viable.

### D. Alternative explanations / not-knowing stance

For each material anomaly or disputed event, generate only plausible alternatives consistent with available evidence. Where useful include:
- benign/administrative explanation;
- error, capacity or coordination failure;
- systemic/process explanation;
- strategic explanation.

For each alternative identify a **discriminating test**: a document, record, interview, dataset, chronology, technical check or other evidence that would strengthen or weaken it.

Alternative explanations are hypotheses, not equal-probability claims. Do not manufacture alternatives contradicted by established facts.

### E. Affective framing — anti-duplication rule

Identify observable framing that may encourage reactions such as:
- fear/threat;
- anger/indignation;
- pride/belonging;
- gratitude/dependence;
- shame/blame;
- urgency/panic;
- reassurance/minimization;
- hope/triumphalism.

Separate:
1. textual/visual technique;
2. plausible audience effect;
3. purpose hypothesis;
4. demonstrated intent.

Emotional effect ≠ proof of manipulative intent.

**Do not independently report affective framing when the activated electoral/media/PR prompt has already captured the same rhetorical feature and the module adds no new implication for evidence, intent, responsibility or next verification.**

In such cases record internally:

`DUPLICATE — already captured by canonical prompt; omitted from module output.`

Affective framing may appear in the module output only when it materially helps answer at least one of these questions:

- Does the framing encourage the audience to substitute emotional identification for inspectable evidence?
- Does it create an unsupported inference about motive, threat or responsibility?
- Does it compress a complex causal/institutional problem into a misleading binary?
- Does it change the evidence that should be sought next?

Do not repeat rhetorical scoring, examples or labels already present in a canonical prompt.

### F. Binary / us-vs-them compression

Check whether a complex public-interest problem is compressed into moral or identity binaries, including:
- people vs enemies;
- patriots vs traitors;
- competent us vs obstructive them;
- innocent institution vs malicious critics;
- only two possible policy choices when more exist.

Record the omitted alternatives, actors, constraints or trade-offs when they are evidenced.

### G. Work-oriented vs conflict-oriented framing

Describe whether the communication is primarily organized around:
- problem definition, evidence, options, responsibilities, trade-offs and measurable next steps; or
- threat, enemy construction, loyalty, blame, symbolic victory and mobilization.

Use this only as a communication-function description. Do not make psychological diagnoses of groups or speakers.

## 6. Required output

### When status = USED

### Epistemic & Intent Layer

**Module status:** USED

| Check | Finding | Evidence | Limitation |
|---|---|---|---|
| Trust basis | ... | ... | ... |
| Epistemic openness | ... | ... | ... |
| Intent discipline | ... | ... | ... |
| Alternative explanations | ... | ... | ... |
| Affective framing | ... | ... | ... |
| Binary compression | ... | ... | ... |
| Work vs conflict framing | ... | ... | ... |

Omit rows that fail the Novelty / Utility Gate.

Then return:

- **FACT:** facts directly supported by evidence;
- **INFERENCE:** supported but non-direct conclusions;
- **ALTERNATIVE HYPOTHESES:** plausible alternatives and discriminating tests;
- **INTENT EVIDENCE:** demonstrated / partial / absent / insufficient;
- **TRUST BASIS:** what makes the claim inspectable or non-inspectable;
- **COMPLEXITY GAP:** important actors, causes, trade-offs or uncertainty omitted from the communication;
- **UTILITY ADDED:** what this module changes in wording, inference strength or next verification step.

### When status = PARTIAL

Return only:

- **Module status:** PARTIAL
- the one or more checks that add material novelty;
- **UTILITY ADDED:** specific effect on wording, inference or next verification;
- all other checks: `omitted — no material novelty or insufficient evidence`.

### When status = NOT APPLICABLE

Return only:

- **Module status:** NOT APPLICABLE
- **Reason:** one sentence explaining why the module adds no material analytical novelty.

Do not manufacture a table merely to demonstrate that the module was invoked.

## 7. Prohibited uses

Do not:
- diagnose narcissism, paranoia, attachment style, psychopathology or personality traits;
- label citizens or political groups psychologically;
- infer unconscious motives;
- use psychoanalytic terminology as a substitute for evidence;
- treat emotional language as proof of falsehood;
- treat lack of trust as proof that an institution is untrustworthy;
- treat a plausible alternative explanation as exculpatory evidence;
- force a module result when the material does not support one;
- duplicate canonical rhetorical findings merely to make the optional module appear active.

## 8. Relationship to canonical prompts

Canonical prompts MAY call this module after their own claim/evidence reconstruction and before final synthesis.

The module is additive. Canonical prompt findings remain authoritative within their own scope. In conflict, higher-order evidence, provenance, legal-verification, intent and causality safeguards prevail.

The module must pass the Novelty / Utility Gate before any finding is added to final synthesis.

## 9. Maintenance record

### v0.1
- Initial optional Epistemic & Intent Layer.
- Fail-open/non-eliminatory semantics.
- No parallel scoring.

### v0.1.1
- Added mandatory **Novelty / Utility Gate** to prevent duplicative activation.
- `NOT APPLICABLE` now explicitly includes cases where the layer would only repeat canonical findings.
- `PARTIAL` requires at least one materially useful contribution.
- Added **affective-framing anti-duplication rule**.
- Affective findings are included only when they materially affect evidence, intent, responsibility, complexity or next verification.
- Added `UTILITY ADDED` field to make incremental value auditable.

### v1.0
- Promoted from maintenance-tested v0.1.1 to operational v1.0.
- Validation basis: three regression cases + two fail-open control cases.
- ISSUE-EBCJ-001 (duplication/verbosity risk): CLOSED.
- ISSUE-EBCJ-002 (affective-framing overlap): CLOSED.
- Novelty / Utility Gate retained as mandatory production safeguard.
- Fail-open, no-parallel-scoring and anti-duplication safeguards retained unchanged.
- Status: CURRENT — OPERATIONAL / FUNCTIONAL / OPTIONAL / NON-ELIMINATORY.
