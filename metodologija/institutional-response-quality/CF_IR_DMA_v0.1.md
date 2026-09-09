# CF Institutional Response Data & Measurement Architecture — v0.1

**Oznaka:** CF-IR-DMA 0.1  
**Status:** razvojna arhitektura — buduća sposobnost  
**Datum:** 9. septembar 2026.

## 1. Svrha

CF-IR-DMA definiše razvojnu arhitekturu za buduće skaliranje CF-IRQF mjerenja sa malih kalibracionih skupova na veće, višekanalne skupove institucionalnih odgovora.

Centralni princip:

> **CF definiše šta se mjeri; AI omogućava da se standardizovani protokol mjerenja primijeni u većem obimu.**

Veliki broj zapisa sam po sebi ne čini uzorak reprezentativnim. Statistički zaključak mora ostati ograničen dizajnom uzorka, pokrivenošću i kvalitetom podataka.

## 2. Ulazni kanali

Arhitektura mora podržati odvojeno označene izvore:

- `CITIZEN` — građani koji analiziraju vlastitu dokumentaciju i zasebno pristanu na doprinos minimalnog strukturisanog rezultata;
- `CSO_LEGAL_AID` — nezavisne organizacije, pravna pomoć, watchdog, istraživačke i druge organizacije koje zakonito raspolažu odgovarajućim korpusom;
- `INSTITUTION` — javne institucije koje obezbijede anonimizovane predmete, strukturisane evidencije ili kontrolisane uzorke;
- `RESEARCH_SAMPLE` — posebno dizajniran istraživački ili validacioni uzorak.

Podaci iz različitih kanala zadržavaju provenance. Doprinos podataka ne daje izvoru metodološku, validacionu ili publikacionu kontrolu.

## 3. Osnovni data model

Minimalna hijerarhija je:

```text
MATTER
  ↓
CASE
  ↓
SOURCE_RECORD
  ↓
DOCUMENT
  ↓
ANALYSIS
  ↓
SIGNAL / INDICATOR
```

- `MATTER_ID` povezuje širi građanski/institucionalni problem koji može proizvesti više različitih postupaka.
- `CASE_ID` označava jednu statističku jedinicu institucionalnog postupanja/odgovora.
- `SOURCE_RECORD` čuva odvojenu verziju istog predmeta pristiglu kroz konkretan kanal.
- dokumenti različitih izvora se ne stapaju bez provenance-a.

Povezani postupci pred različitim organima nisu automatski duplikati; mogu pripadati istom `MATTER_ID`, ali različitim `CASE_ID`.

## 4. Minimalni strukturisani zapis

Buduća implementacija treba, gdje je opravdano, predvidjeti najmanje:

```text
case_id
matter_id (ako postoji)
source_channel
collection_method
sampling_method
institution_id / institution_type
jurisdiction
period
document_completeness
questions_total
questions_answered
evidence_trace_status
IRA/FCA/domain signals
materiality
confidence
validation_level
human_verified
taxonomy_version
method_version
model_version (ako je AI korišten)
```

Raw dokument nije isto što i statistički doprinos. Minimalni anonimizovani strukturisani rezultat treba biti preferirani doprinos kada svrha ne zahtijeva čuvanje izvornog dokumenta.

## 5. Deduplikacija i case resolution

Osnovno pravilo:

> **Jedan stvarni institucionalni predmet = jedna statistička jedinica, ali može imati više nezavisnih izvora podataka i više verzija dokumentarnog traga.**

Sistem mora razlikovati:

- `CONFIRMED_MATCH`;
- `PROBABLE_MATCH`;
- `POSSIBLE_MATCH`;
- `NO_MATCH`.

Nesigurna podudarnost se ne spaja automatski. Službeni broj predmeta ne treba biti javni/analitički CF identifikator; CF koristi vlastiti pseudonimizovani `CASE_ID`. Matching podaci moraju biti odvojeni od istraživačkog sloja koliko god je moguće.

Deduplikacija mora koristiti hijerarhijski pristup: jaki identifikatori kada su zakonito dostupni, zatim kombinacije stabilnih karakteristika predmeta. Konkretna tehnička implementacija zahtijeva zaseban privacy/security dizajn.

## 6. Provenance i cross-source pravila

Spajanje `CASE_ID` ne znači spajanje izvora. Za svaki dokument i nalaz mora ostati vidljivo iz kojeg je kanala došao.

Obavezno pravilo:

> **Source absence is not document non-existence.**

`nije dostavio građanin ≠ dokument ne postoji`  
`nije dostavila institucija ≠ dokument ne postoji`

Ovo ostaje podređeno O/K/R/N i CF dokaznoj disciplini.

Multi-source podudaranje može služiti za cross-source validaciju: poređenje građaninu vidljivog dokumentarnog traga, institucionalnog spisa i nezavisnog posredničkog korpusa. Razlika između izvora je `SOURCE_DISCREPANCY` za provjeru, ne automatski dokaz propusta.

## 7. Brojanje i statistička disciplina

Sistem mora odvojeno prikazivati najmanje:

```text
SOURCE_RECORDS
UNIQUE_CASES
MULTI_SOURCE_CASES
```

Osnovni case-level indikatori koriste `UNIQUE_CASES` kao imenilac, osim kada metodologija eksplicitno definiše drugi nivo analize.

