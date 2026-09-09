# CF Institutional Response Quality Framework

**Oznaka paketa:** CF-IRQF 0.1  
**Status:** razvojni okvir — u kalibraciji  
**Datum:** 9. septembar 2026.

CF Institutional Response Quality Framework (CF-IRQF) je case-neutral razvojni okvir za analizu kvaliteta institucionalnih odgovora i integriteta formalnog zatvaranja predmeta.

Paket sadrži dvije domenske primjene:

- [`administrative/ARCM_BASELINE_v0.1.md`](administrative/ARCM_BASELINE_v0.1.md) — Administrative Response & Closure Monitor (ARCM);
- [`justice/JARM_BASELINE_v0.1.md`](justice/JARM_BASELINE_v0.1.md) — Justice Accountability Response Monitor (JARM).

Zajednički pojmovi i signalna taksonomija definisani su u:

- [`CF_IRQF_BASELINE_v0.1.md`](CF_IRQF_BASELINE_v0.1.md);
- [`RESPONSE_ANOMALY_TAXONOMY_v0.1.md`](RESPONSE_ANOMALY_TAXONOMY_v0.1.md).

Razvojna arhitektura za buduće skaliranje i višekanalno mjerenje definisana je u:

- [`CF_IR_DMA_v0.1.md`](CF_IR_DMA_v0.1.md) — CF Institutional Response Data & Measurement Architecture.

CF-IR-DMA predviđa odvojene ulazne kanale građana, nezavisnih organizacija/pravne pomoći, javnih institucija i kontrolisanih istraživačkih uzoraka; provenance, deduplikaciju, `MATTER → CASE → SOURCE_RECORD` model, privacy-by-design i zabranu populacionih zaključaka iz self-selected uzorka.

## Položaj u metodologiji

CF-IRQF nasljeđuje Povelju GF-MET, Standard dokazivanja, Standard označavanja, AI protokol, QA/ponovljivost i KAIT. Ne mijenja Standard 3.2 niti Metod disciplinovanog administrativnog pritiska (MDAP) 3.2.

MDAP ostaje nadređen za dokazni status, prioritete zaštite, rokove, očekivani službeni trag, procesne okidače, pravne/procesne instrumente i eskalaciju. NIR se uključuje samo nakon svog routing gate-a i ne može odgoditi MDAP zaštitu ili rok.

Operativno:

> odgovor → dekompozicija pitanja → dokazni trag → mapiranje razloga → signal anomalije → ljudska kontrola → MDAP posljedica → NIR samo ako je routing gate otvoren

## Obavezna granica

CF-IRQF procjenjuje kvalitet i provjerljivost odgovora. Ne utvrđuje samostalno zakonitost, disciplinski prekršaj, korupciju, motiv ili namjeru.

> **response quality ≠ legality ≠ misconduct**

AI rezultat je analitički signal. Nije dokaz sam po sebi.

## Case-neutrality

Ovi razvojni dokumenti ne sadrže imena stranaka, brojeve predmeta, adrese, citate iz prepoznatljivih postupaka niti druge podatke iz stvarnih slučajeva. Stvarni predmeti mogu se koristiti za internu kalibraciju i regresiono testiranje, ali se ne objavljuju kao dio ovog paketa. Javni testovi, ako budu objavljeni, moraju biti sintetički ili posebno odobreni i anonimizovani.

## Razvojni pravac

Mali početni skupovi (npr. 30–50 predmeta) tretiraju se kao kalibracioni/validacioni skupovi, ne kao reprezentativna statistika RS/BiH. Dugoročni pravac je validirani measurement protocol koji se može primjenjivati na veće višekanalne skupove, uz jasno razdvajanje `SOURCE_RECORDS`, `UNIQUE_CASES` i `MULTI_SOURCE_CASES`.

Preklapanje izvora nije samo problem deduplikacije: isti `CASE_ID` sa više odvojenih source zapisa može služiti za cross-source validaciju, pod uslovom da se očuva provenance i da odsustvo dokumenta iz jednog izvora nikada nije tretirano kao dokaz nepostojanja.

## Status

CF-IRQF, ARCM, JARM i zajednička taksonomija imaju status `U VALIDACIJI`. CF-IR-DMA 0.1 je razvojna arhitektura buduće sposobnosti. Ne tvrdi da CF trenutno ima produkcioni Data Hub, reprezentativni dataset ili pravno/tehnički odobren sistem centralnog prikupljanja podataka.