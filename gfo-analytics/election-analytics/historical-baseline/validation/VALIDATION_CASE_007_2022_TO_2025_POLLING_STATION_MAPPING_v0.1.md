# VALIDATION CASE 007 — 2022 → 2025 polling-station mapping v0.1

Status: **PASS WITH REVIEW SET**

## Inputs

Historical election: `2022-BIH-RS-PRES-GENERAL-CONFIRMED`

Historical snapshot: `snapshot-20260825T204018.258699Z-95f56f5a`

Canonical election: `2025-BIH-RS-PRES-BYELECTION-CONFIRMED`

Canonical snapshot: `snapshot-20260824T211536.942059Z-01efb8c5`

Mapping engine rule set: `polling_station_mapping_engine_v0_1.py` / v0.1.0.

The mapping is deliberately conservative. Automatic proposals require the same public polling-station code and the same municipality code. Split, merge, renumbering and boundary-change cases are not auto-resolved.

## Input integrity

2022 input contains 2,239 polling stations.

2025 input contains 2,164 polling stations.

Both source snapshots had zero validation flags and zero failed requests at ingest.

## Mapping result

- Exact code + municipality matches: **1,997 / 2,239 (89.19%)**.
- 2022 stations without an exact 2025 match: **242**.
- 2025 stations without an exact 2022 match: **167**.
- Exact matches usable for baseline at the default confidence threshold (>= 0.95): **1,799 / 2,239 (80.35%)**.
- Exact matches withheld from baseline because registered-voter population changed by more than 25%: **198**.

Confidence distribution produced by the v0.1 rules:

- 1,527 records at 0.98;
- 248 records at 0.97;
- 24 records at 0.95;
- 198 records at 0.85;
- 242 records at 0.00 / unmapped.

Among the 1,997 exact-code matches, 1,841 have the same normalized polling-station name and 1,597 have the same normalized location string. Name/location differences are retained as review signals; they do not by themselves invalidate the public-code mapping.

## Review set

The unmatched set is strongly concentrated in a limited number of electoral units. The largest 2022 unmatched groups are:

- Brčko Distrikt BiH (opcija RS), code 028: 137;
- Foča, code 166: 14;
- Banja Luka, code 034: 9;
- Čajniče, code 169: 8;
- Sokolac, code 121: 7;
- Teslić, code 074: 6;
- Laktaši, code 011: 6;
- Prnjavor, code 013: 6;
- Ljubinje, code 179: 6.

The largest unmatched/new 2025 groups are:

- Brčko Distrikt BiH (opcija RS), code 028: 126;
- Prnjavor, code 013: 6;
- Foča, code 166: 6;
- Istočno Novo Sarajevo, code 140: 6;
- Doboj, code 038: 5;
- Laktaši, code 011: 4;
- Banja Luka, code 034: 3.

Brčko therefore dominates the non-exact mapping set and should be handled as a separate review block rather than being allowed to distort the general mapping assessment.

## Interpretation

The v0.1 mapping engine behaves as intended. It obtains a large exact-code core while refusing to silently infer continuity for 242 historical stations and while withholding another 198 exact-code matches whose electorate size changed by more than 25%.

This is sufficient to start a conservative two-election Historical Baseline using the 1,799 default-usable mappings. The remaining 440 2022 records must not be silently included in station-level longitudinal baselines until reviewed or explicitly mapped.

No split, merge, renumbering or boundary-change classification is asserted by this validation. Those labels require a separate review step using names, locations, neighboring codes and, where necessary, official polling-station lists.

## Result

**PASS WITH REVIEW SET.**

The automated mapping layer is suitable for the initial Historical Baseline. A full mapping-proposal CSV is reproducible from the two normalized polling-station inputs with `polling_station_mapping_engine_v0_1.py`; it is not treated as a hand-curated canonical mapping until the review set is resolved.
