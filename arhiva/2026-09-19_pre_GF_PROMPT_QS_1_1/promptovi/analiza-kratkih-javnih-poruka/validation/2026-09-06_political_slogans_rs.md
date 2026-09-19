# GF-SMA politička kalibracija — Opšti izbori 2026, Republika Srpska

**Datum testa:** 2026-09-06  
**Model:** GF-SMA 0.1 → korekcija na GF-SMA 0.2  
**Status:** validacioni uzorak, nije konačna naučna kalibracija

## Cilj

Provjeriti da li početni SMI model razlikuje legitimnu mobilizaciju i nužno slogansko pojednostavljivanje od poruka koje proizvode materijalno važan zaključak bez odgovarajuće dokazne osnove.

## Uzorak

Uzorak obuhvata potvrđene slogane i centralne kratke kampanjske poruke političkih subjekata u Republici Srpskoj u kampanji za Opšte izbore 2026. Izvori su zvanični stranački sajtovi i medijski izvještaji sa početka kampanje.

| # | Subjekt | Poruka | SMI/40 nakon kalibracije | Dominantni obrasci |
|---|---|---|---:|---|
| 1 | SNSD | „Uvijek uz narod, uvijek uz Srpsku“ | 16 | ABSOLUTISM, IDENTITY_CAPTURE, PRESUPPOSITION_LOADING |
| 2 | SDS | „Pravda se vraća u Srpsku“ | 22 | MORAL_CAPTURE, PRESUPPOSITION_LOADING, CAUSAL_COMPRESSION |
| 3 | SPS | „Porodica. Pravda. Ponos.“ | 8 | UNIVERSAL_VALUE_CAPTURE, EMOTIONAL_SUBSTITUTION |
| 4 | DNS–NPS | „Svoji na svome“ | 16 | IDENTITY_CAPTURE, PRESUPPOSITION_LOADING, BINARY_FRAMING |
| 5 | DNS–NPS | „Za snažnu Srpsku“ | 6 | IDENTITY/AFFILIATION, PERSUASION |
| 6 | Pokret Sigurna Srpska | „Sigurno“ | 7 | SEMANTIC_FOG, BRAND/WORDPLAY; nizak materijalni zaključak |
| 7 | Pokret Sigurna Srpska | „Sigurno premijer“ | 20 | FALSE_CERTAINTY, OUTCOME_AS_FACT, INSTITUTIONAL_CHAIN_DELETION |
| 8 | Ujedinjena Srpska | „Dobra. Prava. Zdrava.“ | 8 | SEMANTIC_FOG, UNIVERSAL_VALUE_CAPTURE |
| 9 | Volja naroda Srpske | „Nema izdaje!“ | 25 | EMPTY_ENEMY, BINARY_FRAMING, MORAL_CAPTURE, EMOTIONAL_SUBSTITUTION |
| 10 | SP–DEMOS–NDP | „Složno za Srpsku“ | 8 | IDENTITY/AFFILIATION, MOBILIZATION |
| 11 | Za pravdu i red | „Hrabro, sloboda nema cijenu“ | 12 | UNIVERSAL_VALUE_CAPTURE, EMOTIONAL_SUBSTITUTION, MOBILIZATION |
| 12 | Nebojša Vukanović | „Hrabro do konačne pobjede“ | 8 | MOBILIZATION, ASPIRATIONAL; CER nizak jer nije deklarativna izvjesnost |
| 13 | Narodni front | „Srpska koja radi, Srpska koja pobjeđuje“ | 16 | CAUSAL_COMPRESSION, IDENTITY_CAPTURE, ASPIRATIONAL/CLAIM hybrid |
| 14 | Narodni front | „Republika Srpska – ekonomski tigar i socijalni raj“ | 17 | EMOTIONAL_SUBSTITUTION, MANUFACTURED EXPECTATION, SEMANTIC COMPRESSION |

## Ključni nalazi

### 1. VER i OMI su u v0.1 bili preosjetljivi na samu kratkoću

Slogani poput „Dobra. Prava. Zdrava.“, „Složno za Srpsku“ ili „Za snažnu Srpsku“ imaju malo provjerljivog sadržaja, ali to samo po sebi ne znači visok manipulativni potencijal. Kratkoća je funkcionalna osobina slogana.

