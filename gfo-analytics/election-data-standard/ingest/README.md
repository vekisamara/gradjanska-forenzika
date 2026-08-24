# CIK API Ingest — working module

Status: **v0.2.1 / experimental**

Ovaj folder sadrži radne CIK API alate za GFO Election Data Standard.

- `cik_ingestor_v0_1.py` — sekvencijalni validacioni ingestor (v0.1.1)
- `cik_ingestor_v0_2.py` — prva paralelna snapshot implementacija (v0.2.0; zadržana radi validacionog traga)
- `cik_ingestor_v0_2_1.py` — aktuelni paralelni snapshot-capable ingestor
- `snapshot_delta_v0_1.py` — determinističko poređenje dva snapshot-a

## Confirmed parameters for resId=39

- electionResultId: `39`
- raceId: `91`
- race code: `5`
- race name: `PREDSJEDNIK REPUBLIKE SRPSKE`
- dbName: `WebResult_2022GENP1_2025_11_19_14_41_56`
- languageId: `3`

## v0.2.1 design

Aktuelna verzija uvodi:

1. ograničeno paralelno preuzimanje biračkih mjesta preko `ThreadPoolExecutor`;
2. svaki ingest kao novi nepromjenjivi snapshot;
3. request-level `retrieved_at`;
4. CIK `dataFrom` kao odvojen `source_data_from`;
5. fallback sa basic-info odgovora na parent polling-station objekat za `location` i `dataFrom`;
6. retry/backoff/jitter;
7. completeness accounting i immutable provenance.

Podrazumijevano se koristi `6` workera. Preporučeni raspon je `4–8`. Ne preporučuje se agresivan paralelizam prema javnom CIK API-ju.

## Full RS snapshot

```bash
python3 cik_ingestor_v0_2_1.py \
  --output ./rs-election-snapshots \
  --workers 6
```

Rezultat se upisuje u jedinstveni snapshot:

```text
rs-election-snapshots/
├── LATEST
└── snapshots/
    └── snapshot-YYYYMMDDTHHMMSS.../
        ├── manifest.json
        ├── provenance.csv
        ├── validation_flags.csv
        ├── failed_requests.csv
        ├── raw/
        │   ├── electoral_units.json
        │   ├── polling_stations_eu_*.json
        │   ├── polling_station_*_basic.json
        │   └── polling_station_*_candidates.json
        └── normalized/
            ├── polling_stations.csv
            └── candidate_results.csv
```

Prethodni snapshot se nikada ne prepisuje. `LATEST` je samo pokazivač.

## Temporal metadata

`manifest.json` čuva najmanje:

- `snapshot_id`
- `previous_snapshot_id`
- `snapshot_started_at`
- `snapshot_completed_at`
- `retrieved_at`
- `source_data_from_values`
- `source_data_from_min`
- `source_data_from_max`
- `completeness_status`
- `polling_station_count`
- `expected_polling_station_count`
- `successful_request_count`
- `failed_request_count`
- `dataset_hash`

Normalizovani polling-station redovi čuvaju:

- `snapshot_id`
- `record_retrieved_at`
- `source_data_from`
- `location`
- `active`

Time se razlikuje vrijeme GFO preuzimanja od vremena koje CIK sam navodi za stanje podataka.

## Periodic election-day mode

```bash
python3 cik_ingestor_v0_2_1.py \
  --output ./election-day \
  --workers 6 \
  --watch \
  --interval 1800
```

Ovo pokreće novi snapshot svakih 30 minuta, računato između početaka ciklusa.

## Retry/backoff

Podrazumijevano:

- `--retries 3`
- `--backoff 1.0`
- `--jitter 0.25`
- `--timeout 30`

## Completeness

Snapshot status je `complete` samo ako nema failed requesta i broj normalizovanih biračkih mjesta odgovara očekivanom broju iz CIK listi.

Nepotpuni snapshot se kasnije ne smije tumačiti kao da su nedostajući rezultati nestali iz izvora.

## Snapshot Delta Engine

```bash
python3 snapshot_delta_v0_1.py \
  ./election-day/snapshots/SNAPSHOT_1 \
  ./election-day/snapshots/SNAPSHOT_2 \
  --output ./delta-1-2
```

Engine deterministički poredi candidate votes, turnout, valid/invalid podatke, registered voters i prisustvo rezultata. On ne radi anomaly scoring niti fraud klasifikaciju.

## Validation history

`VALIDATION_CASE_003_FULL_RS_PARALLEL_SNAPSHOT_v0.2.md` dokumentuje prvi puni paralelni snapshot v0.2.0:

- 2.164 biračka mjesta
- 12.984 kandidatska reda
- 4.393 uspješna zahtjeva
- 0 failed requesta
- `complete`
- oko 105,6 sekundi akvizicije

v0.2.0 je imao normalizacijski propust: `location` i `source_data_from` su čitani samo iz basic-info odgovora, iako ih CIK Race5 daje u parent polling-station objektu. RAW podaci nisu izgubljeni. v0.2.1 ispravlja taj problem fallback pravilom.

## Preservation rule

RAW API odgovori se čuvaju byte-for-byte. Svaki RAW artefakt dobija SHA-256, source URL, request retrieval time i broj pokušaja u `provenance.csv`.

## Analytical separation

Ingestor radi:

`ACQUIRE → PRESERVE → TIMESTAMP → NORMALIZE → VALIDATE`

Delta engine radi:

`SNAPSHOT N-1 → SNAPSHOT N → DERIVED DELTAS / REVISION EVENTS`

Ni jedan alat ne radi političku interpretaciju, anomaly scoring, fraud klasifikaciju ili uzročni zaključak.
