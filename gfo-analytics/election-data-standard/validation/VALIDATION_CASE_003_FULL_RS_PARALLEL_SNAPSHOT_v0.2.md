# Validation Case 003 — Full RS Parallel Snapshot

**Standard target:** GFO Election Data Standard v0.2-draft  
**Ingestor under test:** `cik_ingestor_v0_2.py` v0.2.0  
**Date:** 2026-08-24  
**Status:** PASS WITH IMPLEMENTATION ISSUE

## Objective

Validate the first full Republic of Srpska immutable parallel snapshot against the previously validated sequential full-RS ingest and verify snapshot completeness, concurrency performance, temporal metadata and normalized-result equivalence.

## Snapshot under test

`snapshot-20260824T210101.198007Z-4e7b6f7a`

Manifest facts:

- snapshot started: `2026-08-24T21:01:01.198231+00:00`
- snapshot completed: `2026-08-24T21:02:46.791775+00:00`
- acquisition duration: approximately 105.6 seconds
- workers: 6
- polling stations: 2,164
- candidate-result rows: 12,984
- expected polling stations: 2,164
- successful requests: 4,393
- failed requests: 0
- validation flags reported by v0.2.0: 0
- completeness: `complete`
- dataset hash: `25c9835ea1fd0bcf566423ab8eeb44fc13f70d481610c85878084884b7505831`

Observed shell runtime supplied with the test:

- real: `1m45.762s`
- user: `0m44.113s`
- sys: `0m6.485s`

## Full-data reconciliation

The parallel snapshot contains:

- 64 electoral units
- 2,164 unique polling-station IDs
- 2,164 unique polling-station codes
- 6 unique candidate codes
- 1,234,714 registered voters
- 443,961 total votes
- 436,156 valid votes
- 7,805 invalid votes
- 436,156 summed candidate votes

The following invariants reconcile across the complete dataset:

- `valid_votes + invalid_votes == total_votes`
- sum of candidate votes equals total valid votes
- polling-station IDs are unique
- polling-station codes are unique
- candidate-result row count equals `2,164 × 6 = 12,984`

The normalized candidate-result table is value-equivalent to the prior sequential full-RS reference ingest for all shared candidate/result fields.

## Temporal/provenance validation

The snapshot records request-level `retrieved_at` values across approximately the same 105-second acquisition interval represented by the manifest. This confirms that v0.2 preserves observation time rather than representing the complete API crawl as an instantaneous event.

`previous_snapshot_id` is null, as expected for the first snapshot in this snapshot store.

## Implementation issue discovered: source metadata fallback

CIK Race5 exposes `location` and `dataFrom` in the polling-station list object returned by:

`race5_pollingstation/{dbName}/{electoralUnitId}/{languageId}`

The `race5_pollingstationsbasicinfo` object used by v0.2.0 does not contain those fields.

v0.2.0 attempted to normalize `location` and `source_data_from` only from the basic-info response. Consequently:

- `location` was null for all 2,164 normalized polling-station rows;
- `source_data_from` was null for all 2,164 normalized polling-station rows;
- the manifest therefore contained an empty `source_data_from_values` set.

The RAW source data remain intact, so this is a normalization implementation defect rather than data loss at the evidence layer.

## Corrective action

`cik_ingestor_v0_2_1.py` v0.2.1 was created to:

1. prefer `location`/`dataFrom` from basic-info when present;
2. fall back to the parent polling-station list object when basic-info omits them;
3. preserve polling-station `active` state;
4. add a warning validation rule if `source_data_from` is unexpectedly absent;
5. retain retry attempt counts in provenance.

## Validation conclusion

**PASS WITH IMPLEMENTATION ISSUE**

The core v0.2 architecture is validated for:

- bounded parallel acquisition;
- immutable snapshots;
- full-RS completeness accounting;
- request-level provenance timestamps;
- normalized electoral-result equivalence;
- zero failed requests;
- deterministic arithmetic validation.

The v0.2.0 normalizer must not be treated as final because it drops two source metadata fields from NORMALIZED output. This defect is corrected in v0.2.1.

## Next gate

Run one full-RS snapshot with `cik_ingestor_v0_2_1.py` and require:

- 2,164 polling stations;
- 12,984 candidate rows;
- 0 failed requests;
- 0 unexplained validation flags;
- non-null `location` for CIK records where supplied;
- populated `source_data_from` values matching RAW polling-station objects;
- normalized numeric/candidate values equivalent to the sequential reference dataset.

After that, perform a second v0.2.1 snapshot and run `snapshot_delta_v0_1.py` between the two snapshots to validate temporal-delta behavior on an unchanged source dataset.
