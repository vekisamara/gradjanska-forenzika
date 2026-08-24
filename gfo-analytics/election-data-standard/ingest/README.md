# CIK API Ingest — working module

Status: **v0.1 / experimental**

Ovaj folder sadrži radni CIK API ingestor za GFO Election Data Standard.

## Confirmed parameters for resId=39

- electionResultId: `39`
- raceId: `91`
- race code: `5`
- race name: `PREDSJEDNIK REPUBLIKE SRPSKE`
- dbName: `WebResult_2022GENP1_2025_11_19_14_41_56`
- languageId: `3`

## Confirmed Race5 endpoint family

- `race5_electoralunit/{dbName}/{languageId}`
- `race5_pollingstation/{dbName}/{electoralUnitId}/{languageId}`
- `race5_pollingstationsbasicinfo/{dbName}/{pollingStationId}`
- `race5_pollingstationscandidatesresult/{dbName}/{pollingStationId}/{languageId}`

CIK API help additionally documents the Race5 polling-station basic-info response, including `numberOfVoters`, `totalVotes`, `validVotes`, `totalInvalidVotes`, `invalidBlankBallots` and `invalidOthersBallots`.

## Minimal Novi Grad test

Novi Grad has confirmed internal `electoralUnitId=7` and official code `007`.

Run:

```bash
python3 cik_ingestor_v0_1.py --electoral-unit-id 7 --output ./test-novi-grad
```

The script should produce:

```text
test-novi-grad/
├── manifest.json
├── provenance.csv
├── raw/
│   ├── electoral_units.json
│   ├── polling_stations_eu_7.json
│   ├── polling_station_*_basic.json
│   └── polling_station_*_candidates.json
└── normalized/
    ├── polling_stations.csv
    └── candidate_results.csv
```

## Full election ingest

After the Novi Grad test passes:

```bash
python3 cik_ingestor_v0_1.py --output ./cik-2025-rs-president-confirmed
```

This enumerates all electoral units returned by CIK and downloads all polling stations and candidate results.

## Preservation rule

RAW API responses are written unchanged before normalization. Each saved RAW file gets a SHA-256 hash and source URL in `provenance.csv`.

## Known v0.1 limitation

The exact field names returned by the two polling-station result endpoints are inferred from CIK's documented API model and are normalized defensively with alternate key names. The first real run must therefore be treated as a schema-discovery/validation run. If CIK returns a different key name, RAW data remain preserved and the normalizer should be updated rather than editing the source data.

No statistical anomaly logic belongs in this ingestor. Its role is limited to acquisition, preservation and normalization.
