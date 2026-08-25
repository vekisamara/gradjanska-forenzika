# VALIDATION CASE 009 — Peer Group Engine 2022/2025 v0.1

Status: **PASS WITH EXPECTED WARNINGS**

## Purpose

Validate `peer_group_engine_v0_1.py` against the first production Historical Baseline built from the 2022 and 2025 Republika Srpska presidential-election polling-station datasets.

This validation confirms the mechanics of peer construction only. Peer distance is a structural comparison result and is not interpreted as evidence of anomaly, irregularity, manipulation, intent, fraud or illegality.

## Inputs

Historical Baseline input:

- 1,799 polling stations accepted by the conservative 2022 → 2025 mapping;
- two historical election observations per accepted station;
- Historical Baseline validation status: PASS.

Canonical election identity layer:

`2025-BIH-RS-PRES-BYELECTION-CONFIRMED`

Engine:

`peer_group_engine_v0_1.py` / v0.1.0

Parameters:

- `min_peers = 5`
- `max_peers = 15`
- same-municipality candidates only
- political-result features excluded

## Execution result

Primary run:

- input baseline polling stations: **1,799**;
- peer-group rows: **1,799**;
- `ok` peer groups: **1,765**;
- `insufficient_peer_group`: **34**;
- membership rows: **25,506**;
- validation flags: **34**;
- error-severity flags: **0**;
- warning-severity flags: **34**.

All 34 warnings are `GFO-PG-V007` and correspond to targets with fewer than five valid same-municipality peer candidates. This is expected behavior and is not a validation failure.

## Structural invariant audit

All required invariants passed:

1. exactly one `peer_groups.csv` row exists for every one of the 1,799 input baseline polling stations;
2. self-peer memberships: **0**;
3. cross-municipality memberships: **0**;
4. duplicate peer members within a target group: **0**;
5. every `ok` group contains between 5 and 15 selected peers;
6. all groups with fewer than five valid same-municipality candidates are marked `insufficient_peer_group`;
7. peer-group feature rows are derived from selected peers and exclude the target station;
8. no political candidate, party or bloc variable is used in peer selection;
9. no anomaly score is produced.

## Determinism test

The engine was executed twice with identical inputs and parameters.

The following output files were byte-identical across both runs:

- `peer_groups.csv` — SHA-256 `19dc0bed2b6a329639b650fce3fc1ec14f970095a1f29b639fdb665221f7860b`;
- `peer_group_membership.csv` — SHA-256 `4e32104691fc1d690612ffa4d80a8a419691b4ce49a52f6865fd8703fdbec267`;
- `peer_group_features.csv` — SHA-256 `93770466dc40a2169d2a2e0f1331d27a9cbc93f6dac370054a88ec6fd1a7cb33`;
- `peer_group_validation_flags.csv` — SHA-256 `15360e0549654a11a9da35e5c916cc5dc00de94460ba55e1ddc9316b4582e143`.

The manifest processing timestamp is intentionally excluded from byte-for-byte equality.

## Selected-peer-count distribution

Among the 1,765 `ok` groups:

- 5 peers: 12 groups;
- 6 peers: 28 groups;
- 7 peers: 16 groups;
- 8 peers: 9 groups;
- 9 peers: 20 groups;
- 10 peers: 33 groups;
- 12 peers: 26 groups;
- 13 peers: 14 groups;
- 14 peers: 15 groups;
- 15 peers: 1,592 groups.

The absence of an 11-peer category is a property of the municipality-size distribution in this input, not an engine constraint.

## Insufficient-peer distribution

The 34 `insufficient_peer_group` targets are concentrated in small municipalities. Counts by municipality code:

- 168: 5;
- 006: 4;
- 138: 4;
- 023: 4;
- 121: 4;
- 142: 3;
- 179: 3;
- 031: 2;
- 066: 2;
- 058: 1;
- 108: 1;
- 158: 1.

These targets are correctly withheld from peer-based comparison rather than being assigned cross-municipality substitutes.

## Peer-distance audit

Across all 25,506 selected peer memberships:

- mean distance: **1.598296**;
- median distance: **1.219110**;
- 75th percentile: **1.910907**;
- minimum distance: **0.044005**;
- maximum distance: **33.021661**.

The large maximum distance is not a structural validation failure, because v0.1 deliberately selects the nearest same-municipality peers whenever the municipality satisfies the minimum-size rule. However, it identifies an important quality-control issue for the next iteration: extreme feature profiles can have technically valid but substantively distant peers.

Before peer distance is used by the Historical Anomaly Engine, a distance-quality layer should therefore be added or explicitly accounted for, for example through a maximum-distance threshold, low-confidence status, or distance-aware weighting. This must not be converted into an anomaly claim by itself.

## Stratified manual inspection

A sample was inspected covering large, medium and small municipalities and extreme baseline profiles.

Examples:

- large municipality target `034B001`: 15 same-municipality peers, no self-membership;
- medium municipality target `170B001`: 15 same-municipality peers;
- small municipality target `169B001`: 5 peers, exactly the minimum accepted size;
- high-turnout target `038B068`: 15 peers;
- low-turnout target `074B028`: 15 peers;
- high-invalid-rate target `105B019`: peers are structurally valid but very distant, confirming the distance-quality concern above;
- very small registered-voter target `026B009`: 10 peers;
- very large registered-voter target `014B036`: 15 peers.

No sampled case violated municipality, self-membership or duplicate-member constraints.

## Result

**PASS WITH EXPECTED WARNINGS.**

The Peer Group Engine v0.1 is structurally valid and deterministic on the 2022/2025 Historical Baseline. The 34 warnings are expected small-municipality exclusions and demonstrate conservative behavior.

The engine is suitable to proceed to Historical Anomaly Engine development, provided peer-distance quality is retained as an explicit limitation. Peer-based anomaly logic must not treat every technically valid peer group as equally strong evidence where peer distances are large.