**Korekcija v0.2:** uveden MATERIALITY GATE. VER i OMI mogu biti visoki samo kada poruka proizvodi materijalno važan zaključak za koji nedostaje relevantna osnova ili kontekst.

### 2. Aspiracija je bila nedovoljno odvojena od proizvedene izvjesnosti

„Hrabro do konačne pobjede“ mobilizuje i cilja pobjedu, ali ne kaže da je pobjeda već sigurna. „Sigurno premijer“ predstavlja neizvjestan institucionalni ishod kao gotovo gotovu činjenicu.

**Korekcija v0.2:** CER dobija precizne anchor vrijednosti; aspiracija/mobilizacija po pravilu ostaje na 0–1, dok deklarativna izvjesnost neizvjesnog ishoda može doseći 4–5.

### 3. Pozitivna identitetska asocijacija nije isto što i identitetsko prisvajanje

„Za snažnu Srpsku“ i „Složno za Srpsku“ koriste kolektivni identitet, ali ne moraju nužno implicirati da su politički protivnici protiv Srpske. „Uvijek uz narod, uvijek uz Srpsku“ ide dalje jer apsolutnu lojalnost veže za konkretnog političkog aktera. „Nema izdaje!“ još snažnije gradi moralnu podjelu i praznog neprijatelja.

**Korekcija v0.2:** IDA i BIN dobijaju odvojene anchor kriterijume. Visoki BIN zahtijeva stvarnu ili implicitno konstruisanu suprotnu stranu.

## Najkorisniji kontrastni parovi za regresiono testiranje

### CER

- „Hrabro do konačne pobjede“ → aspiracija/mobilizacija → nizak CER.
- „Sigurno premijer“ → neizvjestan institucionalni ishod predstavljen kao izvjestan → visok CER.

### IDA/BIN

- „Za snažnu Srpsku“ → pozitivna identitetska asocijacija → nizak IDA/BIN.
- „Uvijek uz narod, uvijek uz Srpsku“ → jače prisvajanje lojalnosti → srednje/visok IDA.
- „Nema izdaje!“ → implicitna podjela lojalni/izdajnici → visok BIN i EMPTY_ENEMY.

### VER/OMI

- „Dobra. Prava. Zdrava.“ → semantički tanko, ali nizak materiality → nizak VER/OMI.
- „Sigurno premijer“ → zaključak o funkciji zavisi od izbornog i institucionalnog lanca → visokiji VER/OMI.

## Izvori uzorka

- SNSD, SDS, SPS, DNS–NPS, Pokret Sigurna Srpska, Ujedinjena Srpska i Volja naroda: izvještaji o sloganima i otvaranju kampanje 4.9.2026.
- SP–DEMOS–NDP: RTRS, „Složno za Srpsku“, 4.9.2026.
- Za pravdu i red / Nebojša Vukanović: zvanični sajt zapravduired.org i nebojsavukanovic.info, 4.9.2026.
- Narodni front: kampanjske poruke i program predstavljen 4.9.2026.

Relevantne javne adrese:

- https://zapravduired.org/vijesti/kampanja-je-pocela-upoznajte-nase-kandidate-i-program-2026
- https://nebojsavukanovic.info/
- https://sps.ba/porodica-pravda-ponos/
- https://lat.rtrs.tv/vijesti/vijest.php?id=658801

## Zaključak

GF-SMA 0.1 je dobro identifikovao najjače obrasce poput EMPTY_ENEMY, FALSE_CERTAINTY i PRESUPPOSITION_LOADING, ali je previše penalizovao semantičku prazninu tipičnu za slogan kao format.

GF-SMA 0.2 uvodi tri korekcije bez promjene osnovnih osam dimenzija: MESSAGE ROLE CLASSIFICATION, MATERIALITY GATE i preciznije anchor kriterijume za IDA/CER/BIN.

Model ostaje **U VALIDACIJI**. Za stabilizaciju su potrebni dodatni uzorci iz komercijalnog, aktivističkog i institucionalnog/javnog oglašavanja, kao i test međuanalitičke konzistentnosti.
