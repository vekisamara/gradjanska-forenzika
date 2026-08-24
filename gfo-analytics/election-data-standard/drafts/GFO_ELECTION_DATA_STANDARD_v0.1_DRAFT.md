# GFO Election Data Standard v0.1

**Status:** DRAFT  
**Role:** Canonical election-data interoperability standard  
**Date:** 2026-08-24

## 1. Purpose

GFO Election Data Standard definiše otvoren, mašinski čitljiv i auditabilan format za prikupljanje, čuvanje, razmjenu i analitičku obradu izbornih podataka. Standard ne određuje da li je rezultat regularan, manipulisan ili anomalijski; takva pravila pripadaju posebnim analitičkim modulima.

## 2. Fundamental data layers

`RAW -> NORMALIZED -> DERIVED -> INTERPRETED`

- **RAW**: podatak sačuvan u obliku u kojem je pribavljen. Ne mijenja se.
- **NORMALIZED**: RAW podatak preveden u kanonsku GFO strukturu bez promjene činjeničnog značenja.
- **DERIVED**: vrijednost dobijena determinističkom ili statističkom obradom.
- **INTERPRETED**: analitički zaključak izveden iz prethodnih slojeva, uključujući LLM interpretaciju.

## 3. Core entities

### Election
Obavezno: `election_id`, `election_date`, `election_type`, `jurisdiction`, `authority`.

### Polling station
Obavezno: `polling_station_id`, `election_id`, `municipality_code`, `polling_station_name`, `registered_voters`.

Opcionalno: `address`, `latitude`, `longitude`, `urban_rural`, `historical_identifier`.

### Candidate
Obavezno: `candidate_id`, `election_id`, `candidate_name`.

Opcionalno: `party_id`, `political_bloc_id`.

### Result
Obavezno: `election_id`, `polling_station_id`, `candidate_id`, `votes`.

### Turnout
Konačni zapis: `election_id`, `polling_station_id`, `registered_voters`, `total_votes`.

Opcionalno: `valid_votes`, `invalid_votes`.

Live zapis dodatno koristi `timestamp` i `voted_so_far`.

### Source
Obavezno: `source_id`, `source_type`, `source_name`, `retrieved_at`, `verification_status`.

Opcionalno: `source_url`, `document_id`, `observer_id`, `notes`.

## 4. Source types

Kanonske vrijednosti: `official`, `observer`, `political_party`, `media`, `polling_organization`, `civil_society`, `research`, `crowdsourced`, `other`.

Tip izvora nije automatska ocjena pouzdanosti.

## 5. Verification status

Kanonske vrijednosti: `unverified`, `single_source`, `multiple_source`, `documented`, `official`.

Status opisuje nivo potvrđenosti podatka, a ne apsolutnu istinitost.

## 6. Provenance

Svaki dataset mora omogućiti rekonstrukciju porijekla: izvor, vrijeme pribavljanja, originalni format, transformacije, verzija izvora i verzija procesa normalizacije.

RAW dataset mora ostati dostupan za reprodukciju analize.

## 7. Canonical identifiers

Identifikatori moraju biti stabilni i mašinski čitljivi. Zvanični identifikator biračkog mjesta ima prednost. Interni GFO identifikator ne smije izbrisati ili zamijeniti izvorni identifikator.

Primjer `election_id`: `2026-BIH-GE-RS-PRES`.

## 8. Historical mapping

Promjene identifikatora, granica ili strukture biračkih mjesta evidentiraju se u posebnoj mapping tabeli sa najmanje: `current_polling_station_id`, `historical_polling_station_id`, `election_id`, `mapping_type`, `mapping_confidence`, `mapping_source`.

## 9. Temporal data

Vrijeme se čuva u ISO 8601 formatu sa vremenskom zonom, npr. `2026-10-04T15:00:00+02:00`.

Raniji snapshot se ne prepisuje novijim.

## 10. Corrections and revisions

Ispravka ne briše prethodnu vrijednost. Sistem mora podržavati lanac `v1 -> v2 -> v3 -> final` i čuvati prethodnu i novu vrijednost, vrijeme izmjene, izvor i razlog izmjene ako je poznat.

## 11. Missing data

`0` nije isto što i nedostajući podatak. Standard razlikuje najmanje: `0`, `null`, `not_applicable`, `not_reported`.

## 12. Validation

Greške validacije ne mijenjaju RAW podatak. Generišu `validation_flag` i eventualno `validation_severity`.

Osnovne provjere uključuju nenegativne glasove, numeričke tipove, konzistentnost zbirnih vrijednosti, jedinstvenost identifikatora i dozvoljene enumeracije.

## 13. Analytical neutrality

Standard ne definiše: `fraud`, `manipulation`, `suspicious polling station`, političku namjeru ili krivicu. To pripada posebnim analitičkim metodologijama.

## 14. Machine-readable formats

Obavezno: CSV i JSON. Preporučeno: JSON Schema za validaciju i Parquet za veće skupove. Excel može biti ulazno/izlazni format, ali nije kanonski format dugoročnog čuvanja.

## 15. Reproducibility

DERIVED dataset mora sadržati najmanje: `input_dataset_id`, `input_dataset_version`, `processing_module`, `processing_module_version`, `processed_at`. Preporučeno je čuvati parametre i hash ulaza.

## 16. LLM boundary

LLM nije dio kanonskog Data Standarda. LLM koristi paket formiran iz podataka, ali njegov izlaz pripada sloju `INTERPRETED` i ne smije mijenjati RAW, NORMALIZED ili DERIVED zapise.

## 17. Extension principle

Posebni moduli mogu proširiti standard dodatnim poljima, ali ne smiju promijeniti značenje kanonskih polja. Planirani moduli uključuju Historical Election Analytics, Live Election Analytics, Exit Poll Analytics, Polling Station Anomaly Detection, Observer Incident Analytics i Post-Election Forensics.

## 18. Versioning

Standard koristi semantičko verzionisanje. Tokom `0.x` faze dozvoljene su breaking changes. Prije `v1.0` moraju biti stabilizovani schema, provenance, validation, historical mapping, live-data model i reference testovi.

## 19. Core rule

**Data must remain distinguishable from calculation, and calculation must remain distinguishable from interpretation.**
