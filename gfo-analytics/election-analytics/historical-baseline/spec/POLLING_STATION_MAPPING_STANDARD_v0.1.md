# Polling Station Mapping Standard v0.1

## Purpose

Map historical polling stations to a canonical/current polling-station identity before any cross-election baseline is calculated.

## Canonical mapping file

Required columns:

- `canonical_polling_station_code`
- `historical_election_id`
- `historical_polling_station_code`
- `mapping_type`
- `mapping_confidence`
- `usable_for_baseline`
- `mapping_source`

Recommended:

- `historical_polling_station_name`
- `canonical_polling_station_name`
- `municipality_code`
- `registered_voters_historical`
- `registered_voters_canonical`
- `notes`
- `reviewed_by`
- `reviewed_at`

## Mapping types

- `exact_verified`
- `exact_code_unverified`
- `renamed_verified`
- `boundary_changed`
- `split`
- `merged`
- `manual_verified`
- `uncertain`
- `unmapped`

## Automatic rule v0.1

The helper may propose an `exact_code_unverified` mapping only when:

1. historical and canonical polling-station codes are identical;
2. municipality codes are identical;
3. no duplicate candidate target exists for that historical record.

It may increase proposal confidence when names normalize identically and registered-voter counts are reasonably close, but it must not silently promote a proposal to `exact_verified`.

## Unsafe automatic cases

The engine must not automatically resolve:

- one historical BM mapping to several current BM;
- several historical BM mapping to one current BM;
- changed codes with only similar names;
- large registered-voter population changes;
- known split/merge/boundary changes.

These require explicit review or a later specialized reconstruction methodology.

## Baseline eligibility

Default v0.1 baseline requirements:

- `usable_for_baseline = true`
- `mapping_confidence >= 0.95`
- mapping type not in `split`, `merged`, `boundary_changed`, `uncertain`, `unmapped`

## Registered-voter drift

Registered-voter change is a diagnostic, not automatic proof of changed boundaries.

The mapping helper calculates:

`registered_voter_change_pct = (canonical - historical) / historical * 100`

A large change should lower confidence and trigger review, but thresholds belong to the mapping implementation/configuration, not to the core Election Data Standard.

## Audit requirement

Every accepted mapping must remain traceable to either:

- official source evidence;
- deterministic exact-code rule plus metadata;
- explicit manual review.

No fuzzy-name match may enter the analytical baseline without an auditable mapping record.
