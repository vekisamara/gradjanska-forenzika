# GFO MEDIA — PR Analysis v1.1 release manifest

**Datum:** 11. septembar 2026.
**Vrsta izmjene:** validated canonical Source update
**Status:** CURRENT — STABILAN

## Repository source of truth

Važeći tekst prompta nalazi se u:

`promptovi/analiza-pr-saopstenja/01_gradjanska_forenzicka_analiza_institucionalnog_pr_saopstenja.md`

Pri izvozu u GFO Media MASTER ili SHARED Project koristi naziv:

`13_ANALIZA_PR_SAOPSTENJA_v1_1.txt`

## Zamjena

Zamijeniti:

`13_ANALIZA_PR_SAOPSTENJA_v1_0.txt`

sa:

`13_ANALIZA_PR_SAOPSTENJA_v1_1.txt`

Ne dodavati obje verzije kao permanent Sources. V1.0 se može čuvati samo u istoriji repozitorija ili eksplicitno označenoj arhivi.

## Šta se ne mijenja

- Source 13 ostaje jedan od četiri canonical prompta;
- 0–3 scoring ostaje neizmijenjen;
- nivoi institucionalnog prikrivanja 0–6 ostaju neizmijenjeni;
- routing i fail-open pravila ostaju neizmijenjeni;
- Source 16 ostaje vlasnik ORS/FDS/SID/PDS/APD/SVD metrike;
- POG i PIU su kvalitativni izlazi, ne novi paralelni scoreovi;
- Sources 10–12 i 14–18 nisu izmijenjeni ovom revizijom.

## Validacioni dokaz

`metodologija/media-analysis/validation/pr_analysis_v1_1_validation_2026-09-11.md`

Validacija obuhvata pet heterogenih javnih PR predmeta, A/B poređenje sa v1.0, regresionu provjeru i korekcije nakon prvog testnog prolaza. Rezultat je `PASS` bez kritičnih grešaka.

## Post-deployment verification

Nakon zamjene provjeriti:

1. Source 13 se samodeklariše kao `GFO MEDIA — PR Analysis v1.1` i `CURRENT — STABILAN`;
2. v1.0 više nije učitan kao permanent Source;
3. Project Control routing pokazuje na v1.1;
4. Runtime routing pokazuje na v1.1;
5. POG i PIU nisu uvedeni kao numerički scoreovi;
6. Source 16 scoring je neizmijenjen;
7. canonical Sources 10–12 nisu izmijenjeni;
8. validation i case fajlovi nisu učitani kao permanent methodological Sources.

Očekivani rezultat: `PASS — GFO MEDIA PR Analysis v1.1 CURRENT / STABLE`.
