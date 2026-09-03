# GFO MEDIA — NARRATIVE SELECTION & OMISSION LAYER v1.1

**Uloga:** opcioni horizontalni sloj za analitičko obogaćivanje  
**Status:** CURRENT — CONTROLLED OPERATIONAL / OPTIONAL / NON-ELIMINATORY  
**Obuhvat:** javne izjave, medijski sadržaji, institucionalni PR i izborna komunikacija  
**Autoritet:** podređen GFO Media Project Control, Runtime pravilima i kanonskim promptovima 10–13  
**Nezavisnost od slučajeva:** specifikacija ne sadrži činjenice, aktere, institucije niti zaključke iz konkretnih slučajeva.

## 1. Svrha

Sloj provjerava da li komunikacija može proizvesti materijalno nepotpun ili iskrivljen ukupni utisak kroz selekciju činjenica, izostavljanje, framing, zavisnost od izvora ili gubitak sistemskog konteksta, čak i kada pojedinačne navedene činjenice nisu dokazano netačne.

Sloj dopunjuje, ali nikada ne zamjenjuje kanonsku analizu.

## 2. Obavezne zaštite

1. Izostavljanje samo po sebi nije dokaz namjere.
2. Vlasništvo, finansiranje, politička bliskost ili institucionalna pripadnost ne dokazuju manipulaciju konkretnog sadržaja.
3. Više prenosa jednog izvornog sadržaja nisu nezavisne potvrde.
4. Nedostajuća informacija nije prikrivanje bez dodatnog dokaza.
5. Ocjene opisuju karakteristike konkretnog sadržaja i dokazne strukture, ne motive ili osobine autora.
6. Nedostajuća činjenica mora biti materijalna za centralnu tvrdnju da bi uticala na ocjenu izostavljanja.
7. Svaki rezultat iznad 0 mora imati navedenu konkretnu dokaznu osnovu i objašnjenje materijalnosti.
8. Ovaj sloj ne mijenja, ne prosječuje i ne prepisuje kanonske scoring sisteme.

## 3. Novelty / Utility Gate

Sloj se pokreće tek nakon što postoji kanonska claim/evidence struktura. Vrati `NOT APPLICABLE` ako bi sloj samo ponovio postojeći nalaz. Vrati `PARTIAL` kada samo dio provjera daje novu i korisnu informaciju.

## 4. Dizajn metrike

### 4.1 Jedinstven smjer skale

Sve numeričke metrike koriste isti intuitivni smjer:

`0 = indikator nije utvrđen / nizak rizik`  
`4 = indikator je snažno izražen / visok rizik`

### 4.2 Confidence se ne ocjenjuje po svakoj metrici

Per-metric `LOW/MEDIUM/HIGH confidence` se ne koristi u glavnoj tabeli.

Umjesto toga:
- svaka metrika mora sadržati konkretnu dokaznu osnovu;
- ako nema dovoljno podataka za razumnu ocjenu, koristi se `N/A — INSUFFICIENT EVIDENCE`;
- nakon cijele tabele daje se jedan **UKUPNI NIVO POUZDANOSTI NALAZA**: `LOW / MEDIUM / HIGH`, uz obrazloženje;
- po potrebi se zasebno navode **DOKAZNA OGRANIČENJA**.

## 5. Procjene

### A. Omission Risk Score — ORS (0–4)

Mjeri da li identifikovani nedostajući kontekst materijalno mijenja tumačenje centralne tvrdnje.

- 0 — nije utvrđeno materijalno izostavljanje.
- 1 — nedostaje sporedni kontekst; centralno značenje ostaje uglavnom isto.
- 2 — nedostaje relevantan kontekst koji može promijeniti procjenu.
- 3 — ozbiljno izostavljanje; navedene činjenice mogu biti tačne, ali bez nedostajućeg konteksta nastaje materijalno drugačija slika.
- 4 — komunikacijski efekat u velikoj mjeri zavisi od izostavljanja identifikovanog ključnog konteksta.

