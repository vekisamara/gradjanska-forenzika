# GFO MEDIA — Populist Personalization, Authoritarian Narrative & Political Dogma Layer v0.3

**Status:** EXPERIMENTAL / CALIBRATED-2  
**Type:** optional cross-prompt analytical layer  
**Project:** GFO MEDIA v1.1  
**Date:** 2026-09-05

## 1. Purpose

This layer detects and documents three independent communication dimensions without classifying a politician, party, institution or outlet as inherently populist or authoritarian:

- **P — Populist Personalization:** concentration of agency, political credit, public benefit and conflict around a leader/administration;
- **A — Authoritarian Narrative:** threat, polarization, delegitimization of alternative authorities, protector logic, indispensability, loyalty/unity demands and procedural exceptionalism;
- **D — Political Dogma / Epistemic Authority:** communication in which political authority tends to determine what counts as acceptable truth, error is displaced or unacknowledged, and contradictory positions may successively be presented as correct without an evidenced bridge.

P, A and D are independent axes. They MUST NOT be added into a single populism/authoritarianism score.

This layer does not replace canonical Sources 10–13 or support Sources 15–17 and MUST NOT silently rescore them.

## 2. Activation

Use only after a canonical claim/evidence spine exists. Activate when the content materially raises questions of personalization, political credit, enemy/obstacle construction, institutional delegitimization, leader-as-protector framing, contradiction over time, epistemic authority or political reversals.

For one item use **SINGLE CONTENT MODE**. For at least three distinct events/items, or when testing a documented reversal between T1 and T2, use **LONGITUDINAL MODE**.

If the layer adds no material value, return `NOT APPLICABLE`.

## 3. Mandatory safeguards

1. Analyze the structure of concrete communication, not ideology, personality or psychology of the speaker.
2. Do not infer intent, manipulation, coordination, corruption or illegality from narrative structure alone.
3. Absence of evidence is not evidence of falsehood.
4. Legitimate political disagreement with a court/institution is not institutional delegitimization by itself.
5. A documented obstruction is not populist merely because it is described as an obstacle.
6. A real security threat is not threat amplification merely because it is serious.
7. A policy reversal is not political dogma by itself. D findings require analysis of the evidentiary/explanatory bridge and accountability for the change.
8. Distinguish factual inconsistency, changed circumstances, changed law/evidence, strategic change, negotiated compromise and unexplained contradiction.
9. Each scored indicator has separate **intensity (0–4)** and **evidence confidence (HIGH/MEDIUM/LOW)**.
10. Every causal attribution must be tested through: `EVENT → INTERPRETATION → ATTRIBUTED CAUSE → POLITICAL CONSEQUENCE`. Missing bridge = `EVIDENCE GAP`; actor-only support = `SOURCE-DEPENDENT ATTRIBUTION`; independent documentary support = `SUPPORTED ATTRIBUTION`.

## 4. Reality Chain vs Narrative Chain

Always reconstruct separately:

**Reality / institutional chain:** documented actors, competencies, decisions, procedures, financing, implementation, reversals and results.

**Narrative chain:** the causal sequence presented to the audience.

A difference between the two is an analytical signal, not proof of deception.

## 5. P — Populist Personalization indicators

Score each 0–4.

- **P1 Leader Centrality** — degree to which leader becomes central causal actor.
- **P2 Political Credit Capture** — concentration of credit that documentary chain distributes among several actors.
- **P3 Origin Displacement** — perceived origin of initiative/solution moves toward leader/administration contrary to or beyond documented origin.
- **P4 Citizen Agency Appropriation** — active citizens/groups become passive beneficiaries of leader's protection/delivery.
- **P5 Delivery Personalization** — public/institutional result presented primarily as leader's delivery.
- **P6 Obstacle Construction** — opponent/institution is narratively assigned the role of blocker.
- **P7 Moral Monopoly** — actor's position is aligned with citizens/children/public good while alternative position is framed as morally inferior rather than merely disputed.
- **P8 Struggle Narrative** — institutional procedure is transformed into struggle/battle/victory dramaturgy.
- **P9 Institutional Complexity Suppression** — material actors, procedures or dependencies are omitted/simplified so that causal agency and political credit appear substantially simpler than the documented chain.

P9 is distinct from P2: P2 asks **who receives credit**; P9 asks **what institutional complexity disappears for that attribution to become persuasive**.

