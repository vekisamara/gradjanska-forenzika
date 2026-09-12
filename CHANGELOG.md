# Istorija promjena

Sve značajne promjene javne metodologije, promptova, alata, dokumentacije i strukture repozitorija bilježe se ovdje.

Format prati principe Keep a Changelog, uz odvojeno označavanje statusa metodoloških dokumenata.

## [Neobjavljeno]

### Dodano

- 11. septembar 2026: canonical `GFO MEDIA — PR Analysis v1.1` proširen forenzičkim komunikacijskim lancem, CLAIMED/SUPPORTED/OMITTED/IMPLIED razdvajanjem, kvalitativnim POG i PIU izlazima, benchmark testom superlativa i uslovnom analizom tajminga, ponavljanja i distribucije; dodat petoslučajni A/B/regresioni validacioni zapis prema GF-PROMPT-EVAL 1.0.
- 29. avgust 2026: dodat `GFO Negotiation & Institutional Response (NIR) v0.3` kao zaseban kandidat za operativnu validaciju; modul je podređen MDAP v3.2 za dokazni status, prioritete zaštite, rokove, procesne okidače i eskalaciju, a uvodi pregovarački routing gate, BATNA/leverage/concession sloj, institutional-response simulator, strategy review, MDAP→NIR case-state interfejs i Institutional Commitment Record;
- 26. avgust 2026: `GFO Media — Epistemic & Intent Layer v1.0` prihvaćen za operativnu upotrebu nakon pet slučajeva validacije; modul je CURRENT, funkcionalan, opcionalan i non-eliminatory, uz obavezni Novelty / Utility Gate, fail-open pravilo, zabranu paralelnog scoringa i anti-duplication safeguard;
- 26. avgust 2026: u `metodologija/media-analysis/validation/` dodan operational acceptance record za Epistemic & Intent Layer v1.0; ISSUE-EBCJ-001 i ISSUE-EBCJ-002 zatvoreni;
- 23. avgust 2026: u statusni registar dodani GF-PROMPT-QS 1.0 i GF-PROMPT-EVAL 1.0 kao važeći prompt governance slojevi;
- 23. avgust 2026: PPTC (Parallel Proceedings / Temporal Consistency Check) evidentiran kao važeće metodološko pravilo koje čeka punu kodifikaciju u narednoj konsolidovanoj verziji;
- 18. avgust 2026: GF-PPT 0.1 kao nezavisan modul u validaciji, sa metodom, bibliotekom od 16 promptova, Project Card obrascem i validacionim slučajem Čokorska Polja–Goleši;
- centralni registar statusa i verzija;
- razvojni plan;
- pravila doprinosa i sigurnosna politika;
- matrica licenciranja;
- git zaštita lokalnih dokaza, tajni i generisanih evidencija;
- standardizovani akademski metapodaci za citiranje.

### Promijenjeno

- 12. septembar 2026: javni repozitorij razgraničen je od internog organizacionog razvoja. Materijali povezani sa formiranjem buduće NVO, internim strateškim planiranjem i konceptom istraživačkog centra uklonjeni su iz javnog stabla i vode se odvojeno; javna metodologija, promptovi, alati, publikacije, studije slučaja i analize ostaju u ovom repozitoriju. `README.md`, `metodologija/README.md`, `STATUS.md` i `ROADMAP.md` usklađeni su sa novom granicom javnog repozitorija. Ova promjena ne mijenja važeći Standard 3.2, MDAP 3.2, canonical prompt scoring niti status operativnih GFO Media modula.
- 11. septembar 2026: Source 13 ažuriran sa `13_ANALIZA_PR_SAOPSTENJA_v1_0.txt` na `13_ANALIZA_PR_SAOPSTENJA_v1_1.txt`; postojeća 0–3 skala, nivoi prikrivanja 0–6, canonical routing i Source 16 scoring ostali su neizmijenjeni. Nakon prvog testnog prolaza komunikacijski lanac ograničen je na materijalne redove, IMPLIED je vezan za konkretan lokator, a POG je eksplicitno isključen iz dvostrukog bodovanja.
- 29. avgust 2026: NIR granica odgovornosti usklađena sa MDAP v3.2: NIR više ne bira procesni instrument ili stepen eskalacije i ne duplira Protokol jednog pitanja, kvantitativni modul, status izvora O/K/R/N ili MDAP stres-test;
- 26. avgust 2026: GFO Media Epistemic & Intent Layer promovisan iz maintenance-tested v0.1.1 u operativni v1.0; canonical prompts `10–13`, Media Runtime v1.0, scoring i source hierarchy ostali su neizmijenjeni;
- 23. avgust 2026: `STATUS.md` usklađen sa kanonskim `GF-PROMPT-CORE 1.2` od 22. avgusta 2026; prethodni registar je još navodio CORE 1.1;
- 23. avgust 2026: statusni registar precizira odnos CURRENT core metodologije prema PPTC, KAIT-u i GF-PPT-u;
- objašnjen odnos GF-MET 1.0, Standarda 3.2 i KAIT-a;
- usklađene licence metodologije, publikacija i koda.

## Pravila

Svaka naredna stavka treba da navede datum, verziju ili commit, pogođene dokumente i da li mijenja važeći status.