Ocjena iznad 0 zahtijeva navođenje konkretne nedostajuće činjenice, dokumenta, poređenja ili konteksta.

### B. Framing Distortion Score — FDS (0–4)

Mjeri odstupanje između dokazne osnove i interpretativnog okvira koji stvaraju naslov, redoslijed informacija, etikete, pridjevi, kauzalni jezik, stepen sigurnosti ili naglašavanje.

- 0 — framing je proporcionalan dokazima.
- 1 — blago promotivno ili negativno naglašavanje.
- 2 — jasno selektivno uokviravanje.
- 3 — framing materijalno mijenja vjerovatno tumačenje dokaza.
- 4 — činjenice su dominantno organizovane tako da održavaju unaprijed zadat narativ iznad onoga što dokazi samostalno podržavaju.

### C. Source Independence Deficit — SID (0–4)

Mjeri manjak nezavisnosti dokaznih lanaca. Viša vrijednost znači veći deficit.

- 0 — više stvarno nezavisnih izvora uz provjerljiv primarni dokument/podatke.
- 1 — više nezavisnih izvora, ali bez pune primarne dokumentacije.
- 2 — djelimična nezavisna potvrda; značajan dio tvrdnje i dalje vodi do istog izvora.
- 3 — više distributera/prenosa bez materijalne nezavisne provjere.
- 4 — jedan izvorni lanac; nema nezavisne potvrde relevantne za centralnu tvrdnju.

Uvijek odvojeno prikaži `broj_objava` i `broj_nezavisnih_dokaznih_lanaca`.

### D. PR Dependency Score — PDS (0–4)

Mjeri zavisnost medijskog sadržaja od unaprijed pripremljene komunikacije zainteresovanog aktera.

- 0 — nezavisno razvijeno izvještavanje.
- 1 — PR/saopštenje je jedan od više nezavisno obrađenih izvora.
- 2 — PR je glavni izvor, ali postoje materijalne dodatne provjere.
- 3 — sadržaj gotovo u potpunosti reprodukuje izvorni narativ uz malo nezavisne provjere.
- 4 — sadržaj funkcioniše kao praktično preneseni PR predstavljen kao nezavisno izvještavanje.

Ako je predmet analize originalno PR saopštenje, PDS je `N/A — not applicable` i red se može izostaviti.

### E. Alternative Perspective Deficit — APD (0–4)

Mjeri nedostatak materijalno relevantnih perspektiva ili dokaza, a ne odsustvo proizvoljne političke „druge strane“.

Relevantne alternative mogu biti primarni dokument, pogođeni korisnici, ugovor, revizorski nalaz, tehnički zapis, finansijska realizacija, nezavisna ekspertiza ili drugi dokaz sposoban da testira centralnu tvrdnju.

- 0 — ključne relevantne perspektive/dokazi su zastupljeni.
- 1 — manji deficit.
- 2 — nedostaje jedna važna perspektiva ili klasa dokaza.
- 3 — nedostaje većina relevantnih nezavisnih perspektiva/dokaza.
- 4 — sadržaj je gotovo potpuno zatvoren unutar perspektive zainteresovanog aktera.

### F. Systemic Visibility Deficit — SVD (0–4)

Mjeri da li se događaj prikazuje kao izolovan iako ponovo provjereni prethodni dokazi mogu pokazivati širi obrazac.

- 0 — nema podržanog šireg obrasca relevantnog za sadržaj.
- 1 — moguća veza koja zahtijeva dodatnu provjeru.
- 2 — postoje najmanje dva uporediva, odvojena i dokumentovana događaja sa istim relevantnim indikatorom.
- 3 — dokumentovan ponavljajući mehanizam kroz više odvojenih slučajeva.
- 4 — sadržaj materijalno zanemaruje ili suprotstavlja se dobro dokumentovanom sistemskom kontekstu relevantnom za centralnu tvrdnju.

SVD koristi Baseline & Pattern Memory Layer kada je dostupan. Prethodni AI zaključak nije dovoljan; mora se ponovo provjeriti izvorni dokaz.

