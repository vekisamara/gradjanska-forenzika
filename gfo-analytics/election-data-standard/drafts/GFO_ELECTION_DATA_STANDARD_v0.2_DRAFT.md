# GFO Election Data Standard v0.2 — Draft

**Version:** 0.2-draft  
**Status:** WORKING DRAFT  
**Date:** 2026-08-24  
**Role:** Canonical election-data interoperability standard for GFO Analytics

## 1. Purpose

GFO Election Data Standard defines a common, open and machine-readable structure for collecting, preserving, normalizing, exchanging and analyzing election data.

The standard does not determine whether an election result is regular, irregular, fraudulent or politically significant. Those conclusions belong to separate analytical modules.

Its role is to ensure that every analytical result can be traced back to data with known meaning, origin, transformation history, temporal state and version.

## 2. Core processing model

The canonical processing chain is:

**RAW → NORMALIZED → VALIDATED → DERIVED → INTERPRETED**

### RAW

Source data preserved in the form received from the source. RAW values are never silently corrected, overwritten or reformatted in place.

### NORMALIZED

Source data mapped into canonical GFO fields without changing its factual meaning. Normalization may rename fields, standardize types and join identifiers, but every transformation must be documented.

### VALIDATED

Machine-readable checks of consistency, completeness and source/identifier integrity. Validation findings do not modify RAW data and do not themselves constitute analytical interpretation.

### DERIVED

Values produced deterministically or statistically from RAW or NORMALIZED data, such as turnout percentage, vote share, historical mean, standard deviation, swing, snapshot delta or anomaly features.

### INTERPRETED

Human or LLM analytical conclusions produced from traceable evidence. INTERPRETED outputs must never overwrite RAW, NORMALIZED, VALIDATED or DERIVED records.

## 3. Design principles

1. Preserve source evidence before transformation.
2. Keep calculation separate from interpretation.
3. Never equate missing data with zero.
4. Never silently repair source inconsistencies.
5. Every dataset and transformation must be reproducible.
6. Source-specific identifiers must remain distinguishable from canonical identifiers.
7. Revisions and repeated elections must be explicitly modeled.
8. A statistical anomaly is a signal for verification, not proof of misconduct.
9. Repeated retrievals of a changing source are immutable temporal observations, not replacements for earlier data.
10. Temporal comparison is valid only when snapshot completeness and observation times are known.

## 4. Election entity

Required fields:

- `election_id`
- `election_date`
- `election_type`
- `jurisdiction`
- `authority`

v0.2 relationship fields:

- `parent_election_id` — related earlier election event, when applicable;
- `event_relation` — controlled values such as `original`, `repeat`, `partial_repeat`, `postponed`, `rerun`, `correction`;
- `results_determined_at` — timestamp when results were formally determined, if available;
- `results_confirmed_at` — timestamp when results were confirmed, if available;
- `published_at` — source publication timestamp, if available.

Election date and result publication/confirmation times must not be collapsed into one timestamp.

## 5. Electoral Unit entity

v0.2 introduces an explicit electoral-unit entity because source APIs may use internal IDs that differ from official public codes.

Fields:

- `election_id`
- `electoral_unit_id` — source or canonical internal identifier;
- `electoral_unit_code` — official code, where available;
- `electoral_unit_name`
- `source_data_from`
- `active`

## 6. Polling Station entity

Required canonical fields:

- `election_id`
- `polling_station_id`
- `polling_station_code`
- `electoral_unit_id`
- `municipality_code`
- `polling_station_name`
- `registered_voters`

Optional fields:

- `location`
- `address`
- `latitude`
- `longitude`
- `active`
- `source_data_from`

### Identifier rule

`polling_station_id` and `polling_station_code` are distinct concepts.

A source may expose an internal numeric ID and a stable public code such as `007B001`. Both must be preserved where available.

If a child API response contains a placeholder or contradictory identifier, it must not overwrite a validated identifier inherited from the parent request/object. The inconsistency must be recorded as a validation finding.

## 7. Candidate entity

Required fields:

- `election_id`
- `candidate_id`
- `candidate_name`

v0.2 adds:

