# CF Institutional Response Quality Framework — Baseline v0.1

**Oznaka:** CF-IRQF 0.1  
**Status:** razvojni okvir — u kalibraciji  
**Datum:** 9. septembar 2026.

## 1. Svrha

CF-IRQF je metodološki okvir za strukturisanu, dokazno disciplinovanu analizu institucionalnih odgovora. Njegovo centralno pitanje je:

> **Da li je institucija proizvela odgovor koji je materijalno relevantan, individualizovan, dokazno povezan i provjerljiv — i da li formalno zatvaranje odgovara stvarnom stanju otvorenih pitanja?**

Okvir ne ocjenjuje automatski zakonitost odluke niti utvrđuje odgovornost službenika.

## 2. Naslijeđena pravila GF-MET

CF-IRQF obavezno nasljeđuje:

- dokaz ima prednost nad utiskom;
- zaključak mora biti uži ili jednak dokazima;
- odsustvo dostavljenog dokaza nije dokaz nepostojanja;
- tvrdnja institucije nije automatski utvrđena činjenica;
- ne pripisuje se namjera bez dokaza;
- aktivnost nije isto što i ishod;
- važan negativni nalaz mora razmotriti razumno alternativno objašnjenje;
- AI pomaže ekstrakciji, mapiranju i poređenju, ali čovjek potvrđuje ključne nalaze.

Koriste se D1–D5, O/K/R/N, GF-MET oznake sadržaja i statusa tvrdnji te QA pravila ponovljivosti.

## 3. Jedinica analize

Institucionalni odgovor se ne procjenjuje samo kao dokument u cjelini. Osnovni dokazni lanac je:

> **pitanje → činjenica/dokaz → institucionalna radnja → primijenjeni standard → razlog → zaključak → ishod**

Svaka karika se označava kao `prisutna`, `djelimična`, `nedostaje`, `kontradiktorna` ili `nije moguće ocijeniti`.

## 4. Response Decomposition Protocol

### 4.1 Request map

Iz podneska se izdvajaju materijalna pitanja/zahtjevi `P1…Pn`. Argumentacija i kontekst se odvajaju od provjerljivih pitanja.

### 4.2 Evidence map

Za svako pitanje bilježe se:

`P → dostavljeni dokaz → očekivani institucionalni trag → status izvora`

Očekivani trag mora biti formulisan kao dokument, evidencija, zabilješka, zapisnik, odluka, podatak ili izričito dokazivo negativno stanje — ne kao zahtjev za mišljenje.

### 4.3 Response map

Segmenti odgovora dobijaju `R1…Rn` i mapiraju se na pitanja:

`P1 → R3`  
`P2 → djelimično R4`  
`P3 → NO IDENTIFIED RESPONSE`

### 4.4 Action map

Tvrdnje o izvršenoj kontroli, uvidu, provjeri, prosljeđivanju, pribavljanju podataka ili preduzetoj mjeri mapiraju se na očekivani službeni trag. Razlikuju se najmanje:

- dokument postoji;
- dokument ne postoji;
- dokument nije pronađen;
- provjera/radnja nije izvršena;
- status nije moguće utvrditi iz dostupnog materijala.

### 4.5 Reason map

Kada institucija daje razlog za zaključak, analizira se veza:

`tvrdnja/zaključak → ponuđeni warrant → premise → protivdokaz → domet`

Ovaj korak koristi KAIT gdje je opravdanje materijalno sporno.

### 4.6 Closure map

Bilježe se:

`formalni status → odgovorena pitanja → otvorena pitanja → dokazne praznine → stvarni ishod`

Formalno zatvaranje samo po sebi nije dokaz materijalnog razrješenja.

## 5. Formal Closure Anomaly

**Formal Closure Anomaly (FCA)** je signal da je predmet formalno zaključen, odbijen, preusmjeren ili predstavljen kao riješen, dok jedno ili više materijalnih i provjerljivih pitanja ostaje bez jasnog razrješenja u dostupnom dokaznom tragu.

FCA ne dokazuje nezakonitost, namjeru, nesavjestan rad ili disciplinsku odgovornost. On označava nesklad koji zahtijeva ljudsku provjeru i, kada je procesno relevantno, MDAP procjenu.

## 6. Zajednički indikatori

Indikatori su pomoćni i ne predstavljaju pravni scoring.

