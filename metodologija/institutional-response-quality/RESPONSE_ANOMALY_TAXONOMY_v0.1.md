# Response Anomaly Taxonomy v0.1

**Oznaka:** CF-IRQF-TAX 0.1  
**Status:** kandidat u validaciji  
**Datum:** 9. septembar 2026.

## 1. Svrha

Taksonomija definiše zajedničke signalne kategorije za CF-IRQF, ARCM i JARM. Signal označava provjerljiv obrazac u dostupnom materijalu. Ne predstavlja automatski nalaz nezakonitosti, loše namjere, korupcije ili odgovornosti.

Svaki signal mora navesti: materijalno pitanje, relevantni segment odgovora, dokazni locator, šta nedostaje, pouzdanost i alternativno objašnjenje kada je relevantno.

## 2. Zajednički signali

### IRA-01 — Question–Answer Mismatch

**Test:** materijalno pitanje je identifikovano, ali odgovor govori o drugom pitanju ili ne daje odgovor koji se može mapirati na njega.

**Ne koristiti kada:** odgovor je nepovoljan, ali jasno odgovara na pitanje.

### IRA-02 — Generic Rule Substitution

**Test:** opšti propis, princip, nadležnost ili standard naveden je umjesto individualizovanog objašnjenja kako se odnosi na konkretno pitanje i činjenice.

**Ne koristiti kada:** opšti standard je dovoljan jer nema sporne individualne činjenice ili je njegova primjena jasno objašnjena.

### IRA-03 — Evidence-Trace Gap

**Test:** odgovor sadrži provjerljivu činjeničnu tvrdnju ili tvrdnju o službenoj radnji, ali u dostupnom materijalu nije identifikovan očekivani trag koji bi je mogao provjeriti.

**Safeguard:** nedostupnost traga nije dokaz da trag ne postoji.

### IRA-04 — Selective Evidence Response

**Test:** materijalni dostavljeni dokaz ili protivdokaz nije vidljivo adresiran, iako bi mogao promijeniti zaključak ili njegov domet.

**Ne koristiti kada:** dokaz je nerelevantan ili je razumno obuhvaćen drugim obrazloženjem; razlog mora biti dokumentovan.

### IRA-05 — Issue Reframing

**Test:** odgovor preoblikuje prvobitno pitanje u užu, širu ili drugačiju kategoriju i zatim odgovara na preoblikovano pitanje, dok izvorno materijalno pitanje ostaje otvoreno.

**Safeguard:** legitimna pravna klasifikacija nije sama po sebi anomalija; potrebno je pokazati šta je time ostalo neodgovoreno.

### IRA-06 — Competence Deflection

**Test:** odgovor se oslanja na nenadležnost, ali ne daje dovoljno provjerljiv trag o tome šta je sa predmetom učinjeno ili koji je dalji institucionalni put, kada je to relevantno za konkretni postupak.

**Safeguard:** ovaj kod ne utvrđuje pravnu obavezu prosljeđivanja; pravna posljedica se određuje van CF-IRQF-a.

### IRA-07 — Activity–Outcome Substitution

**Test:** izvršena aktivnost, broj radnji ili postojanje administrativnog izlaza koristi se kao zamjena za dokaz stvarnog ishoda ili rješenja centralnog problema.

### IRA-08 — Repetition Without Reassessment

**Test:** nakon relevantnog novog dokaza ili činjenice ponavlja se prethodni zaključak bez vidljive nove provjere, procjene ili obrazloženja zašto novi materijal ne mijenja zaključak.

### IRA-09 — Unresolved Institutional Contradiction

**Test:** dva ili više službenih podataka, akata ili pozicija su materijalno nesaglasni, a odgovor koji se na njih oslanja ne razrješava niti ograničava kontradikciju.

## 3. Formal Closure Anomaly

### FCA-01 — Formal Closure / Substantive Openness

**Test:** predmet je formalno zatvoren, odbijen, proslijeđen ili predstavljen kao riješen, ali najmanje jedno centralno provjerljivo pitanje ostaje bez odgovora, dokaznog traga ili jasnog procesnog statusa.

**Obavezni uslov:** otvoreno pitanje mora biti materijalno za svrhu podneska; sitna ili retorička praznina nije dovoljna.

**Safeguard:** FCA-01 ne znači da je formalno zatvaranje pravno nevaljano.

## 4. Pravila kombinovanja

- Jedan segment može aktivirati više signalnih kodova samo ako svaki kod dodaje zasebnu analitičku informaciju.
- FCA-01 se koristi kao closure-level signal; ne zamjenjuje osnovni IRA kod koji objašnjava zašto je predmet substantivno otvoren.
- KAIT se koristi kada spor zavisi od veze warrant–claim, umjesto stvaranja duplog IRQF adequacy koda.
- Domenski ARCM/JARM kodovi mogu precizirati zajednički signal, ali ne smiju mijenjati njegovu definiciju.

## 5. Pouzdanost

- **visoka:** sadržaj i locator direktno zadovoljavaju test; nema poznate materijalne praznine koja bi vjerovatno promijenila klasifikaciju;
- **srednja:** signal je dobro podržan, ali nedostaje dio spisa, kontekst ili postoji realno alternativno objašnjenje;
- **niska:** radna hipoteza za ciljanu provjeru;
- **neocjenjivo:** nema dovoljno materijala za primjenu testa.

Pouzdanost signala nije isto što i težina izvora D1–D5 niti status izvora O/K/R/N.

## 6. Materiality gate

Signal se u sintezi označava kao:

- **M1 — nizak uticaj:** ne mijenja razumijevanje centralnog odgovora;
- **M2 — srednji:** utiče na jednu važnu komponentu odgovora;
- **M3 — visok:** mogao bi promijeniti zaključak, closure status ili mogućnost građanina da razumije šta je stvarno urađeno.

Materiality nije pravna kvalifikacija.

## 7. False-positive kontrola

Prije potvrde signala analitičar provjerava najmanje:

1. postoji li drugi segment istog odgovora koji rješava problem;
2. postoji li dokument iz paketa koji odgovor izričito inkorporira;
3. da li je navodno neodgovoreno pitanje uopšte materijalno i dovoljno određeno;
4. da li se očekuje dokument koji se u toj vrsti postupka stvarno proizvodi;
5. postoji li benigno objašnjenje koje dostupni dokaz jednako dobro podržava;
6. da li nedostaje dio spisa koji zahtijeva `MISSING EVIDENCE` umjesto potvrđenog signala.

## 8. Minimalni zapis signala

```text
Signal ID:
Pitanje / tvrdnja ID:
Response locator:
[EVIDENCE]:
Test koji je zadovoljen:
[MISSING EVIDENCE]:
Alternativno objašnjenje:
Pouzdanost:
Materiality:
Human-review status:
```

## 9. Validacija

Taksonomija ostaje `0.1 / U VALIDACIJI` dok nezavisni analitičari ne pokažu prihvatljivu ponovljivost klasifikacije na odvojenom testnom setu. Stvarni predmeti korišteni za internu kalibraciju nisu dio ovog dokumenta niti se objavljuju kroz ovaj paket.