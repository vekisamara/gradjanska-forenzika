# Validation Case 005 — Unchanged Snapshot Delta

**Standard target:** GFO Election Data Standard v0.2-draft  
**Snapshot ingestor:** `cik_ingestor_v0_2_1.py` v0.2.1  
**Delta engine under test:** `snapshot_delta_v0_1.py` v0.1.0  
**Date:** 2026-08-24  
**Status:** PASS

## Objective

Verify that two separately acquired complete snapshots of an unchanged CIK Race5 dataset do not generate false revision events merely because their GFO acquisition timestamps, snapshot IDs and request-level retrieval timestamps differ.

## Snapshot pair

- `snapshot-20260824T211109.700647Z-86d66893`
- `snapshot-20260824T211536.942059Z-01efb8c5`

Both snapshots were produced with `cik_ingestor_v0_2_1.py` and represent the same confirmed Republic of Srpska presidential-result dataset.

## Observed result

The delta engine reported:

- comparison status: `comparable`
- delta rows written: `28,132`
- revision events: `0`

The 28,132 rows are full comparison rows, not 28,132 changes. They consist of:

- `2,164 polling stations × 7 station numeric fields = 15,148 comparisons`
- `2,164 polling stations × 6 candidate vote records = 12,984 comparisons`
- total: `28,132 compared values`

No compared substantive value changed between the snapshots.

## Validation conclusion

**PASS**

The temporal pipeline correctly distinguishes observation metadata from election-result content. Different `snapshot_id`, `snapshot_started_at`, `snapshot_completed_at` and `record_retrieved_at` values did not produce false revision events.

This validates the specificity side of temporal comparison on an unchanged source dataset.

## Usability finding

The v0.1.0 console label `Delta rows: 28132` can be misread as a count of changed values even though zero-delta comparison rows are included for auditability.

Corrective implementation: `snapshot_delta_v0_1_1.py` v0.1.1 introduces separate metrics:

- `Compared values`
- `Changed values`
- `Revision events`
- `Written delta rows`

and adds `--changes-only` to write only substantive changes while retaining full-comparison mode as the default audit mode.

## Next gate

Run v0.1.1 against the same unchanged snapshot pair and require:

- `Compared values: 28132`
- `Changed values: 0`
- `Revision events: 0`

Then run a controlled changed-value fixture to validate sensitivity and exact change classification.
