# Validation Case 004 — Full RS Snapshot v0.2.1

**Standard target:** GFO Election Data Standard v0.2-draft  
**Ingestor under test:** `cik_ingestor_v0_2_1.py` v0.2.1  
**Date:** 2026-08-24  
**Status:** PASS

## Objective

Validate the corrected full Republic of Srpska immutable parallel snapshot after the v0.2.0 metadata-fallback defect was fixed in v0.2.1.

## Snapshot under test

`snapshot-20260824T211109.700647Z-86d66893`

Manifest facts:

- snapshot started: `2026-08-24T21:11:09.700805+00:00`
- snapshot completed: `2026-08-24T21:13:01.683890+00:00`
- acquisition duration: approximately 112.0 seconds
- workers: 6
- polling stations: 2,164
- candidate-result rows: 12,984
- expected polling stations: 2,164
- successful requests: 4,393
- failed requests: 0
- validation flags: 0
- completeness: `complete`
- dataset hash: `b96ed24cc92a96cb925dc654d55facac7ab225349ad736fe30d80a2eea7de6ae`

## Full-data reconciliation

The normalized snapshot contains:

- 2,164 polling stations
- 12,984 candidate-result rows
- 1,234,714 registered voters
- 443,961 total votes
- 436,156 valid votes
- 7,805 invalid votes
- 436,156 summed candidate votes

The following invariants reconcile across the complete dataset:

- `valid_votes + invalid_votes == total_votes`
- sum of candidate votes equals total valid votes
- polling-station codes are unique
- candidate-result row count equals `2,164 × 6 = 12,984`

The normalized numeric and candidate values are equivalent to the prior sequential full-RS reference ingest.

## Metadata correction validation

The v0.2.1 fallback correction is confirmed:

- `location` is populated for 2,164 / 2,164 polling-station rows;
- `source_data_from` is populated for 2,164 / 2,164 polling-station rows;
- `active` is populated for 2,164 / 2,164 polling-station rows;
- `record_retrieved_at` is populated for 2,164 / 2,164 polling-station rows;
- `snapshot_id` is populated for 2,164 / 2,164 polling-station rows.

All polling-station rows report the same source state timestamp:

`2026-02-13T11:42:19.57`

The manifest correctly records:

- `source_data_from_values = ["2026-02-13T11:42:19.57"]`
- `source_data_from_min = "2026-02-13T11:42:19.57"`
- `source_data_from_max = "2026-02-13T11:42:19.57"`

## Temporal/provenance validation

The acquisition spans approximately 112 seconds, while record-level `record_retrieved_at` values are preserved. This confirms that the source state timestamp and GFO observation time remain distinguishable.

The snapshot is complete and contains no failed requests, so it is suitable as a valid comparison input for the Snapshot Delta Engine.

## Validation conclusion

**PASS**

`cik_ingestor_v0_2_1.py` is validated for this CIK Race5 full-RS source on:

- bounded parallel acquisition;
- immutable snapshot creation;
- full-dataset completeness;
- request-level temporal provenance;
- correct location/source timestamp fallback;
- normalized-result equivalence;
- zero failed requests;
- zero unexplained validation flags.

## Next gate

Create a second complete v0.2.1 snapshot of the same source and compare the two with `snapshot_delta_v0_1.py`.

For an unchanged source dataset, the expected result is:

- zero numeric/candidate deltas;
- zero revision events;
- different GFO retrieval timestamps are not treated as result changes;
- identical `source_data_from` values are preserved as evidence that both snapshots represent the same CIK source state.
