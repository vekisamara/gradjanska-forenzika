# AI protokol i promptovi

**Oznaka:** GF-MET-AI 1.1

## 1. Uloga AI-a

AI se koristi za ekstrakciju tvrdnji, poređenje verzija, strukturisanje hronologije, otkrivanje dokaznih praznina, pripremu kontrolnih pitanja i provjeru konzistentnosti. AI ne potvrđuje autentičnost dokumenta, važenje propisa, stvarni događaj ni konačnu pravnu kvalifikaciju.

## 2. Obavezni ulaz

Svaki zadatak treba da sadrži:

- jurisdikciju i datum analize;
- vrstu dokumenta i izvor;
- centralno pitanje;
- poznate činjenice i njihove izvore;
- jasno označene praznine;
- jedan primarni cilj izlaza;
- pravilo da se ništa ne dopunjava nagađanjem;
- zahtjev za citat i lokaciju u dokumentu kada je dostupna.

Primjenjuju se `promptovi/00_forenzicko_jezgro.md` i `13_standard_kvaliteta_promptova.md`, a za brojčane i uzročne tvrdnje i kvantitativni modul.

## 3. Standardna struktura prompta

Svaki složeni prompt treba eksplicitno ili putem nasljeđivanja sadržati:

> Context → Task → Evidence rules → Analytical tests → Output schema → Uncertainty → Self-check / Acceptance criteria

Ako jedan prompt pokušava proizvesti više nezavisnih rezultata, zadatak se dijeli u više promptova ili modula.

## 4. Standardni izlaz

1. predmet i centralno pitanje;
2. tvrdnje `T1…Tn`;
3. dokazna matrica;
4. lanac obrazloženja;
5. kontradikcije i izostavljene činjenice;
6. alternativna objašnjenja;
7. nedostajući dokazi;
8. nivo pouzdanosti i šta bi moglo promijeniti zaključak;
9. koraci potvrde/opovrgavanja;
10. lista tvrdnji koje zahtijevaju ljudsku provjeru.

## 5. Zabrane

AI ne smije:

- izmišljati citat, broj akta, datum, izvor ili pravnu normu;
- tretirati tvrdnju institucije kao utvrđenu činjenicu;
- iz odsustva dokumenta automatski zaključiti da radnja nije izvršena;
- pripisivati unutrašnju namjeru;
- davati brojčanu ocjenu bez kriterijuma i podataka;
- obrađivati nepotrebne osjetljive lične podatke;
- popunjavati odlučnu dokaznu prazninu opštim znanjem kada bi to moglo promijeniti zaključak.

## 6. Acceptance criteria

Prije završetka svaki složeni izlaz mora proći najmanje sljedeću provjeru:

- odgovoreno je na centralno pitanje;
- svaka ključna tvrdnja ima dokaz ili oznaku nepotvrđenosti;
- činjenica i tumačenje su razdvojeni;
- važan protivdokaz ili alternativno objašnjenje nisu ignorisani;
- zaključak nije širi od dokaza;
- neprovjereni pravni ili činjenični elementi su označeni;
- navedeno je šta zahtijeva ljudsku provjeru.

## 7. Dvostruka kontrola

Prvi prolaz gradi analizu. Drugi prolaz, uz kontrolni prompt, pokušava osporiti ili suziti zaključak. Čovjek zatim provjerava svaki ključni citat, broj, datum, pravni izvor i poveznicu prema originalu.

Za objavu, žalbu, pravnu strategiju ili nalaz koji može ozbiljno uticati na treće lice, drugi prolaz je obavezan.

## 8. Validacija promptova

Nova ili materijalno izmijenjena verzija složenog prompta testira se prema `14_validacija_promptova.md`. Stabilna verzija mora proći mali benchmark, bez kritičnih grešaka, uz dokumentovanu odluku o statusu.

Greška otkrivena u stvarnom radu koja zahtijeva izmjenu prompta postaje kandidat za trajni regresioni test.

## 9. Dnevnik AI upotrebe

Za objavljene ili složene predmete bilježe se datum, model/alati kada su poznati, oznaka prompta, opis ulaza, izlaz korišten u radu, ljudske korekcije i ime/verzija konačnog dokumenta. Osjetljivi ulazi se ne objavljuju.