- `candidate_code` — official/source candidate code when available;
- `party_id` — optional normalized political-subject identifier;
- `party_name` — optional source-provided party/coalition name;
- `political_bloc_id` — optional historical analytical mapping.

`candidate_code` must remain distinct from any later GFO cross-election identifier.

## 8. Result entity

Required fields:

- `election_id`
- `polling_station_id`
- `candidate_id`
- `votes`

Optional fields:

- `candidate_code`
- `vote_percentage`
- `source_data_from`
- `snapshot_id`
- `record_retrieved_at`

Candidate vote share may be source-provided or DERIVED. If source-provided, its provenance must be preserved. If recalculated, the derived field must identify the calculation module/version.

For live or periodically updated sources, each normalized result record must remain traceable to the snapshot and RAW response from which it was produced.

## 9. Turnout entity

Required final-result fields:

- `election_id`
- `polling_station_id`
- `registered_voters`
- `total_votes`

Optional fields:

- `valid_votes`
- `invalid_votes`
- `invalid_blank_ballots`
- `invalid_other_ballots`
- `turnout_percentage`
- `number_candidates`
- `source_data_from`
- `snapshot_id`
- `record_retrieved_at`

Live-election extensions:

- `timestamp`
- `voted_so_far`
- `source_id`

A source-provided turnout percentage must be distinguishable from a DERIVED turnout percentage calculated by GFO.

## 10. Temporal model and source timestamps

v0.2 distinguishes at least these kinds of time:

1. `election_date` — when voting occurred;
2. `source_data_from` — timestamp embedded in the source dataset/object and describing the source's own data state where that meaning is supported;
3. `published_at` — when the source published the information;
4. `retrieved_at` — when GFO obtained a source object or dataset;
5. `snapshot_started_at` — when a multi-request snapshot acquisition began;
6. `snapshot_completed_at` — when that acquisition completed;
7. `record_retrieved_at` — when a particular API response/record was observed by GFO.

These timestamps may differ and must not be substituted for one another.

A full API ingest can span several minutes. Therefore a snapshot must not be treated as if every record were observed at exactly the same instant. Record-level retrieval time and source-provided time should be preserved where practical.

## 11. Snapshot entity

v0.2 introduces `Snapshot` as a first-class entity for sources that may change over time, including election-night APIs.

Required fields:

- `snapshot_id` — globally unique immutable identifier;
- `election_id`;
- `source_id`;
- `snapshot_started_at`;
- `snapshot_completed_at`;
- `retrieved_at` — canonical retrieval timestamp for the snapshot manifest;
- `completeness_status`;
- `record_count`;
- `dataset_hash` or manifest hash where practical.

Recommended fields:

- `previous_snapshot_id`;
- `source_data_from_min`;
- `source_data_from_max`;
- `expected_record_count`;
- `successful_request_count`;
- `failed_request_count`;
- `ingestor_version`;
- `adapter_version`;
- `notes`.

Controlled `completeness_status` values:

- `complete`
- `partial`
- `failed`
- `unknown`

A snapshot marked `partial`, `failed` or `unknown` must not be compared to another snapshot as if missing records represented deletions from the source.

## 12. Immutable snapshot rule

A repeated ingest must create a new snapshot. It must never overwrite a prior snapshot directory, manifest or normalized observation.

Recommended RAW layout:

```text
raw/
  snapshots/
    <snapshot_id>/
      manifest.json
      electoral_units.json
      polling_stations_eu_*.json
      polling_station_*_basic.json
      polling_station_*_candidates.json
```

The exact storage layout is implementation-specific, but immutability and traceability are mandatory.

If two consecutive snapshots are byte-identical, both observations may still be retained. Storage optimization may deduplicate identical blobs by hash only if the observation metadata for each retrieval remains independently preserved.

## 13. Source and provenance

Every RAW object or file must support reconstruction of:

- source organization;
- source type;
- source URL/API endpoint;
- retrieval time;
- snapshot identifier where applicable;
- original format;
- SHA-256 hash;
- source dataset/version identifiers when available;
- transformation module and version when normalized;
- mapping configuration/version when source-specific field mapping is used.

For APIs, the exact endpoint used for every RAW artifact should be recorded.

For temporal sources, provenance should also preserve `record_retrieved_at` and source-provided `source_data_from` where available.

