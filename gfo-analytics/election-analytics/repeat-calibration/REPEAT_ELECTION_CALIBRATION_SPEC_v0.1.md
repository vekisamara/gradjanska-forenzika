# Repeat Election Calibration v0.1

Purpose: calibrate Historical Anomaly signals against the 2025 RS presidential by-election stations on which CIK annulled the 23 Nov 2025 vote and ordered repeat voting on 8 Feb 2026.

The calibration unit is the polling station. The official target universe is exactly 136 stations in 17 electoral units. The comparison is descriptive and evidentiary: original observation → repeat observation. A change is not, by itself, proof of manipulation, fraud, intent or illegality.

## Required inputs

1. `repeat_136_polling_stations_v0.1.csv` — official repeat-station universe.
2. `original_136_station_results.csv` — preserved station-level results from the 23 Nov 2025 election before replacement/annulment.
3. `repeat_136_final_station_results_v0.1.csv` — final confirmed station-level observations after repeat voting.

## Core outputs

- turnout delta
- total/valid/invalid ballot deltas
- invalid-rate delta
- registered-voter consistency check
- validation flags

Candidate-level swing is a second-stage calibration once an original pre-repeat candidate table is acquired.

## Comparability rule

The repeat election is a high-value calibration case because CIK states that the repeat election used the same candidate lists and the same extracts from the Central Voters Register as the annulled election. This makes the pair substantially more comparable than 2022 general election vs 2025 by-election comparisons.

## Interpretation boundary

The engine never emits a composite anomaly score or a fraud label. It only measures change and exposes the evidence needed for later calibration analysis.
