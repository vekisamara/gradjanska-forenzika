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

## Status

CF-IRQF, ARCM, JARM i zajednička taksonomija imaju status `U VALIDACIJI`. Ne mijenjaju važeće GF-MET standarde dok ne prođu dokumentovanu kalibraciju, regresiono testiranje i inter-analyst provjeru.