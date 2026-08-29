# GFO Negotiation & Institutional Response (NIR)

**Verzija:** 0.3  
**Status:** kandidat za operativnu validaciju  
**Datum:** 29. avgust 2026.

NIR je zaseban modul Građanske forenzike za pripremu i stres-test konkretne interakcije sa institucijom. Ne zamjenjuje Metod disciplinovanog administrativnog pritiska (MDAP) v3.2.

## Podjela odgovornosti

- **MDAP v3.2** upravlja činjenicama, dokaznim tragovima, prioritetima A/B/C, rokovima, procesnim okidačima i eskalacijom.
- **NIR** upravlja pregovaračkim ciljem, interesima, BATNA-om, leverage-om, opcijama, ustupcima, komunikacijom i simulacijom odgovora institucije.
- **Simulator** proizvodi samo hipoteze/scenarije i nikada ne stvara dokaz.

## Routing gate

NIR se ne aktivira automatski. Ako se sljedeći korak može riješiti jednim provjerljivim MDAP pitanjem, koristi se MDAP bez NIR-a. NIR se aktivira kada naredna interakcija uključuje izbor između više rješenja, kompromis, strateško otkrivanje informacija, sastanak, parcijalnu ponudu, neravnotežu pregovaračke moći ili deadlock koji možda može biti riješen bez formalne eskalacije.

## Obavezne zaštite

1. O/K/R/N status izvora iz MDAP-a je obavezujući.
2. Izvor statusa R ili N ne može biti tretiran kao potvrđena činjenica niti kao spreman leverage.
3. Prioritet A i zaštita od aktivne štete imaju prednost nad pregovaranjem.
4. NIR ne smije odgoditi pravni lijek niti pretpostaviti da razgovor ili sastanak zaustavlja zakonski rok.
5. NIR ne bira procesni instrument ili stepen eskalacije umjesto MDAP-a.
6. `[SIMULATION]` nikada ne postaje `[EVIDENCE]` bez nezavisne potvrde.
7. Motivi institucije se označavaju kao hipoteze dok nisu dokazani.

## Tok

`MDAP case state -> NIR routing gate -> NIR strategy -> institutional response simulator -> strategy review -> real interaction -> evidence/commitment ingest -> MDAP loop`

## Fajlovi

- `NIR_BASELINE_v0.3.md` — kanonska arhitektura i granice modula.
- `NIR_RUNTIME_v0.3.md` — izvršna pravila za AI.
- `NIR_CASE_STATE_PACKAGE_v0.3.md` — interfejs MDAP -> NIR.
- `NIR_INSTITUTIONAL_RESPONSE_SIMULATOR_v0.3.md` — red-team simulacija institucije.
- `NIR_STRATEGY_REVIEW_v0.3.md` — post-simulation revizija strategije.
- `NIR_INSTITUTIONAL_COMMITMENT_RECORD_v0.3.md` — zapis obaveza nastalih u stvarnoj komunikaciji.

Kanonska proceduralna metodologija ostaje `metodologija/osnovni-dokumenti/metod_disciplinovanog_administrativnog_pritiska_v3.2.md`.