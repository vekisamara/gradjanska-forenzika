# Registar izvora i verzionisanje

**Oznaka:** GF-MET-VERSION 1.0

## 1. Registar izvora

Svaki izvor dobija stabilan ID, naziv, autora/organ, datum, broj akta, datum pribavljanja, URL ili arhivsku lokaciju, status O/K/R/N, D-nivo, hash kada je potreban, napomenu o potpunosti i ograničenje objave.

Izvorna datoteka se ne mijenja. Radna i anonimizovana kopija imaju drugačiji naziv i vezu prema originalnom ID-u.

## 2. Nazivi radnih dokumenata

Preporučeni oblik:

`GF-[PREDMET]-[VRSTA]-YYYYMMDD-vMAJOR.MINOR.ext`

Primjer strukture, bez vezivanja za konkretan predmet:

`GF-CASE-001-matrica-dokaza-20260805-v1.0.csv`

## 3. Semantičko verzionisanje metodologije

- **MAJOR:** mijenja osnovna pravila, oznake ili pragove dokazivanja;
- **MINOR:** dodaje novi metod, obrazac ili kompatibilno pravilo;
- **PATCH:** ispravlja grešku, vezu, formulaciju ili primjer bez promjene značenja.

Svaka izmjena ima datum, autora/urednika, opis, razlog, povezanu studiju ili stres-test i uticaj na ranije dokumente.

## 4. Verzionisanje studije slučaja

- `0.x` — radni nacrt;
- `1.0` — prva kontrolisana javna verzija;
- `1.x` — novi dokaz dopunjava, ali ne mijenja glavni zaključak;
- `2.0` — novi dokaz materijalno mijenja zaključak ili strukturu nalaza.

Stara verzija se ne briše. Nova verzija sadrži tabelu promjena: tvrdnja, stari status, novi dokaz, novi status i posljedica po zaključak.

## 5. Status objave

`RADNO`, `NA KONTROLI`, `JAVNI NACRT`, `OBJAVLJENO`, `AŽURIRANO`, `ZATVORENO`, `POVUČENO UZ OBRAZLOŽENJE`.

## 6. Veza studije i metodologije

Studija slučaja može predložiti izmjenu metode, ali jedna studija sama ne dokazuje univerzalnost obrasca. Izmjena metodologije se prihvata nakon dokumentovanog problema, predložene korekcije, stres-testa i kontrole kompatibilnosti sa postojećim oznakama.

