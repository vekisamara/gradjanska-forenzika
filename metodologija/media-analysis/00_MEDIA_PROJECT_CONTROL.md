# GFO MEDIA ANALYSIS — PROJECT CONTROL v1.3

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

The Project also contains three optional cross-prompt support layers:

- `15_EPISTEMIC_INTENT_LAYER_v1_0.md` — CURRENT / OPERATIONAL;
- `16_narrative_selection_omission_layer_v1_1.md` — CURRENT / CONTROLLED OPERATIONAL;
- `17_baseline_pattern_memory_layer_v1_0.md` — CURRENT / CONTROLLED OPERATIONAL.

None of Sources 15–17 is a fifth canonical prompt. None may replace, terminate, weaken or silently rescore a canonical analysis.

Permanent Source architecture contains ten files:

- 2 control/runtime Sources (`00–01`);
- 4 canonical analytical prompt Sources (`10–13`);
- 1 publication-layer Source (`14_PUBLICATION_OUTPUT_STANDARD_v1_0.md`);
- 3 optional auxiliary analytical/support Sources (`15–17`).

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
12. synthesize only after separate analyses and support-layer outputs are complete;
13. identify evidence gaps and next verification steps.

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

## 7. Multi-prompt and multi-layer rule

More than one canonical prompt may apply.

Recommended order:

1. public-statement analysis establishes the claim/evidence spine;
2. electoral-context analysis adds election-specific context if activated;
3. media-manipulation analysis evaluates editorial/communication framing;
4. PR analysis evaluates institutional communication if activated;
5. Source 15 runs only when it adds material novelty;
6. Source 16 runs only when it adds material narrative-selection/omission value;
7. Source 17 runs only after the independent primary pass and only when longitudinal comparison is useful;
8. synthesis.

Do not count the same indicator multiple times merely because it appears in several prompts or support layers.

## 8. Fail-open rule for Sources 15–17

The four canonical prompts MUST finish independently of Sources 15–17.

Permitted support-layer statuses include `USED`, `PARTIAL`, `NOT APPLICABLE`, `INSUFFICIENT EVIDENCE` and `UNAVAILABLE` where defined by the source.

Only supported findings from `USED` or `PARTIAL` may enter synthesis. Neutral statuses cannot:

- terminate an analysis;
- lower or erase a canonical score;
- convert a canonical result into failure/N/P;
- weaken an independently evidenced finding;
- act as a publication veto.

## 9. Source hierarchy for verification

Prefer:

1. original statement, full video/transcript or official document;
2. official primary records/data;
3. independent primary sources;
4. high-quality independent secondary sources;
5. media summaries and commentary.

Multiple reproductions of one press release are not multiple independent confirmations.

## 10. Baseline archive boundary

`media-baselines/` contains longitudinal case-memory records.

For MASTER deployment, the full authorized baseline archive may be made available as case-memory context.

For SHARED deployment, only baselines derived from public/published analyses and public evidence should be exposed. Unpublished, sensitive or internal-only baselines must not be included merely because Source 17 is present.

Baseline records are not instruction Sources and must not override Project Control, Runtime or canonical prompts.

## 11. Output discipline

A combined response should normally contain:

- analyzed object and source limitation;
- routing decision;
- neutral reconstruction;
- key claims and evidence status;
- prompt-specific findings;
- optional Source 15/16 findings only when material;
- optional Source 17 pattern finding only after evidence recheck;
- contradictions / missing context / missing evidence;
- confidence and limitations;
- next verification steps;
- short synthesis.

Avoid verdict-first labels such as `LAŽ`, `PROPAGANDA`, `KORUPCIJA`, `ZATAŠKAVANJE` or `MANIPULACIJA` unless the applicable evidence threshold is actually satisfied. Prefer the narrowest finding supported by evidence.

## 12. Project boundary

This Project is an operational application of the locked GFO methodology. Findings from media analyses do not amend the GFO LAB baseline.

Methodological problems discovered here should be recorded as candidate issues and tested before a locked-baseline change.

## 13. Controlled operational status

Source 15 is fully operational based on its prior five-case validation.

Sources 16 and 17 are accepted for controlled operational use after the 2026-09-03 practical regression sequence. Their safeguards worked as intended, including uniform metric direction, omission/framing separation, one overall confidence assessment, independent primary pass before memory, evidence recheck, and same-case anti-recurrence protection.

Broader heterogeneous validation remains desirable before Sources 16–17 are promoted to LOCKED status.

## 14. Maintenance record

### v1.2
- Source 15 operational acceptance preserved.
- Permanent architecture contained eight Sources.

### v1.3 / GFO MEDIA v1.1 — 2026-09-03
- Added Source 16 `Narrative Selection & Omission Layer v1.1` as controlled operational optional layer.
- Added Source 17 `Baseline & Pattern Memory Layer v1.0` as controlled operational optional support layer.
- Permanent methodological Source architecture increased from 8 to 10 files.
- Baseline case records explicitly classified as case-memory, not permanent methodological Sources.
- Added mandatory independent-primary-pass-before-baseline rule.
- Added source-evidence-recheck requirement before recurrence P2–P5.
- Added same-case anti-recurrence safeguard.
- Added MASTER/SHARED baseline exposure boundary.
- Canonical prompts `10–13`, their scoring systems, Publication Output Standard v1.0 and Source 15 scoring/routing authority remain unchanged.