## 14. Source-field mapping

v0.2 formalizes a source adapter layer.

A source adapter maps source-native fields to canonical GFO fields. Example from CIK BiH Race5 validation:

- `pollingStationId` → `polling_station_id`
- `code` (polling station) → `polling_station_code`
- `location` → `location`
- `dataFrom` → `source_data_from`
- `numberOfVoters` → `registered_voters`
- `totalVotes` (basic info) → `total_votes`
- `percentageTotalVotes` → `turnout_percentage`
- `validVotes` → `valid_votes`
- `totalInvalidVotes` → `invalid_votes`
- candidate `code` → `candidate_code`
- candidate `name` → `candidate_name`
- candidate `totalVotes` → `votes`
- candidate `percentage` → `vote_percentage`

Source adapters are implementation artifacts and must be versioned independently from the conceptual standard.

`dataFrom` must not be assumed to mean retrieval time. Its semantics are source-specific and should be documented by the adapter when known.

## 15. Missing and exceptional values

The standard distinguishes:

- `0` — known numeric zero;
- `null` — unavailable/unknown value;
- `not_reported` — source did not provide a value;
- `not_applicable` — field does not apply;
- `source_placeholder` — source supplied a technically present but unusable placeholder value.

Normalization must not silently convert these states into each other.

## 16. Corrections, revisions and temporal observations

A newer value must not destroy an older captured value.

The standard distinguishes two related concepts:

### Source revision

A source changes a value that GFO previously observed for the same logical record.

### GFO observation

A new retrieval captures the source state at a later time, regardless of whether any values changed.

Revision-capable datasets should support:

- `record_version`
- `previous_record_id`
- `revision_timestamp`
- `revision_source`
- `revision_reason`, if known
- `snapshot_id`

A detected change is evidence that the published/source-visible value changed between observations. It is not, by itself, evidence of error, manipulation or electoral misconduct.

## 17. Snapshot delta dataset

Temporal comparison belongs to the DERIVED layer.

A canonical `snapshot_delta` record should contain at least:

- `election_id`
- `polling_station_id`
- `field_name` or `candidate_id`
- `snapshot_from`
- `snapshot_to`
- `value_from`
- `value_to`
- `delta`
- `source_data_from_from`, where available;
- `source_data_from_to`, where available;
- `comparison_status`;
- `processing_module`;
- `processing_module_version`.

Recommended `comparison_status` values:

- `comparable`
- `partial_snapshot`
- `record_missing_from_source`
- `new_record`
- `source_time_incomparable`
- `not_comparable`

A delta engine must not interpret a missing record in a partial snapshot as a zero value.

## 18. Revision event taxonomy

Analytical modules may derive revision events from snapshot deltas. Initial event types include:

- `candidate_vote_increase`
- `candidate_vote_decrease`
- `large_candidate_vote_change`
- `vote_reallocation_pattern`
- `turnout_revision`
- `valid_invalid_revision`
- `registered_voter_revision`
- `result_appeared`
- `result_disappeared`
- `polling_station_appeared`
- `polling_station_disappeared`
- `status_revision`

These are descriptive event labels, not findings of wrongdoing.

Thresholds for `large_*`, severity and anomaly scoring belong to analytical modules, not to this Data Standard.

## 19. Historical polling-station mapping

Cross-election comparison requires explicit mapping because polling-station codes, boundaries or voter populations may change.

Recommended mapping fields:

- `current_polling_station_id`
- `current_polling_station_code`
- `historical_polling_station_id`
- `historical_polling_station_code`
- `election_id`
- `mapping_type`
- `mapping_confidence`
- `mapping_source`

Historical comparison must not assume that equal or similar names imply equivalent polling-station populations.

## 20. Validation as a first-class layer

Normalization does not imply validity.

Every ingest pipeline should produce a machine-readable validation artifact. Initial canonical checks include:

- `total_votes <= registered_voters`
- `valid_votes + invalid_votes == total_votes`, when definitions permit;
- `invalid_blank_ballots + invalid_other_ballots == invalid_votes`, when provided;
- sum of candidate votes `== valid_votes` for single-choice races when applicable;
- required IDs/codes present;
- duplicate polling-station codes detected;
- contradictory parent/child identifiers flagged;
- missing candidate/result records flagged;
- snapshot identifier uniqueness;
- `snapshot_started_at <= snapshot_completed_at`;
- no prior snapshot overwritten;
- completeness status consistent with request/record counts;
- record timestamps falling within or being explainable relative to snapshot acquisition;
- source-time regressions flagged where meaningful for that source adapter.

