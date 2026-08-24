# Historical Baseline v0.1 — User Guide

## 1. Convert a validated snapshot into historical input

Example for the validated 2025 RS presidential by-election snapshot:

```bash
python3 baseline/snapshot_to_historical_input_v0_1.py \
  /path/to/SNAPSHOT_DIR \
  --election-id 2025-BIH-RS-PRES-BYELECTION-CONFIRMED \
  --election-date 2025-11-23 \
  --election-type president_rs \
  --source-id CIK-RACE5-RES39 \
  --output ./data/2025_historical_input.csv
```

The adapter intentionally leaves `political_bloc_id` empty. Cross-election bloc mapping must be created explicitly and must not be inferred from candidate names by the adapter.

## 2. Build one combined historical dataset

After converting/normalizing several elections, concatenate them while keeping one header:

```bash
(head -n 1 data/2022.csv && tail -n +2 data/2022.csv && tail -n +2 data/2025.csv) > data/historical_all.csv
```

For more than two cycles, append additional `tail -n +2` inputs.

## 3. Create mapping proposals

Choose a canonical election whose polling-station set will be the target identity layer.

```bash
python3 mapping/polling_station_mapping_engine_v0_1.py \
  data/historical_all.csv \
  data/historical_all.csv \
  --canonical-election-id 2025-BIH-RS-PRES-BYELECTION-CONFIRMED \
  --output ./mapping/proposals.csv
```

Review `proposals.csv` before analytical use. The helper only proposes exact code+municipality matches. Split/merge/renamed/uncertain cases require explicit review.

## 4. Freeze reviewed mapping

Create a reviewed file, e.g.:

`mapping/polling_station_mapping_reviewed_v0.1.csv`

Only rows with `usable_for_baseline=true` and adequate confidence will enter the default baseline calculation.

## 5. Build baseline

```bash
python3 baseline/baseline_engine_v0_1.py \
  data/historical_all.csv \
  mapping/polling_station_mapping_reviewed_v0.1.csv \
  --output ./output/baseline-v0.1 \
  --min-mapping-confidence 0.95 \
  --min-election-count 2
```

Outputs:

```text
baseline-v0.1/
├── baseline_manifest.json
├── baseline_polling_stations.csv
├── baseline_bloc_shares.csv
└── validation_flags.csv
```

## 6. Interpret outputs correctly

`baseline_polling_stations.csv` contains historical descriptive statistics only.

Example:

```text
turnout_mean = 0.623
turnout_std  = 0.041
```

This does not mean an anomaly exists. A later Historical Anomaly Engine will compare current observations against this baseline.

`baseline_bloc_shares.csv` is produced only where `political_bloc_id` was explicitly supplied for politically comparable elections.

## 7. Current development status

The code path and schemas are ready, but a production baseline requires additional historical CIK cycles to be ingested/normalized and an auditable polling-station mapping to be reviewed.

The already validated 2025/2026 CIK dataset can serve as the first real canonical input. It is not by itself sufficient to estimate historical variance.
