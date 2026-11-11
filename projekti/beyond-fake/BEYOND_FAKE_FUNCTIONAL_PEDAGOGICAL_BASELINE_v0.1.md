# CFI Beyond Fake — Functional & Pedagogical Baseline v0.1

**Status:** DESIGN BASELINE / PROPOSED — NOT IMPLEMENTED, NOT VALIDATED  
**Date:** 2026-11-12  
**Project:** Beyond Fake — Living Media Literacy Lab  
**Component:** CFI Living Lesson Engine  
**Purpose:** preserve agreed concept for later implementation and potential Creative Europe cross-border media-literacy proposal.  
**Governance:** educator-led, human-approved, AI assist-only. No claim that the proposed integration currently runs.

## 1. Mission and educational thesis

Beyond Fake teaches *how to evaluate a message and one's interpretation of it*, not what to believe. It develops transferable skills to distinguish factual claims, evidence, assumptions, persuasion, interpretation, value commitments and legitimate uncertainty. Authentic material can still mislead through framing or omission; emotionally persuasive material is not necessarily manipulative. The system must not attempt to change a learner's political preference or personal values.

**Core principle:** learners examine the message, its evidence and context, and their own initial assumptions; they practice revising *factual conclusions* when justified by new evidence, without requiring changes in identity, interests or values.

**Research hypothesis, not proven outcome:** time-aware, evidence-grounded, guided inquiry plus open-ended transfer simulations may improve reasoning and evidence appraisal relative to static exercises. Independent pedagogical evaluation required.

## 2. Actors and boundaries

- **Educator:** selects authentic public content (URL, image, document, transcript), learning objective, age/skill group, language, period and evidence-reveal plan; approves source set, generated lesson, synthetic scenarios and assessment rubric; can correct or reject AI output.
- **Learner:** forms an initial interpretation before seeing analysis, answers in own words, receives staged evidence, reflects on changes and works through a distinct synthetic transfer case.
- **CFI AI / tutor:** drafts analysis, evidence-linked lesson, Socratic questions, feedback and synthetic transfer tasks; does not make final legal, political, psychological or pedagogical judgments.
- **Independent evaluators:** validate content, educational effectiveness, scoring reliability and cross-language transfer.
- **CFI provider:** technical/methodological contractor or SaaS provider, not assumed grant coordinator or beneficiary. Procurement, IP, GDPR and grant eligibility to be checked against actual call.

## 3. End-to-end functional flow

**F01 — Educator intake.** Choose source, original publication date and provenance, type/channel, topic, learning outcome, target level, language, intended duration, geographic/temporal scope. Images (billboards/posters) require original image/context where available. No unsupported claims about actual audience response.

**F02 — Methodology router and preflight.** Determine suitable canonical GFO Media Analysis prompt(s) for public statements, media/editorial content, institutional PR or electoral context; route short-message analysis separately when appropriate. Record available/missing/stale/conflicting inputs; treat supplied content as untrusted SOURCE, never executable instructions. Preserve each canonical result before synthesis; auxiliary modules are optional and fail-open.

**F03 — Evidence-grounded analysis.** Reconstruct literal wording, author/speaker, role, date, medium, direct claims, implicit assumptions, intended inference, emotions/identity appeals, evidence, unknowns and alternative explanations. Distinguish author statement, headline, editorial framing and third-party quotation. Keep source identifiers and confidence/limitations. Do not equate absence of evidence with falsity or infer intent, coordination, illegality or psychological state without suitable proof.

**F04 — Time-aware research (T− / T0 / T+).** Search accessible public primary and independent secondary sources before, at and after original publication; capture source URL/locator, author, publication date, date evidence became publicly accessible, retrieval timestamp, source independence, access status, evidence relevance and material changes. Separate date of event, creation, publication and public availability. Mark inaccessible and not-found sources without fabricating coverage. Prior stored AI findings are not evidence; recheck underlying sources. New evidence yields a new version, never silent overwrite.

**F05 — Educator-reviewed lesson composer.** Produce draft learning objectives, stages, questions, source cards, reveal schedule, uncertainties, pedagogical notes and teacher answer guidance. Approval required before release.