### P provisional classification

Do not rely on arithmetic alone. Use the indicator pattern and explain the classification. Provisional labels: `LOW`, `MODERATE`, `HIGH`, `VERY HIGH`. Thresholds remain experimental pending larger calibration corpus.

## 6. A — Authoritarian Narrative indicators

Score each 0–4.

- **A1 Us-versus-Them Polarization**
- **A2 Threat Amplification**
- **A3 Institutional Delegitimization**
- **A4 Leader-as-Protector**
- **A5 Leader Indispensability**
- **A6 Loyalty and Unity Demand**
- **A7 Identity Fusion** — leader/party/institution fused with people, nation, entity/state or collective identity.
- **A8 Exceptionalism / Procedure Bypass** — extraordinary political objective used to justify bypassing, neutralizing or treating ordinary legal/procedural constraints as illegitimate.

### A-GATE

A classification above LOW requires at least one core indicator at intensity >=2:

`A2 | A3 | A4 | A5 | A8`

A1, A6 or A7 alone cannot activate an elevated authoritarian classification.

### A labels

- `LOW` — A-GATE inactive or no connected core pattern;
- `ELEVATED` — gate active but core elements are limited;
- `HIGH` — multiple connected core indicators;
- `SEVERE` — strong threat plus institutional delegitimization and protector/indispensability or procedure-bypass justification.

### Existential Threat Flag

If **A2 = 4** because an explicit existential/physical threat to the collective is present, set:

`EXISTENTIAL_THREAT_FRAME = TRUE`

This flag is independent of the aggregate A label.

## 7. D — Political Dogma / Epistemic Authority indicators

The D-axis asks: **does communication require political authority to remain epistemically correct even when evidence, institutions or the actor's own later position create a contradiction?**

Score each 0–4.

- **D1 Leader Infallibility** — leader's error becomes difficult/impossible to acknowledge; contrary outcomes are systematically externalized or reinterpreted so the leader remains correct.
- **D2 Institutional Infallibility** — a politically aligned institution is presented as inherently correct or as direct embodiment of the people, such that criticism/constraint is reframed as opposition to the collective itself.
- **D3 Position Reversal without Error Recognition** — a material position is reversed without identifying changed facts/law/circumstances or acknowledging prior error/incompleteness.
- **D4 Truth Follows Political Interest** — descriptions of reality or legitimacy shift in temporal alignment with political advantage/context without a demonstrated evidentiary bridge. **Never infer motive from temporal alignment alone.**
- **D5 Evidence Subordination** — evidence, expertise, judicial findings or institutional records are accepted/rejected primarily according to compatibility with the political position, rather than answered on evidentiary grounds.
- **D6 Retrospective Consistency Reconstruction** — materially contradictory earlier and later positions are retrospectively presented as continuously consistent without an adequate explanatory bridge.

### D safeguards

A change of policy can be legitimate. Before scoring D3/D4/D6, test at least these alternative explanations:

- changed facts or new evidence;
- changed law or binding decision;
- changed institutional competence;
- negotiated compromise;
- tactical change explicitly distinguished from unchanged principle;
- emergency or security context;
- corrected factual error;
- incomplete earlier public record.

If an alternative explanation is supported, reduce or withhold D scoring accordingly.

Do not state `truth follows political interest` as actor intent. Allowed formulation: `the public position changed in parallel with the political context, while the available record does not demonstrate the factual/legal bridge that would explain the change.`

### D classification

D is pattern-based and remains experimental. Use `LOW`, `ELEVATED`, `HIGH` only with an explanation. A HIGH finding normally requires either:

- D3 >=3 plus at least one of D5/D6 >=2; or
- repeated longitudinal evidence that political authority is privileged over contradictory evidence while reversals remain unacknowledged.

No single disagreement with an institution can establish HIGH political dogma.

## 8. Contradiction Persistence Test

For T1 and T2 (or longer series), determine:

1. What exactly was asserted/decided at T1?
2. What exactly was asserted/decided at T2?
3. Are T1 and T2 logically and legally compatible?
4. If not, what fact, law, evidence, competence or circumstance changed?
5. Did the actor publicly identify that change?
6. Was prior error, incompleteness or policy change acknowledged?
7. If not, how is apparent continuity maintained?
8. Who bears responsibility for the earlier position after reversal?
9. Does the communication effectively ask the audience to treat both incompatible positions as correct at the time political authority held them?

