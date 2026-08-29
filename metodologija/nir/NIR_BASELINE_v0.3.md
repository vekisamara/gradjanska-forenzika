# NIR BASELINE v0.3

## 1. Status i svrha

GFO Negotiation & Institutional Response (NIR) je taktički modul za pripremu konkretne institucionalne interakcije. Njegov zadatak nije da utvrđuje zakonitost, korupciju, namjeru ili odgovornost, niti da zamijeni MDAP v3.2. NIR optimizuje način na koji se potvrđene činjenice, otvorena pitanja i proceduralna pozicija koriste u sastanku, dopisu ili pregovoru.

## 2. Nadređena metodologija

NIR je podređen Metodu disciplinovanog administrativnog pritiska v3.2 u pitanjima: dokaznog statusa, prioritetizacije zaštite, rokova, očekivanog službenog traga, procesnih okidača i eskalacije.

MDAP određuje: **šta treba dokazati i koji zakoniti procesni korak slijedi.**  
NIR određuje: **kako voditi konkretnu interakciju bez ugrožavanja dokazne i procesne pozicije.**

## 3. Routing gate

NIR se aktivira samo ako odgovor na najmanje jedno pitanje glasi DA:

1. Postoji li više realno prihvatljivih ishoda?
2. Postoji li mogućnost razmjene/ustupka?
3. Da li se priprema sastanak ili direktna komunikacija sa donosiocem odluke?
4. Da li treba odlučiti šta otkriti sada, a šta kasnije?
5. Postoji li parcijalna ponuda ili kompromis?
6. Postoji li neravnoteža moći koju treba taktički upravljati?
7. Postoji li deadlock koji možda može biti riješen bez aktiviranja narednog MDAP stepena?

Ako se cilj može ostvariti jednim optimalnim, provjerljivim pitanjem prema MDAP-u, NIR ostaje isključen.

## 4. Ulaz

NIR prima `NIR_CASE_STATE_PACKAGE` sa najmanje:
- aktivna šteta i prioritet A/B/C;
- trenutni MDAP stepen;
- potvrđene, sporne i nepoznate činjenice;
- status izvora O/K/R/N;
- otvorena pitanja;
- očekivani dokazni tragovi;
- negativni dokazi;
- rokovi;
- trenutni procesni okidač;
- pravne/procesne zaštite;
- dozvola za aktiviranje NIR-a: YES / CONDITIONAL / NO.

## 5. NIR izlaz

NIR proizvodi:
1. primary objective;
2. idealni i minimalno prihvatljivi ishod;
3. mapu pozicija i interesa;
4. BATNA i procjenu njene realne dostupnosti;
5. leverage map;
6. distributivna/integrativna/mješovita pitanja;
7. objektivne kriterijume;
8. opcije;
9. concession matrix;
10. communication plan;
11. response tree;
12. institutional response simulation;
13. strategy review;
14. meeting card / next-action card;
15. po stvarnoj interakciji: Institutional Commitment Record.

## 6. Leverage kategorije

- **D — Documentary:** potvrđen dokument ili negativni dokaz.
- **L — Legal:** provjeren pravni standard, odluka ili rok.
- **P — Procedural:** dostupna procesna mogućnost potvrđena MDAP-om.
- **I — Information:** relevantna potvrđena informacija koju druga strana možda ne koristi u trenutnoj poziciji.
- **R — Reputational:** mogućnost zakonite javne provjere; ne koristi se kao prijetnja.
- **A — Alternative:** BATNA, tj. održiva opcija bez dogovora.

Svaki leverage mora imati izvor i status. R/N leverage je samo kandidat, ne operativna poluga.

## 7. Concession discipline

Ustupak se ne preporučuje bez:
- procjene troška za korisnika;
- procjene vjerovatne vrijednosti za instituciju;
- reciprociteta;
- provjere da ne ugrožava pravo, rok ili dokaznu poziciju.

## 8. Evidence-state model

Simulator i strategija razlikuju najmanje:
- E1 dokument postoji;
- E2 dokument ne postoji;
- E3 dokument nije pronađen;
- E4 provjera nije izvršena.

Ovi scenariji ne smiju se stapati. Svaki proizvodi drugačiju taktičku i MDAP posljedicu.

## 9. Institutional Commitment Record

Stvarna izjava institucije kojom se preuzima konkretna obaveza evidentira se kao ICR sa akterom, radnjom, rokom, izvorom, O/K/R/N statusom i stanjem izvršenja. ICR nakon stvarne interakcije prelazi u MDAP dokazni spis.

## 10. Stop i handoff

NIR prekida taktičko pregovaranje i vraća predmet MDAP-u ako:
- aktivna šteta zahtijeva prioritet A;
- teče rok koji bi dalja komunikacija mogla ugroziti;
- nastao je procesni okidač za formalni instrument;
- institucija je dala konačno formalno izjašnjenje koje zahtijeva pravni lijek;
- BATNA ili ključna pretpostavka se pokaže nepostojećom;
- nastavak razgovora proizvodi samo dodatnu prepisku bez novog dokaza, ustupka ili zaštitnog učinka.

## 11. Provenance tags

Svi NIR izlazi koriste:
- `[EVIDENCE]` — sadržaj potvrđen izvornim dokazom;
- `[INFERENCE]` — razumno izveden zaključak;
- `[SIMULATION]` — hipotetička reakcija;
- `[STRATEGY]` — preporučeni potez.

`[SIMULATION]` se nikada ne smije citirati kao dokaz stvarnog ponašanja institucije.

## 12. Verziona kontrola

Ovaj baseline je v0.3 i kandidat je za praktičnu validaciju. Promjena MDAP procesnih pravila ne smije se uvoditi kroz NIR baseline; takva izmjena pripada MDAP metodologiji.