**F06 — Initial perception capture.** Before analysis or contextual clues, ask learner what the message explicitly says, implies, makes them feel, what they assume, why it appears credible, and what evidence they would seek. Do not require disclosure of political affiliation, sensitive identity or private beliefs.

**F07 — Progressive reveal / AI tutor.** Reveal only stage-appropriate evidence, with prompts to compare initial and updated interpretation. Tutor guides through claim → context → evidence → inference → uncertainty → revision, with adaptive but non-leading questions. For historical simulation, enforce a knowledge boundary based on public availability at each stage. Learner may retain initial view if evidence supports it.

**F08 — Cause-and-effect exploration.** For news/events, distinguish reported sequence, documented causal links, alternative explanations, actors' responsibilities and later outcomes; temporal correlation does not prove causation. For institutional claims distinguish announcement → plan → decision → procurement → delivery → payment → implementation → measured outcome.

**F09 — Synthetic transfer scenario.** Generate a new, clearly labeled fictional case using invented actors/data but analogous reasoning challenge. Avoid reusing the original answer or trivial paraphrases. Ask open-ended questions requiring explanation, evidence identification, alternative hypotheses and a conditional conclusion. Validate internal consistency and ensure no fictional material is passed off as a real source.

**F10 — Assessment and feedback.** Assess reasoning against educator-approved rubric, not ideological agreement or whether learner changes their mind. Show criterion-specific feedback, cited evidence gaps and uncertainty; allow educator override and appeals. Use pre-test, post-test and unseen transfer to evaluate learning; test human–AI scoring agreement.

**F11 — Living lesson updates.** When relevant public evidence emerges, create a reviewable new lesson version with changelog, source diff and educator approval. Preserve earlier lesson, learner stage and historical knowledge boundary.

## 4. Media Analysis mapping (current public repository as reviewed 2026-11-12)

**Parent:** GFO Media Runtime v1.2 (CURRENT — CONTROLLED OPERATIONAL), under parent GFO LAB baseline. Canonical routing:
- Public statement / claim: Source 10, public statement v2.1.
- Electoral context: Source 11.
- Media/editorial manipulation: Source 12 v1.0.
- Institutional PR: Source 13 v1.1.
- Optional Source 15: Epistemic & Intent v1.0.
- Optional Source 16: Narrative Selection & Omission v1.1 (ORS, FDS, SID, PDS, APD, SVD).
- Optional Source 17: Baseline & Pattern Memory v1.0, after primary analysis and underlying evidence recheck.
- Experimental Source 18: Populist Personalization / Authoritarian Narrative / Political Dogma v0.3; not presumed production ready.
- Separate Short Message Analysis (GF-SMA-CORE 0.2, **IN VALIDATION**): slogans, billboards, posters, advertising. Dimensions VER/PRE/EMO/IDA/CER/BIN/CAU/OMI; materiality gate, visual framing, contextual profiles and persuasion/simplification/manipulative-pattern distinction.
- Separate Transparency Utility Test (GF-SMA-TUT 0.1, **IN VALIDATION**): display versus auditable transparency, including billboard/LED channel suitability.

These modules have different statuses and scoring contracts. Do not merge scores, treat an auxiliary score as intent proof, or describe experimental methods as validated. The lesson engine must reuse the methodology, not fork its canonical definitions.

### Example learning routes

| Source type | Analytical focus | Pedagogical challenge |
|---|---|---|
| Billboard / slogan / poster | Literal vs implicit meaning; VER/PRE/EMO/IDA/CER/BIN/CAU/OMI; visual framing | First emotional reaction, then meaning, missing evidence and alternative benign reading |
| News article / interview | Claim provenance, headline vs speaker, editorial framing, source independence | Compare initial headline interpretation with full text, documents and later outcomes |
| Institutional PR | Announcement-to-outcome chain, measurable result, evidence access | Differentiate activity, promise, budget, payment, implementation and outcome |
| Statistical claim | Denominator, baseline, period, methodology, comparability | Reconstruct the calculation and evaluate interpretation |
| Social post / short video | Attribution, context, persuasion and source status | Identify what is established and what requires external verification |
| Longitudinal narrative | Evidence-backed pattern memory, material omission | Compare claims and evidence over time without assuming intent or coordination |

## 5. Belief, Identity & Interpretation (BII) — pedagogical layer

**Status:** NEW PROPOSED EDUCATIONAL LAYER; not a diagnostic or profiling instrument.