Self-selected građanski ili CSO uzorak ne smije se predstavljati kao reprezentativna statistika svih institucionalnih predmeta. Ispravna formulacija mora navesti populaciju stvarno analiziranih predmeta.

Podaci iz različitih kanala ne smiju se objediniti za populacionu inferenciju osim kada dizajn uzorka, coverage i uporedivost to opravdavaju.

Institucionalni agregati i FOI podaci mogu služiti kao `Institutional Data Layer` za razumijevanje populacije, denominatora i pokrivenosti; individualni/multi-source predmeti čine odvojeni `Case Evidence Layer`.

## 8. Potencijalni indikatori za skaliranje

Pored CF-IRQF indikatora, razvojno se mogu testirati:

- `Formal Closure Signal Rate` — udio analiziranih jedinstvenih predmeta sa potvrđenim FCA signalom;
- `Cross-Source Completeness Rate` — stepen podudarnosti relevantnog dokumentarnog traga između izvora;
- `Citizen-Visible Evidence Rate` — udio dokumentovanih institucionalnih radnji koje su identifikabilne iz građaninu dostupnog odgovora/dokumentacije;
- source-specific QCR/ETR/NER i drugi postojeći CF-IRQF indikatori.

Ovi indikatori nisu pravni skorovi i ne dokazuju nezakonitost, namjeru ili odgovornost.

## 9. Validation levels

Razvojna implementacija treba razlikovati kvalitet zapisa, npr.:

- `L0 USER_GENERATED` — AI/korisnička analiza bez nezavisne provjere;
- `L1 PROTOCOL_CHECKED` — prošla definisane automatske/metodološke kontrole;
- `L2 INDEPENDENTLY_REVIEWED` — kodiranje potvrdio nezavisni analitičar;
- `L3 RESEARCH_GRADE` — dio kontrolisanog uzorka sa dokumentovanim dizajnom i QA.

Konačne oznake i kriterijumi moraju se validirati prije produkcione upotrebe.

## 10. Privatnost i upravljanje podacima

Buduća implementacija mora koristiti privacy-by-design:

- odvojen pristanak za analizu i za statistički doprinos;
- data minimisation;
- de-identification/pseudonimizaciju;
- jasno prikazivanje korisniku šta se šalje u zbirni sistem;
- odvajanje `Identity/Matching Layer` od `Research/Analytics Layer`;
- ograničen pristup podacima za matching;
- posebna pravila za osjetljive kategorije predmeta;
- retention, correction, withdrawal i incident pravila prije produkcione implementacije.

Prije stvarnog centralnog prikupljanja potrebna je zasebna pravna, privacy i security provjera. Ovaj dokument ne utvrđuje pravnu osnovu za obradu.

## 11. Governance

Budući Data & Methodology Governance Protocol mora najmanje urediti:

- prihvat i odbijanje datasetova;
- provenance i integritet izvora;
- konflikte interesa;
- taxonomy/method/model versioning;
- deduplikaciju i korekcije;
- pravila validacije;
- pravo institucije na metodološki odgovor/ispravku činjenice bez prava veta na nalaz;
- pravila objavljivanja agregata i suppression pragove;
- audit trail metodoloških promjena.

Princip:

> **data contribution ≠ methodological control ≠ validation ≠ publication control**

## 12. Razvojni put

Predloženi razvojni redoslijed:

1. **multi-source calibration** — mali, raznovrstan skup za stabilizaciju instrumenta i inter-analyst provjeru;
2. **controlled multi-stakeholder pilot** — test građanskog, nezavisnog i institucionalnog ulaznog kanala;
3. **validated measurement protocol** — dokumentovana reproduktivnost i false-positive/negative kontrole;
4. **scaled multi-source collection** — dobrovoljno i kontrolisano povećanje broja predmeta;
5. **observatory capability** — longitudinalni agregati i source-specific poređenja;
6. **representative research** — populacioni zaključci samo iz posebno dizajniranih uzoraka kada uslovi to dozvole.

Početnih 30–50 predmeta, ako se koristi, predstavlja kalibracioni/validacioni skup, a ne osnov za tvrdnje o prevalenciji u RS/BiH.

## 13. Donorska i institucionalna primjena

Arhitektura omogućava model u kojem građani, nezavisne organizacije i javne institucije mogu učestvovati kao jasno označeni izvori podataka, dok CF zadržava jedinstveni measurement protocol i nezavisna pravila validacije.

Institucije se mogu uključiti kao `data and improvement partners`, uključujući institucionalni self-check i kontrolisane uzorke, bez pretvaranja doprinosa podataka u kontrolu nad metodologijom.

Cilj potencijalnog pilota nije dokazati da je neka institucija "loša", nego testirati da li se kvalitet institucionalnog odgovora može pouzdano, ponovljivo i skalabilno mjeriti i koristiti za poboljšanje građanske i institucionalne prakse.

## 14. Status

CF-IR-DMA 0.1 je razvojna arhitektura buduće sposobnosti. Ne znači da CF trenutno posjeduje centralni Data Hub, produkcioni sistem za crowdsourcing, pravno odobren sistem obrade osjetljivih podataka ili reprezentativni statistički dataset.