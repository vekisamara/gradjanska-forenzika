# GFO Election Data Standard — Validation Case 001: Novi Grad

**Status:** PASS WITH MAPPING CORRECTION  
**Date:** 2026-08-24  
**Scope:** CIK BiH, potvrđeni rezultati prijevremenih izbora za predsjednika Republike Srpske, `electionResultId=39`, izborna jedinica Novi Grad (`electoralUnitId=7`, code `007`).

## 1. Objective

Prvi stvarni end-to-end test standarda provjerava da li GFO može:

1. automatski preuzeti službene CIK podatke kroz javni API;
2. sačuvati RAW JSON bez izmjene;
3. evidentirati provenance i SHA-256;
4. normalizovati biračka mjesta i rezultate kandidata;
5. provjeriti osnovnu aritmetičku konzistentnost;
6. identifikovati nepodudarnosti između pretpostavljene i stvarne CIK JSON šeme.

## 2. Confirmed CIK parameters

- `electionResultId = 39`
- `raceId = 91`
- `race code = 5`
- `dbName = WebResult_2022GENP1_2025_11_19_14_41_56`
- `languageId = 3`
- `electoralUnitId = 7`
- electoral unit code: `007`
- electoral unit name: `NOVI GRAD`

## 3. Test package

Korisnički izvršen `cik_ingestor_v0_1.py` proizveo je paket sa:

- 52 biračka mjesta;
- 312 kandidatskih redova;
- 52 RAW basic-info odgovora;
- 52 RAW candidate-result odgovora;
- RAW listom biračkih mjesta;
- RAW listom izbornih jedinica;
- manifestom i provenance evidencijom.

Broj kandidatskih redova je konzistentan sa 52 biračka mjesta × 6 kandidata = 312.

## 4. Actual CIK Race5 structures observed

### Polling station list

Primjer `007B001 CENTAR 1`:

```json
{
  "pollingStationId": 6,
  "name": "CENTAR  1",
  "location": "O.Š.SVETI SAVA NOVI GRAD",
  "code": "007B001",
  "dataFrom": "2026-02-13T11:42:19.57",
  "active": true
}
```

### Polling station basic info

```json
{
  "pollingStationId": 0,
  "numberOfVoters": 576,
  "numberCandidates": 6,
  "totalVotes": 224,
  "percentageTotalVotes": 38.89,
  "validVotes": 220,
  "totalInvalidVotes": 4,
  "invalidBlankBallots": 1,
  "invalidOthersBallots": 3
}
```

Important: `pollingStationId` inside the basic-info payload was observed as `0`; canonical polling-station identity must therefore be inherited from the parent API request/list object, not from this field.

### Candidate result

Observed CIK structure:

```json
{
  "name": "BRАNKО BLАNUŠА - SRPSKA DEMOKRATSKA STRANKA",
  "code": "00018",
  "totalVotes": 121,
  "percentage": 55.0
}
```

The initial v0.1 normalizer expected `candidateId`/`votes` variants and therefore left `candidate_id` and `votes` empty. This was an ingestor mapping defect, not a source-data defect.

## 5. Mapping correction

Ingestor v0.1.1 maps:

- `code` → `candidate_code`
- `code` → fallback `candidate_id`
- `name` → `candidate_name`
- `totalVotes` → `votes`
- `percentage` → `vote_percentage`
- polling-station `location` → `location`
- polling-station `dataFrom` → `source_data_from`
- `numberCandidates` → `number_candidates`
- `percentageTotalVotes` → `turnout_percentage`

## 6. Arithmetic validation

The corrected mapping was replayed locally against all uploaded Novi Grad RAW files.

Result:

- polling stations tested: **52**
- candidate rows tested: **312**
- validation flags: **0**

Checks performed per polling station:

1. `total_votes <= registered_voters`
2. `valid_votes + invalid_votes == total_votes`
3. `invalid_blank_ballots + invalid_other_ballots == invalid_votes`
4. sum of all candidate votes `== valid_votes`
5. polling-station ID present
6. polling-station code present

For `007B001 CENTAR 1`:

- registered voters: 576
- total votes: 224
- valid votes: 220
- invalid votes: 4
- blank invalid: 1
- other invalid: 3
- Branko Blanuša: 121
- Siniša Karan: 99

Checks:

- 220 + 4 = 224
- 1 + 3 = 4
- 121 + 99 = 220

## 7. Standard-design findings

Validation Case 001 supports the overall RAW → NORMALIZED architecture but requires the v0.2 draft to add or clarify:

- separate `polling_station_code` and source-internal `polling_station_id`;
- `location` as source-provided polling-station location text;
- `source_data_from` as source dataset timestamp distinct from retrieval time;
- `candidate_code` as an official source identifier;
- explicit source-field mapping rules;
- `number_candidates` and `turnout_percentage` as optional normalized fields;
- rule that unreliable/placeholder identifiers inside child payloads must not override a validated parent identifier;
- validation output as a first-class artifact, not silent correction.

## 8. Conclusion

**PASS WITH MAPPING CORRECTION**

The CIK API can serve as a reproducible machine-readable source for the GFO Election Data Standard. The initial ingestion architecture is valid. A concrete field-mapping defect was identified and corrected without modifying RAW data.

The next validation step is to rerun Novi Grad with ingestor v0.1.1 and require `validation_flag_count = 0`, then expand to the complete Republic of Srpska dataset.
