# GFO Election Data Standard v0.2 — Draft

**Version:** 0.2-draft  
**Status:** WORKING DRAFT  
**Date:** 2026-08-24  
**Role:** Canonical election-data interoperability standard for GFO Analytics

## 1. Purpose

GFO Election Data Standard defines a common, open and machine-readable structure for collecting, preserving, normalizing, exchanging and analyzing election data.

The standard does not determine whether an election result is regular, irregular, fraudulent or politically significant. Those conclusions belong to separate analytical modules.

Its role is to ensure that every analytical result can be traced back to data with known meaning, origin, transformation history and version.

## 2. Core processing model

The canonical processing chain is:

**RAW → NORMALIZED → DERIVED → INTERPRETED**

### RAW

Source data preserved in the form received from the source. RAW values are never silently corrected, overwritten or reformatted in place.

### NORMALIZED

Source data mapped into canonical GFO fields without changing its factual meaning. Normalization may rename fields, standardize types and join identifiers, but every transformation must be documented.

### DERIVED

Values produced deterministically or statistically from RAW or NORMALIZED data, such as turnout percentage, vote share, historical mean, standard deviation, swing or anomaly features.

### INTERPRETED

Human or LLM analytical conclusions produced from traceable evidence. INTERPRETED outputs must never overwrite RAW, NORMALIZED or DERIVED records.

## 3. Design principles

1. Preserve source evidence before transformation.
2. Keep calculation separate from interpretation.
3. Never equate missing data with zero.
4. Never silently repair source inconsistencies.
5. Every dataset and transformation must be reproducible.
6. Source-specific identifiers must remain distinguishable from canonical identifiers.
7. Revisions and repeated elections must be explicitly modeled.
8. A statistical anomaly is a signal for verification, not proof of misconduct.

## 4. Election entity

Required fields:

- `election_id`
- `election_date`
- `election_type`
- `jurisdiction`
- `authority`

New v0.2 relationship fields:

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

Candidate vote share may be source-provided or DERIVED. If source-provided, its provenance must be preserved. If recalculated, the derived field must identify the calculation module/version.

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

Live-election extensions:

- `timestamp`
- `voted_so_far`
- `source_id`

A source-provided turnout percentage must be distinguishable from a DERIVED turnout percentage calculated by GFO.

## 10. Source timestamps

v0.2 distinguishes at least four kinds of time:

1. `election_date` — when voting occurred;
2. `source_data_from` — timestamp embedded in the source dataset/object;
3. `published_at` — when the source published the information;
4. `retrieved_at` — when GFO obtained it.

These timestamps may differ and must not be substituted for one another.

## 11. Source and provenance

Every RAW object or file must support reconstruction of:

- source organization;
- source type;
- source URL/API endpoint;
- retrieval time;
- original format;
- SHA-256 hash;
- source dataset/version identifiers when available;
- transformation module and version when normalized;
- mapping configuration/version when source-specific field mapping is used.

For APIs, the exact endpoint used for every RAW artifact should be recorded.

## 12. Source-field mapping

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

## 13. Missing and exceptional values

The standard distinguishes:

- `0` — known numeric zero;
- `null` — unavailable/unknown value;
- `not_reported` — source did not provide a value;
- `not_applicable` — field does not apply;
- `source_placeholder` — source supplied a technically present but unusable placeholder value.

Normalization must not silently convert these states into each other.

## 14. Corrections and revisions

A newer value must not destroy an older captured value.

Revision-capable datasets should support:

- `record_version`
- `previous_record_id`
- `revision_timestamp`
- `revision_source`
- `revision_reason`, if known

This allows analysis of changes between preliminary, updated, determined and confirmed results.

## 15. Historical polling-station mapping

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

## 16. Validation as a first-class layer

Normalization does not imply validity.

Every ingest pipeline should produce a machine-readable validation artifact. Initial canonical checks include:

- `total_votes <= registered_voters`
- `valid_votes + invalid_votes == total_votes`, when definitions permit;
- `invalid_blank_ballots + invalid_other_ballots == invalid_votes`, when provided;
- sum of candidate votes `== valid_votes` for single-choice races when applicable;
- required IDs/codes present;
- duplicate polling-station codes detected;
- contradictory parent/child identifiers flagged;
- missing candidate/result records flagged.

Validation findings must contain at least:

- record identifier;
- validation rule code;
- severity;
- message;
- processing module/version.

A validation failure must not modify RAW data.

## 17. Machine-readable formats

Canonical interchange formats:

- JSON
- CSV

Recommended technical formats:

- JSON Schema for validation;
- Parquet for large analytical datasets.

XLS/XLSX may be accepted as source or user-input formats but should be normalized before analytical processing.

## 18. Reproducibility

Every DERIVED dataset must identify:

- input dataset ID/version;
- input hash where practical;
- processing module;
- processing module version;
- processing parameters/configuration;
- processing timestamp.

The same input, algorithm version and parameters must reproduce the same deterministic result.

## 19. LLM separation

LLMs are consumers of evidence packages, not custodians of canonical election data.

Canonical flow:

**RAW → NORMALIZED → VALIDATED → DERIVED → LLM INPUT PACKAGE → INTERPRETED**

LLM outputs must never overwrite prior layers.

## 20. Validation evidence incorporated into v0.2

This draft incorporates findings from:

- CIK 2025/2026 normalization test;
- Validation Case 001 — Novi Grad;
- real CIK Race5 API payloads for 52 polling stations and 312 candidate-result rows.

The real-source validation confirmed the architecture and exposed a concrete source-field mapping defect in ingestor v0.1, corrected in v0.1.1.

## 21. v0.2 status and next gates

v0.2 remains a draft until the following are completed:

1. rerun Novi Grad using ingestor v0.1.1;
2. require zero unexplained arithmetic validation flags;
3. ingest the complete Republic of Srpska confirmed-results dataset;
4. test duplicate/missing/placeholder handling across all electoral units;
5. update CSV Data Dictionary to v0.2;
6. split JSON Schema into entity-specific schemas;
7. define source-adapter metadata schema;
8. create at least one cross-election polling-station mapping test.

## 22. Core rule

**Data must remain distinguishable from calculation, calculation from validation, and validation from interpretation.**