- **Question Coverage Rate (QCR):** udio materijalnih pitanja sa identifikovanim odgovorom.
- **Evidence Trace Rate (ETR):** udio provjerljivih činjeničnih zaključaka za koje je identifikovan dokazni trag.
- **Evidence Responsiveness Rate (ERR):** udio relevantnih dostavljenih dokaza koji su vidljivo adresirani.
- **Specificity:** stepen individualizacije odgovora prema konkretnim pitanjima naspram generičkih formulacija.
- **New Evidence Responsiveness (NER):** da li novi materijalni dokaz proizvodi novu provjeru ili obrazloženu ponovnu procjenu.
- **Closure Integrity:** usklađenost formalnog zatvaranja sa stanjem otvorenih pitanja i dokaznih praznina.
- **Citizen Actionability:** može li primalac razumjeti šta je urađeno, šta je utvrđeno, na osnovu čega i šta slijedi.

Numeričke vrijednosti se ne koriste bez definisanog imenitelja, pravila kodiranja i validacionog protokola.

## 7. Dozvoljena uloga AI-a

AI može:

1. **Extract** — izdvojiti pitanja, tvrdnje, radnje, razloge i dokumentarne reference;
2. **Map** — povezati pitanje sa odgovorom i zaključak sa ponuđenim tragom;
3. **Compare** — porediti faze istog predmeta ili skup odgovora;
4. **Flag** — označiti kandidat-signal iz važeće taksonomije;
5. **Measure** — izračunati unaprijed definisane indikatore.

AI ne smije potvrditi autentičnost, pravnu valjanost, motiv, nezakonitost, disciplinski prekršaj ili korupciju.

## 8. Izlaz i provenance

Minimalni izlaz:

```text
[EVIDENCE] dokumentovani sadržaj i locator
[INFERENCE] ograničen zaključak izveden iz dokaza
[SIGNAL: IRA/FCA/DOMAIN CODE] definisani anomalijski signal
[MISSING EVIDENCE] konkretan trag koji bi mogao promijeniti nalaz
Pouzdanost: visoka / srednja / niska / neocjenjivo
Alternativno objašnjenje: kada je relevantno
Human check: obavezne tačke provjere
```

Ako se NIR aktivira, `[SIMULATION]` i `[STRATEGY]` ostaju odvojene kategorije; simulacija nikada nije dokaz.

## 9. Human Validation Gate

Prije high-impact ili javnog nalaza obavezno je:

`AI analiza → provjera citata/izvora → O/K/R/N i D1–D5 kontrola → alternativno objašnjenje → drugi analitički prolaz → potvrditi / suziti / odbaciti signal`

Signal koji zavisi od nedostupnog kompletnog spisa mora biti ograničen na dostupni materijal.

## 10. Odnos prema KAIT-u

KAIT pita da li ponuđeno opravdanje nosi sadržaj, sigurnost i domet institucionalne tvrdnje. CF-IRQF pita da li je odgovor kao institucionalni proizvod materijalno odgovorio na pitanje i ostavio provjerljiv trag.

Kada signal zavisi od adekvatnosti opravdanja, CF-IRQF poziva KAIT; ne uvodi konkurentski adequacy scoring.

## 11. Odnos prema MDAP-u i NIR-u

CF-IRQF ne bira pravni lijek, procesni instrument niti stepen eskalacije.

- **CF-IRQF:** kakav odgovor je proizveden i koji dokazni signal postoji;
- **MDAP:** šta treba dokazati, koji rok/prioritet postoji i koji procesni korak slijedi;
- **NIR:** kako voditi stvarnu interakciju kada routing gate to opravdava.

NIR ne smije odgoditi Priority A zaštitu, zakonski/procesni rok ili MDAP okidač.

## 12. Case-neutrality i privatnost

Baseline ne sadrži podatke stvarnih predmeta. Kalibracioni materijal vodi se odvojeno i nije dio javnog baseline-a. Osjetljivi testni podaci se ne objavljuju; javni benchmark može koristiti sintetičke ili posebno odobrene anonimizovane slučajeve.

## 13. Validacija prije stabilizacije

Za promociju iz `U VALIDACIJI` potrebno je najmanje:

- sadržajno raznovrstan testni set;
- pozitivni, negativni, granični i missing-evidence testovi;
- nula kritičnih grešaka prema GF-PROMPT-EVAL za povezane promptove;
- inter-analyst provjera najmanje dijela skupa;
- dokumentovane false-positive i false-negative kategorije;
- odluka uredništva i ažuriranje `STATUS.md` i `CHANGELOG.md`.

Stvarni kalibracioni predmeti nisu sastavni dio ovog javnog dokumenta.