Output one of:

`NO MATERIAL CONTRADICTION`  
`EXPLAINED REVERSAL`  
`PARTIALLY EXPLAINED REVERSAL`  
`UNEXPLAINED MATERIAL REVERSAL`  
`INSUFFICIENT EVIDENCE`

## 9. Enemy Function Test

For every negatively framed actor/institution ask whether its narrative function is to:

1. explain failure;
2. explain delay;
3. increase leader value;
4. homogenize supporters;
5. justify conflict;
6. produce fear;
7. delegitimize oversight;
8. turn a political alternative into a moral/collective threat.

A negative actor need not be an invented enemy. The test concerns narrative function, not factual existence of conflict.

## 10. Convergence Detector

### P → A

`I deliver → they block → they act against citizens → they act against our values/collective → extraordinary unity/protection becomes necessary.`

### A → P

`I/we protect the collective → concrete subsidies/projects/services are increasingly represented as products of protective leadership.`

### A ↔ D

Potential escalation:

`institution produces adverse outcome → institution is delegitimized → political authority becomes preferred source of legitimacy/truth → later reversal occurs → prior position is not acknowledged as erroneous → new position becomes the new orthodoxy.`

Convergence is a longitudinal pattern, not proof of authoritarian intent.

## 11. Ideal types for comparison

**Delivery-personalist:**  
`citizen has problem → leader offers benefit → obstacle appears → leader fights → result → political credit.`

**Protection-authoritarian:**  
`collective is threatened → enemy identified → alternative institutions become unreliable/illegitimate → unity is required → strong leadership provides protection.`

**Dogmatic-epistemic:**  
`political authority states position → position becomes accepted orthodoxy → contrary evidence/authority is subordinated → position reverses → error is not acknowledged → new position becomes accepted orthodoxy.`

## 12. Required output schema

For every use return:

- `observed_claim`
- `documented_chain`
- `narrative_chain`
- `missing_links`
- `alternative_explanations`
- `P_scores[] {indicator, intensity, evidence, evidence_confidence}`
- `A_scores[] {indicator, intensity, evidence, evidence_confidence}`
- `A_gate {active, triggered_by}`
- `D_scores[] {indicator, intensity, evidence, evidence_confidence}`
- `contradiction_persistence_test`
- `special_flags {existential_threat_frame}`
- `convergence`
- `classification {P_level, A_level, D_level}`
- `why_not_stronger_label`
- `documents_that_could_change_assessment`

## 13. Calibration record

Calibrated against the following mechanisms/cases during development:

- Banja Luka school uniforms — obstacle construction and moral monopoly;
- Tunjice water system — delivery personalization negative control for authoritarian dimension;
- Kino Kozara / Park oslobođenja — political credit capture, origin displacement and struggle narrative;
- Česma bridge land exchange — institutional complexity suppression and administrative heroization;
- `najbolji izbor` political statement — false-positive control demonstrating need for A-GATE;
- institutional-delegitimization statements concerning the Constitutional Court of BiH;
- explicit existential-threat rhetoric — basis for existential-threat flag;
- NSRS 2025 reversal sequence concerning state judicial/law-enforcement institutions — basis for D-axis and Contradiction Persistence Test.

Calibration examples are not precedent and do not predetermine later scoring. Underlying evidence must be rechecked before reuse.

## 14. False-positive guards

The layer must explicitly consider and, where supported, prefer benign/ordinary explanations including legitimate self-credit, documented obstruction, legitimate security communication, ordinary party branding, policy advocacy, legitimate institutional criticism, shared-credit communication, new evidence and explained policy reversal.

High P does not imply A. High A does not imply D. High D does not establish authoritarianism, dishonesty or illegality. Combined P/A/D findings may justify stronger scrutiny only when each axis is independently evidenced.

## 15. Status and promotion rule

Version v0.3 is **EXPERIMENTAL / CALIBRATED-2**. It is not a canonical prompt and does not modify canonical Sources 10–13 or their scoring.

Promotion toward CURRENT requires a larger mixed corpus with positive and negative controls, including ordinary institutional criticism, normal completed-project promotion, documented obstruction, legitimate security statements, shared-credit communication, explained policy reversals and unexplained reversals.
