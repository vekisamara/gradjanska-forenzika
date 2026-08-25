# VALIDATION CASE 010 — Historical Anomaly Engine v0.1

Status: **PASS WITH METHODOLOGICAL LIMITATION**

## Purpose

Validate the mechanics of `historical_anomaly_engine_v0_1.py` using a retrospective 2025 observation layer against a 2022-only structural baseline and 2022-only peer reference.

This test validates calculation, mapping, missing-data behavior and determinism. It does **not** validate substantive anomaly interpretation because the compared election contexts are not equivalent.

## Inputs

Historical reference:

- election: 2022 Republika Srpska presidential general election;
- 1,799 polling stations accepted by the reviewed 2022 → 2025 mapping;
- one historical election per station;
- therefore historical station-level standard deviation is unavailable by design.

Current observation layer:

- election: `2025-BIH-RS-PRES-BYELECTION-CONFIRMED`;
- 1,799 mapped polling stations.

Peer reference:

- Peer Group Engine v0.1 rerun using 2022-only baseline features;
- same-municipality candidates only;
- political features excluded;
- 1,765 usable peer groups and 34 `insufficient_peer_group` cases, consistent with Case 009 structure.

## Result counts

- historical baseline station count: **1,799**;
- current mapped station count: **1,799**;
- signal rows: **1,799**;
- validation flags: **0**;
- non-null historical turnout z-scores: **0**, expected because the 2022-only baseline contains one election and no historical variance;
- non-null peer turnout z-scores: **1,765**;
- non-null peer invalid-rate z-scores: **1,764**.

## Determinism

Two runs with identical inputs and parameters produced byte-identical:

- `historical_anomaly_signals.csv`;
- `validation_flags.csv`.

Signal CSV SHA-256:

`1291008003ccacc513faead25c7fefc819f654b45c56df59f9cf5ec579489dc2`

Determinism criterion: **PASS**.

## Structural invariants

PASS:

1. one signal row exists for every mapped current polling station with a historical baseline;
2. no composite anomaly score is produced;
3. no political variable is used;
4. historical z-scores remain null when historical variance is unavailable;
5. peer signals remain unavailable where no usable peer group exists rather than being fabricated;
6. current totals are internally consistent;
7. no validation errors are emitted;
8. repeated execution is deterministic.

## Observed retrospective signal distribution

The 2025 by-election has a strong system-wide distribution shift relative to the 2022 general election:

- mean historical turnout delta: **-0.175498**;
- median historical turnout delta: **-0.168049**;
- mean peer turnout delta: **-0.182612**;
- median peer turnout delta: **-0.176106**;
- mean historical invalid-rate delta: **-0.042745**;
- median historical invalid-rate delta: **-0.038382**.

Counts that would appear extreme under a naive peer-z interpretation are correspondingly large:

- `|peer_turnout_z| >= 2`: **1,397** stations;
- `|peer_invalid_rate_z| >= 2`: **1,234** stations;
- `|turnout_invalid_interaction| >= 4`: **1,347** stations.

These counts are **not anomaly findings**. They demonstrate that the 2022 general election and 2025 early/by-election context are not directly interchangeable as a production anomaly reference without contextual normalization or a comparability gate.

## Methodological finding

Case 010 confirms an important design requirement: statistical mechanics alone are insufficient if the reference election context is not analytically comparable.

The engine therefore remains signal-only. Large deviations must not be interpreted as suspicious merely because they exceed a numerical threshold. A production layer must record election-context comparability before signal interpretation.

This is especially important here because the large majority of stations move in the same direction, indicating a broad election-level shift rather than isolated polling-station behavior.

## Result

**PASS WITH METHODOLOGICAL LIMITATION.**

The Historical Anomaly Engine v0.1 is mechanically valid for the implemented signals. The retrospective 2022 → 2025 run is suitable as a calculation and stress test, but not as substantive anomaly validation.

The next validation step should use the 2025 original election and the February 2026 repeat-election polling stations, where the election event, candidate field and affected polling stations are much more directly comparable. That test should be treated as the first substantive calibration case for the Historical Anomaly Engine.
