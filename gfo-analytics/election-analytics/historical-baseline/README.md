# GFO Election Analytics — Historical Baseline v0.1

**Status:** WORKING / EXPERIMENTAL  
**Standard dependency:** GFO Election Data Standard v0.2-draft

Historical Baseline je prvi analitički sloj iznad GFO Election Data Standarda.

Njegov zadatak nije da označi izborno mjesto kao anomalno, nego da iz više izbornih ciklusa proizvede reproduktivan istorijski profil biračkog mjesta koji kasnije koriste Historical Anomaly Engine, Peer Group Engine i LLM evidence package.

## Canonical flow

```text
NORMALIZED HISTORICAL ELECTION DATA
        ↓
POLLING-STATION MAPPING
        ↓
BASELINE FEATURE ENGINE
        ↓
BASELINE DATASET
        ↓
future: PEER GROUP / ANOMALY ENGINE
```

## v0.1 package

- `METHODOLOGY_v0.1.md` — metodološka pravila baseline-a
- `spec/HISTORICAL_INPUT_DICTIONARY_v0.1.csv` — kanonski historical input
- `spec/POLLING_STATION_MAPPING_STANDARD_v0.1.md` — pravila mapiranja BM kroz izbore
- `mapping/polling_station_mapping_engine_v0_1.py` — konzervativni mapping helper
- `baseline/baseline_engine_v0_1.py` — deterministički baseline feature engine
- `validation/VALIDATION_PLAN_v0.1.md` — validacioni plan
- `examples/historical_results_SYNTHETIC.csv` — sintetički primjer ulaza
- `examples/polling_station_mapping_SYNTHETIC.csv` — sintetički mapping primjer

## Important separation

Baseline Engine izračunava istorijske karakteristike. Ne izračunava anomaly score i ne koristi LLM.

`RAW → NORMALIZED → MAPPED → BASELINE FEATURES`

Tek budući analitički sloj radi:

`BASELINE + CURRENT ELECTION → DEVIATIONS / ANOMALY FEATURES`

## Planned historical coverage

Poželjni ciklusi za RS predsjedničku analitiku:

- Opšti izbori 2018;
- Lokalni izbori 2020, samo za relevantne turnout/strukturne karakteristike kada je metodološki opravdano;
- Opšti izbori 2022;
- Lokalni izbori 2024, uz isto ograničenje;
- prijevremeni izbori za predsjednika RS 2025;
- ponovljeno glasanje 2026 na poništenim biračkim mjestima.

Nisu svi izbori politički direktno uporedivi. Turnout i strukturne karakteristike mogu koristiti širi istorijski set, dok candidate/bloc share zahtijeva eksplicitno definisanu političku uporedivost.

## First production gate

v0.1 se smatra tehnički spremnim tek kada najmanje dva stvarna izborna ciklusa budu normalizovana, mapirana i baseline engine proizvede stabilan izlaz bez neobjašnjenih validation flagova.
