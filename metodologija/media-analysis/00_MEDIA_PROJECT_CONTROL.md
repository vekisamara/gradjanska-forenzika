# GFO MEDIA ANALYSIS — PROJECT CONTROL v1.4

**Project release:** GFO MEDIA v1.1  
**Project type:** operational media/public-communication analysis  
**Parent methodology:** GFO LAB Universal Baseline v2.0.1 — VERIFIED & LOCKED  
**Project baseline:** GFO Media Runtime Baseline v1.1  
**Status:** CURRENT — CONTROLLED OPERATIONAL

## 1. Purpose and architecture

This Project analyzes public statements and media/institutional communication through four canonical AI prompts:

1. `10_ANALIZA_JAVNE_IZJAVE_v2_1.txt`
2. `11_IZBORNI_KONTEKST_2026_v1_0.txt`
3. `12_ANALIZA_MEDIJSKE_MANIPULACIJE_v1_0.txt`
4. `13_ANALIZA_PR_SAOPSTENJA_v1_0.txt`

The canonical prompts remain separate analytical instruments. Project routing may activate one or more prompts, but must not silently merge their scoring systems, terminology or conclusions.

The Project also contains three CURRENT optional cross-prompt support layers:

- `15_EPISTEMIC_INTENT_LAYER_v1_0.md` — CURRENT / OPERATIONAL;
- `16_narrative_selection_omission_layer_v1_1.md` — CURRENT / CONTROLLED OPERATIONAL;
- `17_baseline_pattern_memory_layer_v1_0.md` — CURRENT / CONTROLLED OPERATIONAL.

It also contains one EXPERIMENTAL calibrated layer:

- `18_populist_personalization_authoritarian_dogma_layer_v0_3.md` — EXPERIMENTAL / CALIBRATED-2.

None of Sources 15–18 is a fifth canonical prompt. None may replace, terminate, weaken or silently rescore a canonical analysis. Source 18 is not CURRENT and must remain explicitly labeled experimental in analytical output.

Permanent operational Source architecture remains the established v1.1 control/runtime + canonical + publication + CURRENT support set. Source 18 is an experimental extension and is not counted as a promoted CURRENT permanent Source until separate acceptance/promotion.

The baseline records stored under `media-baselines/` are case-memory records, not permanent methodological Sources. Validation documents are test artifacts, not permanent methodological Sources.

## 2. Default workflow

When the user provides a link, article, statement, transcript, screenshot, video description, official announcement or supporting document:

1. preserve/identify the analyzed content;
2. determine the closest primary source;
3. classify the content;
4. select the minimum sufficient canonical prompt set;
5. gather current external evidence when verification requires it;
6. execute selected canonical prompt(s);
7. keep prompt-specific findings distinguishable;
8. optionally invoke Source 15 only if its Novelty / Utility Gate passes;
9. optionally invoke Source 16 only if it can add material omission/framing/source-independence value beyond the canonical findings;
10. only after the primary analysis is complete, optionally invoke Source 17 for baseline retrieval and recurrence testing;
11. recheck underlying evidence before any prior baseline is counted toward recurrence;
12. optionally invoke experimental Source 18 when personalization, authoritarian narrative, political dogma/epistemic authority or longitudinal contradiction is materially relevant;
13. synthesize only after separate analyses and support-layer outputs are complete;
14. identify evidence gaps and next verification steps.

If the user simply says `analiziraj`, perform routing automatically.

## 3. Canonical prompt routing

### A. Public statement / factual claim

Use `10_ANALIZA_JAVNE_IZJAVE_v2_1.txt` as the default primary prompt when the central object is a statement by a public official, institution or other bearer of public responsibility.

### B. Electoral/political context 2026

Add `11_IZBORNI_KONTEKST_2026_v1_0.txt` when the content is materially connected to the 2026 electoral/preelectoral context, party competition, campaign framing, voter targeting, political promises or electoral rhetoric.

Electoral timing alone is not proof of manipulation, intent, coordination or electoral purpose.

### C. Media manipulation

Use/add `12_ANALIZA_MEDIJSKE_MANIPULACIJE_v1_0.txt` when the analytical object includes editorial framing, headline, lead, image choice, omission, source attribution, clickbait, emotional/statistical framing or separation between speaker and media responsibility.

Do not assess the outlet as a whole.

### D. Institutional PR

Use/add `13_ANALIZA_PR_SAOPSTENJA_v1_0.txt` when the content is official/institutional communication or a public official is speaking in an institutional capacity and the relevant question concerns promotion, plan-versus-result substitution, crisis PR, minimization, responsibility shifting or verifiability of institutional claims.

## 4. Optional Source 15 — Epistemic & Intent Layer

After the canonical analysis has a claim/evidence spine, Source 15 MAY be used when epistemic trust, intent discipline, alternative explanations, binary framing or complexity compression can add material analytical value.

The mandatory Novelty / Utility Gate applies.

If the module would only repeat canonical findings, return `NOT APPLICABLE`.

Neutral statuses are fail-open and must not affect canonical scoring, confidence or completion.

## 5. Optional Source 16 — Narrative Selection & Omission Layer

Source 16 MAY be used after the canonical claim/evidence spine exists when selection, omission, framing, source independence, PR dependence, missing alternative evidence or systemic-context visibility are materially relevant.

Source 16 must follow these rules:

