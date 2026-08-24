# Validation Rules v0.1

**Status:** DRAFT

Validacija ne smije mijenjati RAW podatke. Svaka povreda pravila proizvodi `validation_flag`; NORMALIZED zapis se može odbiti, prihvatiti uz upozorenje ili zadržati za ručnu provjeru.

## Severity

- `INFO` — neuobičajeno ali prihvatljivo.
- `WARN` — podatak je moguće koristiti uz oprez.
- `ERROR` — zapis nije siguran za automatsku analitiku.
- `FATAL` — zapis ne zadovoljava minimalni schema ugovor.

## Structural rules

### VAL-001 Required field missing
FATAL ako nedostaje obavezno polje definisano data dictionary-em.

### VAL-002 Invalid type
FATAL kada vrijednost nije dozvoljenog tipa.

### VAL-003 Invalid enumeration
ERROR za vrijednosti van kontrolisanog vokabulara.

### VAL-004 Duplicate key
ERROR ako postoji više kanonskih zapisa sa istim očekivano jedinstvenim ključem bez revision oznake.

## Referential integrity

### VAL-010 Unknown election
ERROR ako zapis referencira nepoznat `election_id`.

### VAL-011 Unknown polling station
ERROR ako rezultat/turnout referencira nepoznat `polling_station_id`.

### VAL-012 Unknown candidate
ERROR ako rezultat referencira nepoznat `candidate_id` za konkretne izbore.

## Numeric consistency

### VAL-020 Negative value
FATAL za negativne glasove, registrovane birače ili turnout vrijednosti.

### VAL-021 Votes exceed registered voters
WARN/ERROR ako `total_votes > registered_voters`. RAW vrijednost se čuva; zahtijeva provjeru definicije izvora i mogućih posebnih kategorija glasanja.

### VAL-022 Candidate votes exceed valid votes
ERROR ako je `candidate_votes > valid_votes` kada su obje vrijednosti uporedive u istom scope-u.

### VAL-023 Valid plus invalid mismatch
WARN ako su dostupni `valid_votes`, `invalid_votes` i `total_votes`, ali njihov zbir nije jednak `total_votes`. Pravilo se primjenjuje samo kada definicije izvora garantuju istu populaciju.

### VAL-024 Sum of candidate votes mismatch
WARN ako zbir kandidatskih glasova nije jednak objavljenom broju važećih glasova. Dodatne kategorije ili posebni listići moraju se provjeriti prije ERROR statusa.

## Temporal rules

### VAL-030 Timestamp missing for live record
ERROR ako live turnout zapis nema ISO 8601 timestamp sa vremenskom zonom.

### VAL-031 Non-monotonic turnout
WARN ako `voted_so_far` opada u kasnijem snapshot-u. Raniji zapis se ne briše.

### VAL-032 Future/invalid election timestamp
ERROR ako live zapis vremenski ne odgovara definisanom izbornom događaju bez obrazloženja.

## Provenance rules

### VAL-040 Missing provenance
FATAL za NORMALIZED ili DERIVED dataset bez provenance zapisa.

### VAL-041 Missing original identifier
ERROR ako je zvanični identifikator postojao u RAW izvoru, ali nije sačuvan u normalizaciji.

### VAL-042 Untraceable transformation
ERROR za DERIVED dataset bez identifikovane verzije ulaznog dataseta i processing modula.

## Missing data rules

### VAL-050 Zero substituted for missing
ERROR ako se utvrdi da je `null`/`not_reported` tokom normalizacije pretvoren u `0` bez eksplicitne dokumentovane transformacije.

### VAL-051 Empty string ambiguity
WARN za prazne stringove u poljima koja imaju semantičke missing vrijednosti; normalizator ih mora mapirati na dokumentovanu missing kategoriju.

## Historical mapping rules

### VAL-060 Unmapped historical station
INFO/WARN kada biračko mjesto nema potvrđenu istorijsku vezu. Takav zapis ne smije automatski ulaziti u longitudinalni baseline.

### VAL-061 Low-confidence mapping
WARN kada je `mapping_confidence` ispod praga koji odredi konkretni analitički modul.

## Revision rules

### VAL-070 Silent overwrite
FATAL ako novi snapshot ili službena korekcija prepisuje postojeću vrijednost bez revision lanca.

### VAL-071 Missing revision provenance
ERROR ako promjena vrijednosti nema vrijeme i izvor promjene.

## LLM boundary

### VAL-080 Interpreted value in canonical data
ERROR ako polje koje sadrži procjenu tipa `fraud`, `suspicious`, političku namjeru ili LLM zaključak bude upisano u RAW/NORMALIZED kanonske zapise.

## Validation output

Preporučeni zapis:

```json
{
  "record_id": "...",
  "rule_id": "VAL-031",
  "severity": "WARN",
  "message": "voted_so_far decreased from previous snapshot",
  "source_value": 417,
  "previous_value": 423,
  "review_status": "open"
}
```
