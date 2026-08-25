# GFO Election Analytics — Peer Group Specification v0.1

Status: **CURRENT DEVELOPMENT SPEC**

## 1. Purpose

Peer Group Engine builds a non-political reference neighborhood for each polling station. It complements the station's own historical baseline by answering a different question: how does this station compare with structurally similar stations in the same municipality?

The engine does **not** produce an anomaly score, fraud score, risk label or interpretation. It produces deterministic peer membership and descriptive peer-group features for later analytical modules.

Core rule: **a peer-group difference is a comparison signal, not evidence of irregularity.**

## 2. Inputs

Required inputs:

1. `baseline_polling_stations.csv` from Historical Baseline Engine v0.1;
2. canonical historical input containing polling-station metadata, normally `historical_all_*.csv`;
3. explicit `canonical_election_id` used to resolve municipality identity for the canonical polling-station code.

The baseline supplies structural features. The canonical historical input supplies municipality metadata.

## 3. Features used for peer similarity

v0.1 deliberately excludes candidate, party and political-bloc results.

Similarity features are:

- `log1p(registered_voters_mean)`;
- `turnout_mean`;
- `invalid_rate_mean`.

These features are standardized **within municipality** using robust location and scale:

- center = median;
- scale = median absolute deviation (MAD), converted by factor 1.4826;
- when MAD is zero or unavailable, population standard deviation is used;
- when both are zero/unavailable, scale falls back to 1.0 for that feature.

The distance between two stations is Euclidean distance in the standardized feature space.

## 4. Municipality boundary

Peer candidates must have the same `municipality_code` as the target polling station.

v0.1 does not automatically cross municipal boundaries. If a municipality does not provide enough valid peer candidates, the station receives `insufficient_peer_group` rather than being forced into a weak comparison group.

## 5. Per-station peer neighborhoods

Peer groups in v0.1 are target-specific nearest-neighbor neighborhoods rather than mutually exclusive clusters.

For each target station:

1. exclude the target itself;
2. restrict candidates to the same municipality;
3. require all three similarity features to be present;
4. calculate standardized Euclidean distance;
5. sort by `(distance, polling_station_code)` for deterministic tie-breaking;
6. retain up to `max_peers` nearest stations;
7. require at least `min_peers` members.

Defaults:

- `min_peers = 5`;
- `max_peers = 15`.

A station can be a peer of several target stations. This is expected.

## 6. Outputs

### `peer_group_membership.csv`

One row per target/member relationship:

- `peer_group_id`
- `target_polling_station_code`
- `peer_polling_station_code`
- `municipality_code`
- `peer_rank`
- `distance`
- `membership_confidence`

`peer_group_id` is deterministic: `PG-<target_polling_station_code>`.

`membership_confidence` is a monotonic convenience transform of distance:

`1 / (1 + distance)`

It is not a probability.

### `peer_groups.csv`

One row per target polling station:

- group identity;
- status (`ok` or `insufficient_peer_group`);
- municipality;
- available candidate count;
- selected peer count;
- minimum/mean/maximum peer distance.

### `peer_group_features.csv`

Descriptive distribution of the selected peers, excluding the target itself:

- registered-voter mean/std;
- turnout mean/std/min/max;
- invalid-rate mean/std/min/max;
- valid-vote-rate mean/std where available.

### `peer_group_validation_flags.csv`

Machine-readable validation findings.

### `peer_group_manifest.json`

Input hashes, module version, parameters and output counts.

## 7. Validation rules

- `GFO-PG-V001`: duplicate canonical polling-station code in baseline input — error.
- `GFO-PG-V002`: missing canonical municipality metadata — warning; station cannot receive peers.
- `GFO-PG-V003`: missing required similarity feature — warning; station cannot receive peers.
- `GFO-PG-V004`: self-membership detected — error.
- `GFO-PG-V005`: peer from a different municipality — error.
- `GFO-PG-V006`: duplicate peer member in one target group — error.
- `GFO-PG-V007`: fewer than `min_peers` valid candidates — warning / `insufficient_peer_group`.
- `GFO-PG-V008`: selected peer count exceeds `max_peers` — error.

## 8. Explicit exclusions in v0.1

v0.1 does not use:

- candidate or party vote share;
- political-bloc identity;
- geographic coordinates;
- urban/rural classification unless later supplied as independently validated metadata;
- machine-learning clustering;
- anomaly thresholds or composite scores.

These exclusions are deliberate to prevent political circularity and opaque grouping.

## 9. Downstream use

Historical Anomaly Engine may later compare a current or historical polling-station observation with:

1. the station's own historical baseline;
2. the station's peer-group distribution.

The two signals must remain separate in v0.1 of the anomaly layer. A later composite score, if ever introduced, requires separate calibration and validation.
