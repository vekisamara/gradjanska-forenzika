# CIK API Ingest — working module

Status: **v0.2 / experimental**

Ovaj folder sadrži radne CIK API alate za GFO Election Data Standard.

- `cik_ingestor_v0_1.py` — sekvencijalni validacioni ingestor (v0.1.1)
- `cik_ingestor_v0_2.py` — paralelni, snapshot-capable ingestor za temporalno praćenje
- `snapshot_delta_v0_1.py` — determinističko poređenje dva snapshot-a

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

## v0.2 design

v0.2 uvodi dvije glavne promjene:

1. ograničeno paralelno preuzimanje biračkih mjesta preko `ThreadPoolExecutor`;
2. svaki ingest je novi nepromjenjivi snapshot sa vlastitim vremenskim i provenance metapodacima.

Podrazumijevano se koristi `6` workera. Preporučeni raspon je `4–8`. Ne preporučuje se agresivan paralelizam prema javnom CIK API-ju.

HTTP greške se ponavljaju sa eksponencijalnim backoffom i jitterom.

## Novi Grad test

```bash
python3 cik_ingestor_v0_2.py \
  --electoral-unit-id 7 \
  --output ./test-novi-grad-v02 \
  --workers 6
```

## Full RS snapshot

```bash
python3 cik_ingestor_v0_2.py \
  --output ./rs-election-snapshots \
  --workers 6
```

Rezultat se ne upisuje direktno u output root, nego u jedinstveni snapshot:

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

Prethodni snapshot se nikada ne prepisuje. `LATEST` je samo pokazivač na najnoviji snapshot.

## Temporal metadata

`manifest.json` čuva najmanje:

- `snapshot_id`
- `previous_snapshot_id`
- `snapshot_started_at`
- `snapshot_completed_at`
- `retrieved_at`
- `source_data_from_values`
- `completeness_status`
- `polling_station_count`
- `expected_polling_station_count`
- `successful_request_count`
- `failed_request_count`
- `dataset_hash`

Normalizovani redovi dodatno čuvaju:

- `snapshot_id`
- `record_retrieved_at`
- `source_data_from`

Time se može razlikovati vrijeme GFO preuzimanja od vremena koje izvor sam navodi za podatke.

## Periodic election-day mode

Za periodično povlačenje podataka:

```bash
python3 cik_ingestor_v0_2.py \
  --output ./election-day \
  --workers 6 \
  --watch \
  --interval 1800
```

Ovo pokreće novi snapshot svakih 30 minuta. Interval se računa između početaka ciklusa; ako jedan snapshot traje 4 minute, skripta čeka još približno 26 minuta.

Minimalni dozvoljeni interval je 60 sekundi. Za javni API preporučuje se mnogo konzervativniji interval.

Za prekid koristiti `Ctrl+C`.

## Retry/backoff

Podrazumijevano:

- `--retries 3`
- `--backoff 1.0`
- `--jitter 0.25`
- `--timeout 30`

Primjer konzervativnijeg poziva:

```bash
python3 cik_ingestor_v0_2.py \
  --output ./rs-election-snapshots \
  --workers 4 \
  --retries 4 \
  --backoff 1.5
```

## Completeness

Snapshot status može biti:

- `complete`
- `partial`
- `failed`
- `unknown`

Ako bilo koji electoral-unit ili polling-station zahtjev ne uspije nakon retry pokušaja, snapshot se označava kao `partial`, a detalji ostaju u `failed_requests.csv`.

Nepotpuni snapshot se kasnije ne smije tumačiti kao da su nedostajući rezultati nestali iz CIK izvora.

## Snapshot Delta Engine

Nakon što postoje najmanje dva snapshot-a, mogu se porediti:

```bash
python3 snapshot_delta_v0_1.py \
  ./election-day/snapshots/SNAPSHOT_1 \
  ./election-day/snapshots/SNAPSHOT_2 \
  --output ./delta-1-2
```

Izlaz:

```text
delta-1-2/
├── delta_manifest.json
├── snapshot_deltas.csv
└── revision_events.csv
```

Engine poredi:

- candidate votes;
- registered voters;
- total votes / turnout;
- valid votes;
- invalid votes;
- invalid ballot components;
- polling-station/result presence.

Primjeri deskriptivnih događaja:

- `candidate_vote_increase`
- `candidate_vote_decrease`
- `turnout_revision`
- `valid_invalid_revision`
- `registered_voter_revision`
- `result_appeared`
- `result_disappeared`
- `polling_station_appeared`
- `polling_station_disappeared`

To nisu anomaly ili fraud zaključci. To su deterministički opisi promjene između dva opažena stanja.

Ako je jedan snapshot `partial`, engine podrazumijevano postavlja poređenje na `partial_snapshot` i ne pretvara nedostajuće redove u događaje nestanka. `--allow-partial` postoji samo za kontrolisane eksperimente i ne treba ga koristiti kao normalan election-day režim.

## Preservation rule

RAW API odgovori se čuvaju byte-for-byte prije analitičke upotrebe. Svaki RAW artefakt dobija SHA-256 i tačan source URL u `provenance.csv`.

## Analytical separation

Ingestor radi:

`ACQUIRE → PRESERVE → TIMESTAMP → NORMALIZE → VALIDATE`

Delta engine radi:

`SNAPSHOT N-1 → SNAPSHOT N → DERIVED DELTAS / REVISION EVENTS`

Ni jedan od ova dva alata ne radi anomaly scoring, političku interpretaciju, fraud klasifikaciju ili uzročni zaključak. To pripada budućem Election Analytics sloju.
