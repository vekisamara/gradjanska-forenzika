# VALIDATION CASE 008 — Historical Baseline 2022 + 2025 v0.1

Status: **PASS**

## Inputs

- 2022 CIK Race5 snapshot: `snapshot-20260825T204018.258699Z-95f56f5a`
- 2025 CIK Race5 snapshot: `snapshot-20260824T211536.942059Z-01efb8c5`
- Mapping result: Validation Case 007
- Baseline engine semantics: `baseline_engine_v0_1.py` / v0.1.0
- Minimum mapping confidence: `0.95`
- Minimum election count: `2`

## Scope

The baseline uses only the 1,799 polling stations whose 2022→2025 mapping was usable at the default confidence threshold. Canonical 2025 identity mappings were added explicitly for those same stations so that each canonical polling-station identity has exactly two election observations.

Political-share baseline was intentionally not calculated because no explicit cross-election `political_bloc_id` mapping has been reviewed. Candidate-name continuity was not inferred.

## Result

- Baseline polling stations: **1,799**
- Station-election observations: **3,598**
- Stations with exactly two turnout-eligible elections: **1,799 / 1,799**
- Validation flags: **0**
- Bloc-share baseline rows: **0** (by design)

## Descriptive baseline

Across the 1,799 mapped stations:

- mean 2022 turnout: **53.72%**
- mean 2025 turnout: **36.17%**
- mean station-level turnout change, 2025 minus 2022: **-17.55 percentage points**
- median station-level turnout change: **-16.80 percentage points**
- mean 2022 invalid-ballot rate: **6.15%**
- mean 2025 invalid-ballot rate: **1.87%**

These are descriptive historical measurements only. They are not anomaly scores and do not imply irregularity.

## Methodological note

With only two elections, the calculated standard deviations are mathematically valid but are not yet robust estimates of long-run variance. This baseline is sufficient for pipeline validation and provisional historical comparison, but the next historical cycle should materially improve variance estimates.

## Result

**PASS.** The two-election Historical Baseline pipeline is operational for 1,799 conservatively mapped polling stations, with zero validation flags and no inferred political equivalence.