## 6. Klasifikacija tvrdnje

Po potrebi razlikovati:
- `FALSE CLAIM` — dokazi podržavaju zaključak da je tvrdnja netačna.
- `UNSUPPORTED CLAIM` — dostupni dokazi ne podržavaju tvrdnju dovoljno.
- `FRAMED CLAIM` — osnovna činjenica može biti podržana, ali framing prelazi ili preusmjerava njeno dokazno značenje.
- `OMISSION-DRIVEN CLAIM` — navedene činjenice mogu biti podržane, ali identifikovani izostavljeni materijalni kontekst mijenja ukupni utisak.

Visok ORS/FDS/APD/PDS/SID/SVD ne pretvara tvrdnju automatski u `FALSE CLAIM`.

## 7. Obavezni izlaz

Vrati status modula: `USED`, `PARTIAL`, `NOT APPLICABLE`, `INSUFFICIENT EVIDENCE` ili `UNAVAILABLE`.

| Metrika | Ocjena | Šta je utvrđeno | Zašto je materijalno |
|---|---:|---|---|
| ORS | 0–4 | ... | ... |
| FDS | 0–4 | ... | ... |
| SID | 0–4 | ... | ... |
| PDS | 0–4 | ... | ... |
| APD | 0–4 | ... | ... |
| SVD | 0–4 | ... | ... |

Ne prikazuj numeričku ocjenu kada nema dovoljno dokaza; koristi `N/A — INSUFFICIENT EVIDENCE` ili izostavi red ako metrika po prirodi nije primjenjiva.

Nakon tabele navedi:
- `CENTRALNI NALAZ`
- `PRIMARNO IZOSTAVLJANJE`, ako postoji
- `BROJ OBJAVA`
- `NEZAVISNI DOKAZNI LANCI`
- `ALTERNATIVNI FRAME / REKONSTRUKCIJA`
- `DOKAZI POTREBNI ZA POTVRDU ILI OSPORAVANJE`
- `UKUPNI NIVO POUZDANOSTI NALAZA: LOW/MEDIUM/HIGH`
- `DOKAZNA OGRANIČENJA`
- `DODATA ANALITIČKA VRIJEDNOST`

## 8. Odnos prema drugim slojevima

Sloj je dodatni i non-eliminatory. Kanonski promptovi za javne izjave, izborni sadržaj, medijsku manipulaciju i institucionalni PR mogu ga pozvati nakon sopstvene primarne analize. SVD može pozvati Baseline & Pattern Memory Layer.

Nijedan nalaz ovog sloja ne smije neprimjetno promijeniti postojeći kanonski scoring ili routing.

## 9. Maintenance record

### v1.0
- Uvedeni ORS, FDS, SIS, PDS, APD i SVD.
- Uvedena razlika između broja objava i nezavisnih dokaznih lanaca.
- Uvedena klasifikacija false/unsupported/framed/omission-driven.

### v1.1
- SIS zamijenjen sa `SID — Source Independence Deficit` kako bi sve numeričke skale koristile isti smjer: 0 = nizak indikator, 4 = visok indikator.
- Ukinut per-metric `Confidence` iz glavne tabele.
- Uveden jedan ukupni nivo pouzdanosti nalaza nakon kompletne metrike.
- `N/A` više ne dobija confidence vrijednost.
- Pojednostavljena tabela na četiri intuitivna polja.
- Dodata eksplicitna kategorija `N/A — INSUFFICIENT EVIDENCE` radi sprečavanja lažne preciznosti.
- Specifikacija ostaje nezavisna od konkretnih slučajeva.

### Controlled operational acceptance — 2026-09-03
- Practical regression test completed on a current institutional PR.
- The revised metric direction and single-confidence design produced clearer output than v1.0.
- Canonical prompt scores and routing remained unchanged.
- Unsupported intent and illegality inference remained blocked.
- Module accepted for controlled operational use in GFO Media v1.1; broader heterogeneous validation remains desirable before LOCKED status.
