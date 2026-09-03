# GFO MEDIA v1.1 — CONTROLLED MIGRATION MANIFEST

**Date:** 2026-09-03  
**Target projects:** `GFO Media Analysis MASTER` and `GFO Media Analysis - shared`  
**Migration type:** additive controlled operational migration  
**Canonical scoring change:** NONE

## 1. Final permanent methodological Source set

Both MASTER and SHARED should contain exactly these ten permanent methodological Sources:

1. `00_MEDIA_PROJECT_CONTROL.md` — **replace old version with Project Control v1.3**
2. `01_GFO_MEDIA_RUNTIME_BASELINE_v1_1.md` — **replace Runtime v1.0**
3. `10_ANALIZA_JAVNE_IZJAVE_v2_1.txt` — unchanged
4. `11_IZBORNI_KONTEKST_2026_v1_0.txt` — unchanged
5. `12_ANALIZA_MEDIJSKE_MANIPULACIJE_v1_0.txt` — unchanged
6. `13_ANALIZA_PR_SAOPSTENJA_v1_0.txt` — unchanged
7. `14_PUBLICATION_OUTPUT_STANDARD_v1_0.md` — unchanged
8. `15_EPISTEMIC_INTENT_LAYER_v1_0.md` — unchanged / CURRENT OPERATIONAL
9. `16_narrative_selection_omission_layer_v1_1.md` — **new controlled-operational Source**
10. `17_baseline_pattern_memory_layer_v1_0.md` — **new controlled-operational Source**

## 2. Files that must actually be uploaded/replaced during this migration

If the projects already contain the verified pre-migration eight-Source set, only four file operations are required:

### REPLACE

- old `00_MEDIA_PROJECT_CONTROL.md` → repository file `metodologija/media-analysis/00_MEDIA_PROJECT_CONTROL.md`
- old `01_GFO_MEDIA_RUNTIME_BASELINE_v1_0.md` → repository file `metodologija/media-analysis/01_GFO_MEDIA_RUNTIME_BASELINE_v1_1.md`

### ADD

- `metodologija/media-analysis/16_narrative_selection_omission_layer_v1_1.md`
- `metodologija/media-analysis/17_baseline_pattern_memory_layer_v1_0.md`

Do not re-upload unchanged Sources 10–15 unless the target project is missing them or their identity/version cannot be verified.

## 3. Files that must NOT be permanent methodological Sources

Do not add as permanent methodological Sources:

- `16_narrative_selection_omission_layer_v1_0.md` — superseded;
- anything under `metodologija/media-analysis/validation/`;
- `media-baselines/_TEMPLATE.md`;
- `media-baselines/README.md`;
- individual `/analize` or `/blog` posts merely as methodology;
- practical test documents;
- case-specific baseline records as instruction Sources.

## 4. Baseline-memory data boundary

Source 17 is methodology. The records under `media-baselines/` are case-memory data.

### MASTER

MASTER may receive/access the full authorized baseline archive where useful, including internal/significant unpublished records if permitted. These records remain case-memory data and never outrank Sources 00–17.

### SHARED

SHARED should receive/access only baseline records derived from public/published analyses and public evidence. Internal, sensitive or unpublished baseline records should remain excluded.

If no baseline archive is loaded/available in either project, Source 17 must return `BASELINE SEARCH: unavailable` and the canonical analysis continues normally.

## 5. Controlled operational status

Source 15 remains fully operational based on its prior five-case validation.

Sources 16 and 17 are `CURRENT — CONTROLLED OPERATIONAL / OPTIONAL / NON-ELIMINATORY` after the 2026-09-03 practical regression sequence.

They are not LOCKED. Broader heterogeneous validation remains desirable.

## 6. Safeguards preserved by migration

- canonical prompts `10–13` remain primary and independent;
- no canonical score is recalculated from Sources 15–17;
- optional-layer failure/unavailability is fail-open;
- Source 16 uses one score direction: 0 low → 4 high;
- Source 16 uses SID, not superseded SIS;
- Source 16 uses one overall confidence assessment, not per-metric confidence;
- Source 17 may search memory only after the independent primary pass;
- prior GFO conclusions do not count as evidence without underlying-source recheck;
- same-event and same-case updates do not manufacture recurrence;
- high omission/framing/pattern scores do not prove intent, illegality or corruption.

## 7. Post-upload verification checklist

After migration verify in each project:

1. exactly ten permanent methodological Sources are loaded;
2. Sources `00–01` are Project Control v1.3 and Runtime v1.1;
3. Sources `10–13` remain unchanged canonical prompts;
4. Source 14 remains publication-layer only;
5. Source 15 remains CURRENT operational optional layer;
6. Source 16 is v1.1 and uses SID + single overall confidence;
7. Source 17 is v1.0 and contains two-pass + evidence-recheck + anti-recurrence rules;
8. `16...v1_0` is not loaded;
9. validation/case files are not permanent methodological Sources;
10. no scoring/routing rule in canonical prompts was modified.

Expected verdict after correct migration: `PASS — GFO MEDIA v1.1 CONTROLLED OPERATIONAL`.
