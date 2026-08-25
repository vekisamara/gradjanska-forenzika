# VALIDATION CASE 009 — Peer Group Engine 2022/2025 v0.1

Status: **READY FOR EXECUTION**

## Purpose

Validate `peer_group_engine_v0_1.py` against the first production Historical Baseline built from the 2022 and 2025 Republika Srpska presidential-election polling-station datasets.

This validation must confirm the mechanics of peer construction only. It must not interpret peer differences as anomalies or irregularities.

## Inputs

Historical Baseline input:

- 1,799 polling stations accepted by the conservative 2022 → 2025 mapping;
- two historical election observations per accepted station;
- Historical Baseline validation status: PASS.

Canonical election identity layer:

`2025-BIH-RS-PRES-BYELECTION-CONFIRMED`

Engine:

`peer_group_engine_v0_1.py` / v0.1.0

Default parameters:

- `min_peers = 5`
- `max_peers = 15`
- same-municipality candidates only
- political-result features excluded

## Expected invariants

The run passes only if all of the following hold:

1. exactly one `peer_groups.csv` row exists for every input baseline polling station;
2. no target polling station appears as its own peer;
3. every selected peer has the same municipality code as its target;
4. no peer is duplicated within one target neighborhood;
5. every `ok` group has at least 5 and at most 15 members;
6. every group with fewer than 5 valid same-municipality candidates is marked `insufficient_peer_group`;
7. every `peer_group_features.csv` row is derived only from selected peers and excludes the target station itself;
8. repeated runs with identical inputs and parameters produce identical membership ordering and numerical output except for the processing timestamp in the manifest;
9. no candidate, party or political-bloc variable is used in peer selection;
10. no anomaly score is produced.

## Required audit counts

After execution, record:

- input baseline station count;
- eligible feature station count;
- total peer-group count;
- `ok` group count;
- `insufficient_peer_group` count;
- membership row count;
- validation flag count by rule code;
- distribution of selected peer counts;
- municipality distribution of insufficient groups;
- median and maximum peer distance.

## Validation procedure

Run:

```bash
python3 peer_group_engine_v0_1.py \
  baseline_polling_stations.csv \
  historical_all_2022_2025.csv \
  --canonical-election-id 2025-BIH-RS-PRES-BYELECTION-CONFIRMED \
  --output ./peer-group-v0.1 \
  --min-peers 5 \
  --max-peers 15
```

Then verify invariants programmatically and inspect a small stratified sample covering:

- a large municipality;
- a medium municipality;
- a small municipality near the minimum peer threshold;
- a station with high historical turnout;
- a station with low historical turnout;
- a station with high invalid-ballot rate;
- a station with very small or very large registered-voter population.

## Pass criteria

**PASS** requires:

- zero error-severity validation flags;
- all structural invariants satisfied;
- deterministic rerun equality;
- no evidence that peer membership crosses municipality boundaries or includes the target itself.

Warnings for `insufficient_peer_group` are permitted and expected for small municipalities. They do not constitute failure.

## Interpretation boundary

A close or distant peer relationship is a structural comparison result only. It does not establish abnormality, manipulation, intent, fraud or illegality.

Final status must remain **READY FOR EXECUTION** until the output files are actually produced and audited. Do not convert this document to PASS based on expected behavior alone.