Validation findings must contain at least:

- record identifier;
- validation rule code;
- severity;
- message;
- processing module/version.

A validation failure must not modify RAW data.

## 21. Temporal anomaly separation

The Data Standard permits temporal features to be calculated but does not decide whether they are anomalous.

Three analytical dimensions should remain distinguishable downstream:

- `historical` — comparison with previous elections;
- `spatial_peer` — comparison with other relevant polling stations;
- `temporal` — comparison between successive observations/snapshots of the same election.

Examples such as a candidate vote decrease, large increase, turnout revision or result disappearance are inputs to a Temporal Anomaly Engine. Their weights, thresholds and explanations belong to the Election Analytics methodology.

## 22. Machine-readable formats

Canonical interchange formats:

- JSON
- CSV

Recommended technical formats:

- JSON Schema for validation;
- Parquet for large analytical datasets.

XLS/XLSX may be accepted as source or user-input formats but should be normalized before analytical processing.

## 23. Reproducibility

Every DERIVED dataset must identify:

- input dataset ID/version or snapshot IDs;
- input hash where practical;
- processing module;
- processing module version;
- processing parameters/configuration;
- processing timestamp.

The same input, algorithm version and parameters must reproduce the same deterministic result.

For temporal analyses, the exact ordered set of snapshots used must be recorded.

## 24. LLM separation

LLMs are consumers of evidence packages, not custodians of canonical election data.

Canonical flow:

**RAW SNAPSHOTS → NORMALIZED → VALIDATED → DERIVED DELTAS/FEATURES → LLM INPUT PACKAGE → INTERPRETED**

LLM outputs must never overwrite prior layers.

An LLM must be able to distinguish source values from GFO-derived deltas and from analytical anomaly classifications.

## 25. Election-day acquisition profile

A conforming election-day ingestor should support repeated acquisition at a configured interval or via an external scheduler.

The acquisition component is responsible only for:

1. retrieving source data;
2. preserving immutable RAW responses;
3. recording temporal/provenance metadata;
4. normalizing source fields;
5. producing validation findings.

It should not assign anomaly severity or infer causes.

A separate delta/analytics component compares snapshots.

Recommended conceptual separation:

```text
CIK/API/source
    ↓
Snapshot Ingestor
    ↓
Immutable Snapshot Store
    ↓
Normalization + Validation
    ↓
Snapshot Delta Engine
    ↓
Historical / Spatial / Temporal Analytics
    ↓
LLM Evidence Package
```

## 26. Validation evidence incorporated into v0.2

This draft incorporates findings from:

- CIK 2025/2026 normalization test;
- Validation Case 001 — Novi Grad;
- real CIK Race5 API payloads for 52 polling stations and 312 candidate-result rows;
- successful Novi Grad rerun with ingestor v0.1.1 and zero unexplained validation flags;
- design review for repeated election-day CIK/API snapshots and electronic-counting update scenarios.

The real-source validation confirmed the architecture and exposed a concrete source-field mapping defect in ingestor v0.1, corrected in v0.1.1.

## 27. v0.2 status and next gates

v0.2 remains a draft until the following are completed:

1. ingest the complete Republic of Srpska confirmed-results dataset;
2. test duplicate/missing/placeholder handling across all electoral units;
3. update CSV Data Dictionary to v0.2, including Snapshot and temporal fields;
4. split JSON Schema into entity-specific schemas;
5. define source-adapter metadata schema;
6. create at least one cross-election polling-station mapping test;
7. implement and validate immutable snapshot acquisition;
8. implement a deterministic Snapshot Delta Engine;
9. test at least two successive snapshots, including a controlled changed-value fixture;
10. verify that partial snapshots cannot generate false disappearance/deletion events.

## 28. Core rule

**Data must remain distinguishable from observation time, calculation from validation, and validation from interpretation. A newer observation must never erase an older one.**
