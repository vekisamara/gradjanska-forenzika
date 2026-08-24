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

CIK-ova potvrđena result aplikacija je dinamička i javna stranica ne izlaže kompletan biračko-mjesto dataset kao jednostavan statički CSV kroz trenutno dokumentovani javni link. Zbog toga u ovom commitu nisu izmišljeni niti ručno rekonstruisani redovi rezultata po biračkim mjestima.

Za puni test treba pribaviti jedan od sljedećih kanonskih RAW izvora:

1. službeni eksport rezultata po biračkim mjestima iz CIK aplikacije, ako je dostupan;
2. službeni XLS/CSV/JSON dataset;
3. kompletan izvještaj koji sadrži rezultate po biračkim mjestima, uz dokumentovanu ekstrakciju.

Tek tada se kreira `raw/` kopija, hash i normalizovani dataset.

## Validation conclusion

**PASS WITH DESIGN ISSUES**

v0.1 je dovoljan za osnovne election/source/provenance entitete, ali prije v0.2 treba dodati eksplicitno modeliranje povezanih izbornih događaja i razdvojiti vremenske tačke objave, utvrđivanja i potvrđivanja rezultata.

## Source register

- CIK BiH, Prijevremeni izbori za predsjednika Republike Srpske — potvrđeni rezultati, resId=39.
- CIK BiH, Odluka o potvrđivanju i objavljivanju rezultata, 13.02.2026.
- CIK BiH, Odluka o utvrđivanju i objavljivanju rezultata ponovnih prijevremenih izbora na 136 biračkih mjesta u 17 izbornih jedinica, 09.02.2026.