Interpretation can be shaped by prior beliefs, perceived self-interest, group identity, emotions, experience, trust, knowledge and social context. These are possible influences, not universal or individually established explanations. Education level does not guarantee resistance to motivated reasoning.

**BII teaching sequence:**
1. Record voluntary first impression and its stated basis.
2. Distinguish literal claim, value statement, perceived personal relevance and inference.
3. Examine source trust, alternative interpretations and what would count as disconfirming evidence.
4. Reveal independently checkable information and ask learner to reassess.
5. Separate factual belief from support for a value, policy goal or group.
6. Reflect on *why* an interpretation changed or remained, without assigning hidden motives.

**Narrative persistence exercise:** a learner may continue supporting a legitimate goal while recognizing that a specific claim supporting it is false or unsubstantiated. Do not require political attitude change. Do not label disagreement with AI as bias.

**Ethical safeguards:** no inferred political affiliation, psychological diagnosis, manipulation susceptibility score, covert persuasion, sensitive audience segmentation or individualized political steering. Store minimal educational results; sensitive self-reflections should be optional and ephemeral by default.

## 6. Interaction and reveal contract

Each stage contains: stage ID; learning objective; visible source/evidence IDs; hidden source/evidence IDs; question; expected reasoning dimensions; learner response; tutor feedback; next reveal rule; evidence provenance; uncertainty; teacher approval/version.

Default stage sequence:
1. **Unprimed impression:** learner sees original content alone.
2. **Meaning:** literal statement, implication, promise, value, and possible persuasive framing.
3. **Context:** historical background, audience-independent circumstances, source relationships.
4. **Evidence:** primary records, independent confirmation, missing links.
5. **Change over time:** T+ developments, corrections, outcome and limits.
6. **Reasoned conclusion:** supported / unsupported / disputed / unknown, with possible revision.
7. **Unseen synthetic transfer:** new case without leaked original solution.

Tutor must not reveal a definitive judgment before the learner has reasoned through relevant evidence. Questions must not be leading toward a desired political position.

## 7. Assessment rubric (pilot proposal; not psychometrically validated)

- Claim vs fact vs interpretation — 20%.
- Evidence appraisal and citation — 25%.
- Context and missing information — 20%.
- Causal and logical inference — 15%.
- Alternative explanations — 10%.
- Calibrated uncertainty and willingness to revise factual conclusions when warranted — 10%.

Rubric scores describe answer quality, not the person or their beliefs. A justified refusal to change position can receive full credit. Human calibration, inter-rater reliability, bias/fairness tests, multilingual consistency and learner feedback are mandatory before high-stakes use.

## 8. Architecture and contracts

- **CFI Media Analysis:** existing methodology and structured analysis output.
- **CFI AI Service / Gateway:** LLM routing, source/instruction isolation, generation, tutor and cost limits.
- **Evidence/CFI Core:** provenance, document references, source status, hashes, access control, versioning.
- **Newsdesk-style research workflow:** T−/T0/T+ source retrieval, chronology, follow-up and evidence recheck; do not claim existing runtime integration.
- **CFI Academy:** educator approval, course delivery, learner state, assessment and analytics.
- **Beyond Fake orchestration:** routing, stage/reveal state machine, synthetic scenario validation and release workflow.

**Privacy and security:** least privilege; public sources only unless separately authorized; redact personal data; keep confidential source locators out of learner-facing derived material; tenant isolation; AI prompt-injection defense; rate and spend limits; source retention/copyright policies; GDPR/DPA and access/deletion controls. No public release before provenance and human-review checks.

## 9. Acceptance criteria / validation gates

