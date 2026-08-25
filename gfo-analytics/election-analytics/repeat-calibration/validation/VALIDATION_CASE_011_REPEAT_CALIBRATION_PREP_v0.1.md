# VALIDATION CASE 011 — 2025 original vs 2026 repeat calibration preparation

Status: **PARTIAL — AGGREGATE CALIBRATION AVAILABLE; STATION-LEVEL ORIGINAL DATA STILL REQUIRED**

## Confirmed official target universe

CIK ordered repeat voting on 136 polling stations in 17 electoral units for 8 February 2026. CIK states that the repeat election used the same candidate lists and the same Central Voters Register extracts as the annulled election. This makes the pair materially more comparable than the 2022 general-election vs 2025 by-election comparison.

## Repeat-side verification

The final CIK Race5 snapshot `snapshot-20260824T211536.942059Z-01efb8c5` contains all 136 official repeat-station codes: **136/136 present**.

For those 136 stations the final snapshot contains:

- registered voters: 84,249
- total votes: 41,835
- valid votes: 41,161
- invalid votes: 674
- candidate result rows: 816 (6 candidates × 136 stations)

Final candidate totals on the 136 repeat stations:

- Siniša Karan: 28,698
- Branko Blanuša: 12,126
- Igor Gašević: 105
- Dragan Đokanović: 103
- Slavko Dragičević: 77
- Nikola Lazarević: 52

## Aggregate original-vs-repeat reconstruction

A contemporaneous report documenting CIK's removal of the 136 annulled polling-station results preserves the CIK determined candidate totals before deletion and the totals remaining after deletion. Subtracting the latter from the former yields the aggregate original 23 Nov 2025 candidate votes on the 136 annulled stations.

Original 136-station aggregate:

- Siniša Karan: 26,496
- Branko Blanuša: 11,218
- Dragan Đokanović: 93
- Nikola Lazarević: 90
- Igor Gašević: 94
- Slavko Dragičević: 75
- total valid candidate votes: 38,066

Repeat 136-station aggregate:

- Siniša Karan: 28,698
- Branko Blanuša: 12,126
- Dragan Đokanović: 103
- Nikola Lazarević: 52
- Igor Gašević: 105
- Slavko Dragičević: 77
- total valid candidate votes: 41,161

Aggregate deltas:

- Karan: +2,202
- Blanuša: +908
- Đokanović: +10
- Lazarević: -38
- Gašević: +11
- Dragičević: +2
- valid candidate votes: +3,095

These are descriptive aggregate changes only. They do not establish station-level behavior and are not an anomaly verdict.

## Important voter-register note

CIK's pre-election public communication stated that 84,474 voters had the right to vote at the repeat election, while the sum of `registered_voters` in the 136 regular polling-station records in the final Race5 snapshot is 84,249. The difference is 225 and must not be silently reconciled. It may reflect categories outside the regular polling-station API layer or another administrative distinction. This requires provenance clarification before any denominator-sensitive aggregate turnout calibration.

## Station-level blocker

The current final Race5 API snapshot does not retain the superseded 23 November 2025 station-level results for the 136 annulled stations. The CIK decision of 15 December 2025 states that its integral part is a tabular presentation of results by polling station, political subject and candidate, but the currently linked one-page decision PDF does not itself contain that table.

Therefore station-level calibration must not reconstruct original observations from the final post-repeat snapshot or infer them from aggregate totals.

## Required next acquisition

Acquire an authoritative pre-repeat station-level table/snapshot dated after original counting and before replacement/deletion of the 136 stations. Acceptable provenance includes:

- a preserved CIK results-portal/API snapshot from December 2025;
- the official CIK tabular annex associated with the 15 Dec 2025 determined-results decision;
- another official CIK export retaining the original polling-station values.

## Result

**PARTIAL.** Aggregate candidate calibration is now available and recorded in `CASE011_AGGREGATE_CANDIDATE_CALIBRATION_v0.1.csv`. Full station-level Historical Anomaly calibration remains blocked until the original 136-station data are acquired.