- one numerical direction for all metrics: `0 = low/not established`, `4 = high/strongly expressed`;
- use SID, not the superseded SIS direction;
- no per-metric confidence column;
- use one overall finding-confidence level after the table;
- use `N/A — INSUFFICIENT EVIDENCE` rather than forcing a number;
- PDS is not applicable when the analyzed object is the originating PR itself;
- high ORS/FDS/SID/PDS/APD/SVD does not prove falsehood, illegality, concealment or intent;
- canonical scores are never recalculated from Source 16 metrics.

Source 16 is optional and non-eliminatory. It may enter synthesis only when it adds material value.

## 6. Optional Source 17 — Baseline & Pattern Memory Layer

Source 17 MAY be used for longitudinal retrieval and recurrence testing only after the primary analysis of the new item is complete.

Mandatory two-pass order:

`NEW CONTENT → PRIMARY CANONICAL ANALYSIS → BASELINE RETRIEVAL → PATTERN COMPARISON → SOURCE EVIDENCE RECHECK → PATTERN ASSESSMENT → SYNTHESIS`

Rules:

- prior GFO conclusions are not evidence merely because they exist in a baseline;
- before a prior event counts toward P2–P5, the underlying evidence supporting the matching mechanism must be rechecked;
- multiple publications about the same originating event are not separate recurrence events;
- later communications in the same continuing case do not automatically create a new case;
- similarity of outcome does not prove similarity of cause;
- similarity of mechanism does not prove common intent, coordination, illegality or corruption;
- absence of a baseline is not evidence that no prior event existed.

If the baseline archive is unavailable, return `BASELINE SEARCH: unavailable` and continue the canonical analysis normally.

## 7. Experimental Source 18 — P/A/D Layer

Source 18 MAY be used after the canonical claim/evidence spine exists when the content materially raises one or more of these questions:

- personalization of public benefit, agency or political credit;
- obstacle/enemy construction;
- threat/protector/indispensability framing;
- institutional delegitimization or procedural exceptionalism;
- political dogma / epistemic authority;
- material contradiction or policy reversal across time.

Source 18 keeps three independent axes: P (Populist Personalization), A (Authoritarian Narrative) and D (Political Dogma / Epistemic Authority). They must never be combined into one score.

Mandatory safeguards include A-GATE, separate intensity/evidence-confidence fields, Reality Chain vs Narrative Chain, Contradiction Persistence Test for reversals, alternative-explanation testing and prohibition on intent inference from temporal correlation.

Source 18 is EXPERIMENTAL / CALIBRATED-2. Its output must not silently change canonical scores or be described as a final classification of a person, party, institution or media outlet.

## 8. Multi-prompt and multi-layer rule

More than one canonical prompt may apply.

Recommended order:

1. public-statement analysis establishes the claim/evidence spine;
2. electoral-context analysis adds election-specific context if activated;
3. media-manipulation analysis evaluates editorial/communication framing;
4. PR analysis evaluates institutional communication if activated;
5. Source 15 runs only when it adds material novelty;
6. Source 16 runs only when it adds material narrative-selection/omission value;
7. Source 17 runs only after the independent primary pass and only when longitudinal comparison is useful;
8. experimental Source 18 runs only after evidence reconstruction and when P/A/D questions add material value;
9. synthesis.

Do not count the same indicator multiple times merely because it appears in several prompts or support layers.

## 9. Fail-open rule for Sources 15–18

The four canonical prompts MUST finish independently of Sources 15–18.

Permitted support/experimental-layer statuses include `USED`, `PARTIAL`, `NOT APPLICABLE`, `INSUFFICIENT EVIDENCE` and `UNAVAILABLE` where defined by the source.

Only supported findings from `USED` or `PARTIAL` may enter synthesis. Neutral statuses cannot:

- terminate an analysis;
- lower or erase a canonical score;
- convert a canonical result into failure/N/P;
- weaken an independently evidenced finding;
- act as a publication veto.

Experimental Source 18 additionally cannot promote itself to CURRENT status through use in a case analysis.

## 10. Source hierarchy for verification

Prefer:

1. original statement, full video/transcript or official document;
2. official primary records/data;
3. independent primary sources;
4. high-quality independent secondary sources;
5. media summaries and commentary.

Multiple reproductions of one press release are not multiple independent confirmations.

## 11. Baseline archive boundary

`media-baselines/` contains longitudinal case-memory records.

For MASTER deployment, the full authorized baseline archive may be made available as case-memory context.

For SHARED deployment, only baselines derived from public/published analyses and public evidence should be exposed. Unpublished, sensitive or internal-only baselines must not be included merely because Source 17 is present.

Baseline records are not instruction Sources and must not override Project Control, Runtime or canonical prompts.

## 12. Output discipline

Keep separate:

- observed content;
- verified external facts;
- source-dependent allegations;
- analytical inference;
- evidence gaps;
- alternative explanations;
- prompt-specific scores/findings;
- optional support-layer findings;
- experimental Source 18 P/A/D findings when used.

Do not present an analytical inference as a verified fact. Do not use labels about a person's character or ideology where the evidence supports only a communication pattern.

## 13. Change-control boundary

This control update registers Source 18 as an experimental extension only. It does not modify the text, scoring, routing logic or canonical status of Sources 10–13. Sources 15–17 retain their prior status and safeguards.
