# Historical Baseline Validation Plan v0.1

## Objective

Validate that the mapping + baseline pipeline produces stable, reproducible historical features before any anomaly scoring is introduced.

## Gate A — Synthetic fixture

Input:

- at least 2 elections;
- at least 2 polling stations;
- one exact mapping;
- one unmapped/low-confidence case;
- at least one political bloc.

Expected:

- deterministic turnout/invalid-rate means;
- sample standard deviation only when n >= 2;
- low-confidence mapping excluded;
- no anomaly labels produced.

## Gate B — Two real election cycles

Normalize two real CIK election datasets into `HISTORICAL_INPUT_DICTIONARY_v0.1`.

Require:

- mapping coverage reported;
- mapping confidence distribution reported;
- zero unexplained duplicate keys;
- zero unexplained arithmetic inconsistencies;
- reproducible baseline output hash.

## Gate C — 2025 / repeat-2026 mapping

Use the 2025 RS presidential by-election and repeat-vote 2026 data.

Purpose:

- validate polling-station identity mapping on the subset involved in repeat voting;
- test whether repeated-election records can be represented without collapsing the two events;
- preserve original/repeat relationship from Election Data Standard v0.2.

## Gate D — Multi-cycle baseline

Add earlier election cycles and calculate baseline features with at least 3 turnout-eligible observations where mapping permits.

Report:

- number of canonical BM with n=1, n=2, n>=3;
- turnout baseline coverage;
- structural baseline coverage;
- political-bloc baseline coverage;
- mapping types used;
- excluded split/merge/uncertain records.

## Gate E — Freeze before anomaly work

Historical Baseline v0.1 may be frozen only when:

1. all calculations are reproducible;
2. mapping rules are auditable;
3. current/raw data are not overwritten;
4. missing data do not become zero;
5. political-share comparability is explicit;
6. the baseline engine produces no anomaly score or misconduct inference.

## Next-stage validation

After baseline freeze, Historical Anomaly Engine validation should use a blinded ranking test against the known set of polling stations where voting was later annulled/repeated. That validation belongs to the anomaly module, not to this baseline package.
