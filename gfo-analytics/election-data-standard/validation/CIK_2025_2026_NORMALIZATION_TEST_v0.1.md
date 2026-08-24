# CIK 2025/2026 Normalization Test v0.1

**Status:** WORKING NOTE  
**Date:** 2026-08-24

## Objective

Prvi real-source test GFO Election Data Standarda koristi javne izvore Centralne izborne komisije BiH za prijevremene izbore za predsjednika Republike Srpske 2025. i ponovljene izbore 2026.

## Verified source facts used in this test

- prijevremeni izbori održani su 23.11.2025;
- odgođeno glasanje na biračkom mjestu 068B005 Korićani održano je 30.11.2025;
- ponovljeni izbori održani su 08.02.2026;
- ponovljeni izbori obuhvatili su 136 biračkih mjesta u 17 osnovnih izbornih jedinica;
- CIK BiH je 13.02.2026. potvrdio objedinjene rezultate;
- potvrđeni rezultati dostupni su kroz CIK-ovu web aplikaciju za rezultate (`resId=39`).

## Normalized entities successfully represented

Prvi test pokazuje da standard može bez gubitka značenja predstavljati:

1. izborni događaj;
2. ponovljeni izborni događaj kao poseban event povezan sa originalnim izborima;
3. nadležno tijelo;
4. provenance javnog izvora;
5. datume glasanja i potvrđivanja;
6. scope ponavljanja izbora.

## Issue discovered: repeated election linkage

v0.1 treba eksplicitno polje za vezu između originalnog i ponovljenog izbornog događaja.

Predložena polja za v0.2:

- `parent_election_id`
- `event_relation` sa vrijednostima npr. `repeat`, `postponed`, `rerun`, `partial_repeat`, `correction`.

Bez toga bi odnos 23.11.2025 -> 08.02.2026. bio sačuvan samo u napomeni, što nije dovoljno za mašinsku analizu.

## Issue discovered: publication vs election timestamps

Standard treba razlikovati najmanje:

- `election_date`
- `results_determined_at`
- `results_confirmed_at`
- `published_at`

To je važno za praćenje revizija rezultata.

## Row-level result test

CIK-ova potvrđena result aplikacija je dinamička. Dodatnim pregledom CIK-ove javne ASP.NET Web API dokumentacije utvrđeno je da aplikacija ima javno dokumentovane endpoint obrasce za `Race5`, koji odgovara izbornoj utrci korištenoj u ruti `#/5/13/0` aplikacije sa `resId=39`.

Relevantni API obrasci su:

- `GET race5_basicinfo/{dbName}`
- `GET race5_candidatesresult/{dbName}/{languageId}`
- `GET race5_electoralunit/{dbName}/{languageId}`
- `GET race5_electoralunitbasicinfo/{dbName}/{electoralUnitId}`
- `GET race5_electoralunitcandidatesresult/{dbName}/{electoralUnitId}/{languageId}`
- `GET race5_pollingstation/{dbName}/{electoralUnitId}/{languageId}`
- `GET race5_pollingstationsbasicinfo/{dbName}/{pollingStationId}`
- `GET race5_pollingstationscandidatesresult/{dbName}/{pollingStationId}/{languageId}`

Dokumentovani odgovor `race5_pollingstation` sadrži najmanje `pollingStationId`, `name`, `location`, `code`, `dataFrom` i `active`.

Dokumentovani odgovor `race5_pollingstationsbasicinfo` sadrži najmanje broj birača, ukupne glasove, važeće i nevažeće glasove, prazne nevažeće listiće i ostale nevažeće listiće.

Dokumentovani odgovor `race5_pollingstationscandidatesresult` sadrži najmanje `name`, `code`, `totalVotes` i `percentage` za kandidata na konkretnom biračkom mjestu.

CIK administrativni API dokumentuje i endpoint:

- `GET administration_electionresultcontroller_getdatabasename/{electionResultId}`

koji je predviđen za dobijanje `dbName` iz `electionResultId`. Za ovaj slučaj `electionResultId` je 39. U trenutnom istraživačkom okruženju stvarni odgovor tog endpointa nije bilo moguće direktno dohvatiti, pa `dbName` još nije verifikovan i ne smije se nagađati.

Zbog toga još nije kreiran stvarni row-level RAW dataset. Čim se pribavi verifikovani `dbName`, može se automatizovati kompletan lanac:

`resId=39 -> dbName -> Race5 electoral units -> polling stations -> polling-station basic info -> candidate results`.

Za puni test treba pribaviti jedan od sljedećih kanonskih RAW izvora:

1. direktan odgovor javnog CIK API-ja za `resId=39`;
2. službeni eksport rezultata po biračkim mjestima iz CIK aplikacije, ako je dostupan;
3. službeni XLS/CSV/JSON dataset;
4. kompletan izvještaj koji sadrži rezultate po biračkim mjestima, uz dokumentovanu ekstrakciju.

Tek tada se kreira `raw/` kopija, hash i normalizovani dataset.

## Validation conclusion

**PASS WITH DESIGN ISSUES**

v0.1 je dovoljan za osnovne election/source/provenance entitete. Dodatno je potvrđeno da CIK infrastruktura izlaže strukturisane API modele za izborna mjesta i rezultate kandidata, što čini automatski ingest tehnički realnim. Prije v0.2 treba dodati eksplicitno modeliranje povezanih izbornih događaja i razdvojiti vremenske tačke objave, utvrđivanja i potvrđivanja rezultata.

## Source register

- CIK BiH, Prijevremeni izbori za predsjednika Republike Srpske — potvrđeni rezultati, `resId=39`.
- CIK BiH, ASP.NET Web API Help — Administration_ElectionResult, Administration_Race i Race5 endpoint dokumentacija.
- CIK BiH, Odluka o potvrđivanju i objavljivanju rezultata, 13.02.2026.
- CIK BiH, Odluka o utvrđivanju i objavljivanju rezultata ponovnih prijevremenih izbora na 136 biračkih mjesta u 17 izbornih jedinica, 09.02.2026.
