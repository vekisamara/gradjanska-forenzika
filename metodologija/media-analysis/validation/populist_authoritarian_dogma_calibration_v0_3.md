# GFO MEDIA P/A/D Layer v0.3 — Calibration Record

**Date:** 2026-09-05  
**Layer:** `18_populist_personalization_authoritarian_dogma_layer_v0_3.md`  
**Status:** PASS WITH CALIBRATION CHANGES → incorporated into v0.3

## Calibration purpose

The calibration tests whether the layer can distinguish political personalization from authoritarian narrative and political dogma without producing false positives from ordinary PR, legitimate institutional criticism or policy change.

## Cases and principal findings

| Case | P | A | D | Principal mechanism |
|---|---|---|---|---|
| Banja Luka school uniforms | HIGH | ELEVATED candidate | not tested | obstacle construction + moral monopoly |
| Tunjice water system | MODERATE | LOW | LOW/not applicable | delivery personalization |
| Kino Kozara / Park oslobođenja | VERY HIGH | LOW | LOW/not applicable | credit capture + origin displacement + struggle narrative |
| Česma bridge land exchange | HIGH | LOW | not established | complexity suppression + administrative heroization |
| `najbolji izbor` statement | MODERATE | LOW after A-GATE | not established | unanimity/superlative without core authoritarian gate |
| Constitutional Court delegitimization rhetoric | MODERATE | HIGH candidate | ELEVATED candidate | institutional delegitimization |
| existential-threat rhetoric | MODERATE | HIGH | not established | threat amplification + identity fusion |
| NSRS 2025 reversal sequence | separate P not material | A relevant | HIGH candidate pending full corpus recheck | reversal without error recognition + evidence/authority subordination |

## Changes adopted

### 1. A-GATE

Raw arithmetic produced a false-positive risk: polarization/unanimity/identity rhetoric could generate a misleading moderate A score without threat, delegitimization, protector logic, indispensability or procedure bypass.

v0.3 therefore requires at least one of A2/A3/A4/A5/A8 at intensity >=2 before A can exceed LOW.

### 2. Existential Threat Flag

A2=4 triggers a separate `EXISTENTIAL_THREAT_FRAME` flag. It is not itself a finding of authoritarian intent.

### 3. Intensity separated from evidence confidence

Every P/A/D indicator records both intensity and evidence confidence. Strong rhetoric may be HIGH-confidence as an observed frame while the factual causal allegation embedded in it remains unresolved.

### 4. P9 Institutional Complexity Suppression

Added after the Česma land-exchange test. It detects material compression of multi-actor legal/administrative processes. It is distinct from P2 Political Credit Capture.

### 5. D-axis Political Dogma / Epistemic Authority

Added after analysis of reversals in which political/institutional positions may change materially while prior error, changed evidence or changed legal principle is not clearly acknowledged.

D1 Leader Infallibility  
D2 Institutional Infallibility  
D3 Position Reversal without Error Recognition  
D4 Truth Follows Political Interest  
D5 Evidence Subordination  
D6 Retrospective Consistency Reconstruction

D is independent of P and A.

### 6. Contradiction Persistence Test

Added to prevent the model from treating every policy reversal as dogma. The test requires comparison of T1/T2, changed facts/law/evidence, public explanation, acknowledgment of error/incompleteness, and alternative explanations.

## Key false-positive findings

- Completed-project promotion may be personalized without being authoritarian.
- Unanimity and political certainty are insufficient for A without A-GATE.
- Criticism of a court decision is not the same as delegitimization of the court as an institution.
- Documented obstruction is not automatically populist obstacle construction.
- A policy reversal is not dogma if changed facts, law, evidence, competence or negotiated compromise adequately explain it.
- Temporal proximity between a reversal and political benefit does not prove motive.

## Validation status

**PASS WITH CALIBRATION CHANGES — CHANGES INCORPORATED IN v0.3.**

The layer remains EXPERIMENTAL / CALIBRATED-2. It must not modify canonical Sources 10–13. Promotion requires a larger mixed corpus and explicit negative controls.