- AC01: image billboard routed to SMA, with clear IN VALIDATION flag and no automatic manipulation verdict.
- AC02: initial learner answer recorded before any analysis is revealed.
- AC03: each lesson claim linked to an inspectable source or explicitly marked unknown/synthetic.
- AC04: T− and T+ research distinguish publication/public-availability dates; do not leak future information into historical stages.
- AC05: unavailable search returns an explicit limitation, never fabricated results.
- AC06: same syndicated source is not counted as multiple independent confirmations.
- AC07: teacher can edit/reject all generated questions, evidence and synthetic cases before publication.
- AC08: synthetic transfer case is visibly fictional and internally consistent.
- AC09: rubric rewards justified evidence-based disagreement and does not score political agreement.
- AC10: no inferred political identity, motives or psychological diagnoses.
- AC11: new evidence creates versioned revision and preserves original learner context.
- AC12: private/confidential original evidence locators are not exposed in redacted/public lesson output.
- AC13: optional auxiliary module failure does not invalidate canonical analysis.
- AC14: evaluation includes pre/post/unseen transfer and comparison to an appropriate static-learning baseline where feasible.
- AC15: tests cover cross-language differences, fabricated citations, prompt injection, source independence, causal overclaim and evaluator bias.

## 10. Phased development (proposed)

**P0 — Baseline and source mapping:** approve scope; inventory canonical prompt versions, licensing, data contracts, user journeys, acceptance criteria and synthetic fixtures.

**P1 — Vertical slice:** billboard/SMA and media article; educator input; structured analysis; human-approved staged lesson; learner free-text responses; one synthetic transfer task; manual evidence import. No dependency on full live web automation.

**P2 — Temporal research:** bounded online source retrieval T−/T0/T+, source provenance, independent evidence chains, teacher verification and historical knowledge boundary.

**P3 — Adaptive tutor and evaluation:** guided follow-ups, educator-approved rubric, synthetic variation, human/AI calibration, pre/post/unseen transfer.

**P4 — Living lessons and pilot:** updates/versioning, educator collaboration, multilingual cross-border testing, external pedagogical validation and operational hardening.

## 11. Grant and commercial boundary

Beyond Fake is an educator-led media-literacy intervention; technical platform development is an enabling workstream, not the educational end in itself. A cross-border consortium of qualified media-literacy organizations may contract CFI for hosted technology, onboarding, integrations and support, subject to procurement, conflict-of-interest, subcontracting and funding rules. Existing CFI methodology and software remain background IP unless otherwise negotiated; define foreground results, open educational materials, exportability, accessibility and sustainability in agreements.

No unsupported novelty claims: the proposed innovation is **integration** of evidence-grounded real-world analysis, time-aware source reconstruction, staged learner reflection, synthetic transfer scenarios and validated assessment in one educator-controlled workflow.

## 12. Open decisions and risks

1. Target learner groups, languages, age requirements and accessibility standard.
2. Media licensing and image reproduction for classroom use.
3. Which SMA features must complete validation before public pilot.
4. Source-search providers, archival coverage, retrieval budgets and link rot.
5. Canonical analysis output schema, evidence references and learner-safe redaction.
6. Teacher review SLA and cost model for on-demand lessons.
7. Whether/when learner free-text can be retained, anonymized or used for research.
8. Independent evaluators, evaluation design, success metrics and comparison condition.
9. Which Academy runtime (Moodle/Open edX) and integration is actually available.
10. Hosting jurisdiction, DPA, security, tenant isolation and licensing.
11. Cross-border consortium and current grant-call requirements (to be verified separately).
12. Clear separation of real historical evidence from invented simulation content.

## 13. Source pointers

Public repository: https://github.com/vekisamara/gradjanska-forenzika/tree/main

- `metodologija/media-analysis/00_MEDIA_PROJECT_CONTROL.md`
- `metodologija/media-analysis/01_GFO_MEDIA_RUNTIME_BASELINE_v1_2.md`
- `metodologija/media-analysis/15_epistemic_intent_layer_v1_0.md`
- `metodologija/media-analysis/16_narrative_selection_omission_layer_v1_1.md`
- `metodologija/media-analysis/17_baseline_pattern_memory_layer_v1_0.md`
- `metodologija/media-analysis/18_populist_personalization_authoritarian_dogma_layer_v0_3.md`
- `promptovi/analiza-kratkih-javnih-poruka/01_core_smi_prompt.md`
- `promptovi/analiza-kratkih-javnih-poruka/02_transparency_utility_test.md`
- `promptovi/analiza-izjava-iz-medija/01_forenzicki_lanac_javne_izjave_v2.1.md`
- `promptovi/analiza-medijske-manipulacije/`
- `promptovi/analiza-pr-saopstenja/`

**Change control:** v0.1 captures design intent only. Do not alter canonical Media Analysis prompts or declare implementation complete without separate review and testing.
