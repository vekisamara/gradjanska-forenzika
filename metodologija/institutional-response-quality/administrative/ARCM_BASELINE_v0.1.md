# Administrative Response & Closure Monitor — Baseline v0.1

**Oznaka:** CF-ARCM 0.1  
**Status:** razvojni modul — u kalibraciji  
**Datum:** 9. septembar 2026.

## 1. Svrha

Administrative Response & Closure Monitor (ARCM) je domenska primjena CF-IRQF-a za odgovore organa uprave, inspekcija, komunalnih službi, upravnih odjeljenja, FOI tijela i drugih javnih službi.

Centralno pitanje:

> **Da li je organ samo proizveo administrativni izlaz ili je dao provjerljiv odgovor na materijalno pitanje iz predmeta?**

ARCM ne utvrđuje samostalno zakonitost, obavezu službenika, disciplinsku odgovornost ili namjeru.

## 2. Naslijeđeni standardi

ARCM obavezno koristi:

- CF-IRQF Response Decomposition Protocol;
- CF-IRQF-TAX zajedničke IRA/FCA kodove;
- GF-MET dokazne nivoe D1–D5 i O/K/R/N;
- razlikovanje `dokument nije dostavljen / nije pronađen / organ tvrdi da ne postoji / provjera nije izvršena`;
- KAIT kada treba ocijeniti da li ponuđeno opravdanje nosi zaključak;
- MDAP za rokove, očekivani dokazni trag, procesni instrument i eskalaciju.

## 3. Minimalni ARCM ulaz

- podnesak ili precizna lista materijalnih pitanja;
- institucionalni odgovor;
- dokumenti na koje se odgovor poziva kada su dostupni;
- relevantni prethodni/naknadni odgovori ako se analizira ponovna procjena;
- status izvora i jasno označene dokazne praznine.

Bez ključnog dijela spisa nalaz se ograničava na dostupni materijal.

## 4. Administrativni domenski signali

### A-01 — Formal Record Dominance

Formalni podatak ili evidencijska oznaka koristi se kao dovoljan zaključak iako postoji materijal koji upućuje da stvarno ili drugo službeno stanje zahtijeva dodatnu provjeru.

**Safeguard:** ne pretpostavlja se da je organ pravno morao zanemariti evidenciju; signal samo označava neadresiranu dokaznu napetost.

### A-02 — Inspection / Action Without Trace

Odgovor navodi pregled, kontrolu, provjeru ili drugu službenu radnju, ali u dostupnom materijalu nije identifikovan očekivani službeni trag.

**Safeguard:** nedostupan zapis nije dokaz da zapis ne postoji.

### A-03 — Referral Loop

Predmet ili pitanje se ponavljano preusmjerava između organa, a iz dostupnog traga nije jasno ko preuzima provjerljivo materijalno pitanje niti koji je njegov status.

### A-04 — Competence Fragmentation

Više organa daje tačne ili moguće tačne odgovore o uskim segmentima nadležnosti, ali centralno pitanje ostaje bez institucionalnog vlasnika ili provjerljivog razrješenja.

**Safeguard:** fragmentacija organizacije sama po sebi nije nepravilnost; potrebno je pokazati posljedicu na konkretno materijalno pitanje.

### A-05 — Evidence Burden Transfer

Od građanina se traži da dostavi dokaz ili podatak koji je u istom institucionalnom sistemu potencijalno službeno provjerljiv, a odgovor ne pokazuje da li je mogućnost službene provjere razmotrena.

**Safeguard:** ovaj signal ne utvrđuje pravnu dužnost organa da pribavlja dokaz po službenoj dužnosti. To se provjerava zasebno.

### A-06 — New Evidence / No Reassessment

Novi materijalni dokaz ne proizvodi vidljivu novu provjeru, obrazloženu procjenu ili objašnjenje zašto ne mijenja raniji zaključak.

### A-07 — Administrative Output Substitution

Dopis, kontrola, nalog, prosljeđivanje, broj izvršenih radnji ili drugi administrativni izlaz predstavljen je kao dokaz da je centralni problem riješen bez zasebnog dokaza o ishodu.

## 5. ARCM analiza

Radni tok:

1. označiti `P1…Pn` materijalna pitanja;
2. mapirati dostavljene dokaze i očekivane službene tragove;
3. označiti `R1…Rn` relevantne segmente odgovora;
4. izvršiti P→R mapiranje;
5. provjeriti tvrdnje o službenim radnjama;
6. provjeriti nove dokaze i kontradikcije;
7. primijeniti zajedničke IRA/FCA i, gdje opravdano, A-kodove;
8. izvršiti false-positive kontrolu;
9. izraditi ograničeni nalaz i predati procesnu posljedicu MDAP-u.

## 6. Preporučeni izlaz

```text
Centralno pitanje:
Pitanja: P1…Pn
Question coverage:
Ključni dokazni tragovi:
Zajednički signali: IRA/FCA
ARCM signali: A-XX
[MISSING EVIDENCE]:
Alternativno objašnjenje:
Pouzdanost / materiality:
Šta se može tvrditi:
Šta se ne može tvrditi:
MDAP handoff: činjenica/praznina koja zahtijeva procesnu procjenu
```

ARCM ne generiše automatski urgenciju, žalbu ili eskalaciju. MDAP određuje da li i koji instrument slijedi.

## 7. Institucionalni self-check

ARCM se može koristiti i kao pre-dispatch kontrola kvaliteta odgovora:

- jesu li sva materijalna pitanja prepoznata;
- je li jasno šta je organ stvarno uradio;
- postoji li provjerljiv trag za ključne činjenične zaključke;
- je li relevantni novi dokaz adresiran;
- je li nenadležnost/prosljeđivanje objašnjeno na način koji omogućava praćenje statusa;
- razlikuju li se aktivnost i stvarni ishod;
- može li građanin razumjeti šta je utvrđeno i šta slijedi.

## 8. Granice javnog poređenja

Poređenje institucija ili organizacionih jedinica ne smije koristiti zbirni skor bez unaprijed definisanog uzorka, kodiranja, imenitelja, perioda, kontrole različitih vrsta predmeta i objavljene metodologije. Pojedinačni signal nije rang institucije.

## 9. Case-neutrality i validacija

Baseline je case-neutral. Stvarni predmeti korišteni za razvoj, kalibraciju ili regresiono testiranje nisu dio javnog paketa. ARCM ostaje `U VALIDACIJI` dok ne prođe sadržajno raznovrstan testni set, inter-analyst provjeru i dokumentovanu kontrolu false-positive nalaza.