# GFO Election Day Acquisition Profile v0.2

**Status:** WORKING SPECIFICATION  
**Parent:** GFO Election Data Standard v0.2-draft

## Purpose

This profile defines how a GFO-compatible ingestor may repeatedly acquire a changing election-results source during election day while preserving temporal meaning, provenance and source integrity.

## 1. Snapshot interval

A snapshot is an acquisition interval, not an instantaneous observation.

Every snapshot must record:

- `snapshot_id`
- `snapshot_started_at`
- `snapshot_completed_at`
- `retrieved_at`
- `completeness_status`

Individual source responses should additionally record `record_retrieved_at`.

If the source exposes its own timestamp such as CIK `dataFrom`, it is preserved separately as `source_data_from`.

## 2. Immutable acquisition

Every repeated ingest creates a new immutable snapshot.

A newer snapshot must never overwrite:

- RAW responses;
- normalized rows;
- provenance;
- validation findings;
- manifest of a previous snapshot.

A mutable `LATEST` pointer is permitted because it does not replace snapshot evidence.

## 3. Bounded parallelism

Parallel requests are permitted to reduce acquisition duration.

The implementation must use bounded concurrency. For the current CIK experimental adapter:

- default: `6` workers;
- recommended range: `4–8` workers;
- higher concurrency requires separate validation and must not be assumed safe for a public source.

Parallel acquisition must not imply that all records were observed at the same time.

`record_retrieved_at` remains mandatory/recommended at the record/API-response level even when multiple workers run concurrently.

## 4. Parallelization unit

For the current Race5 adapter, the preferred pattern is:

1. fetch electoral-unit list sequentially;
2. fetch polling-station list for one electoral unit;
3. fetch polling-station bundles concurrently within that electoral unit;
4. proceed to the next electoral unit.

A polling-station bundle contains at least:

- polling-station basic info;
- polling-station candidate results.

This bounds load while still eliminating most network wait time.

## 5. Retry policy

Transient request failures should be retried before a record is marked failed.

Reference defaults:

- retries after initial attempt: `3`;
- initial backoff: `1.0 s`;
- exponential sequence: approximately `1, 2, 4 ... s`;
- jitter: enabled;
- request timeout: `30 s`.

Retry metadata belongs in the snapshot manifest.

A failure after all retries must be preserved as a failed request and must affect snapshot completeness.

## 6. Completeness

Allowed statuses:

- `complete`
- `partial`
- `failed`
- `unknown`

A snapshot is `complete` only when all expected polling-station retrievals represented by successfully enumerated source lists have been acquired and there are no unresolved failed requests.

If an electoral-unit list or polling-station bundle fails after retries, the snapshot is `partial` unless no usable data were obtained, in which case it may be `failed`.

Partial snapshots must not generate disappearance/deletion conclusions in later delta analysis.

## 7. Expected counts

Where the source exposes a polling-station list, the ingestor should record:

- `expected_polling_station_count`
- `polling_station_count`
- `successful_request_count`
- `failed_request_count`

These fields permit later verification that a temporal snapshot is suitable for comparison.

## 8. Source-time handling

Source-native timestamps must be preserved without silently assigning semantics that the source has not documented.

For the CIK adapter, `dataFrom` is stored as `source_data_from`.

The manifest may record all distinct `source_data_from_values` seen during a snapshot.

`source_data_from_min` and `source_data_from_max` should only be populated when the adapter can safely parse the source timestamp as a chronological value. Otherwise the raw values remain preserved and min/max remain null.

## 9. Periodic/watch mode

A conforming implementation may support repeated snapshots at a configured interval.

The reference v0.2 ingestor interprets the interval as time between snapshot starts.

Example:

- configured interval: 30 min;
- acquisition duration: 4 min;
- wait before next snapshot: approximately 26 min.

This avoids temporal drift caused by adding a full interval after every completed ingest.

## 10. Separation from delta analysis

The acquisition component performs:

`ACQUIRE → PRESERVE → TIMESTAMP → NORMALIZE → VALIDATE`

It does not perform:

- anomaly scoring;
- political interpretation;
- fraud classification;
- causal inference.

A separate Snapshot Delta Engine compares two or more complete/comparable snapshots and produces DERIVED temporal changes.

## 11. Reference implementation

Reference implementation:

`ingest/cik_ingestor_v0_2.py`

Current experimental defaults:

- `workers=6`
- `retries=3`
- `backoff=1.0`
- `jitter=0.25`
- `timeout=30`
- `watch interval=1800 s`

These are implementation defaults, not universal requirements of the conceptual GFO Election Data Standard.
