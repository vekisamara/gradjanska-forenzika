# AI protokol i promptovi

**Oznaka:** GF-MET-AI 1.0

## 1. Uloga AI-a

AI se koristi za ekstrakciju tvrdnji, poređenje verzija, strukturisanje hronologije, otkrivanje dokaznih praznina, pripremu kontrolnih pitanja i provjeru konzistentnosti. AI ne potvrđuje autentičnost dokumenta, važenje propisa, stvarni događaj ni konačnu pravnu kvalifikaciju.

## 2. Obavezni ulaz

Svaki zadatak treba da sadrži:

- jurisdikciju i datum analize;
- vrstu dokumenta i izvor;
- centralno pitanje;
- poznate činjenice i njihove izvore;
- jasno označene praznine;
- cilj izlaza;
- pravilo da se ništa ne dopunjava nagađanjem;
- zahtjev za citat i lokaciju u dokumentu.

Primjenjuje se `promptovi/00_forenzicko_jezgro.md`, a za brojčane i uzročne tvrdnje i kvantitativni modul.

## 3. Standardni izlaz

1. predmet i centralno pitanje;
2. tvrdnje `T1…Tn`;
3. dokazna matrica;
4. lanac obrazloženja;
5. kontradikcije i izostavljene činjenice;
6. alternativna objašnjenja;
7. nedostajući dokazi;
8. nivo pouzdanosti;
9. koraci potvrde/opovrgavanja;
10. lista tvrdnji koje zahtijevaju ljudsku provjeru.

## 4. Zabrane

AI ne smije:

- izmišljati citat, broj akta, datum, izvor ili pravnu normu;
- tretirati tvrdnju institucije kao utvrđenu činjenicu;
- iz odsustva dokumenta automatski zaključiti da radnja nije izvršena;
- pripisivati unutrašnju namjeru;
- davati brojčanu ocjenu bez kriterijuma i podataka;
- obrađivati nepotrebne osjetljive lične podatke.

## 5. Dvostruka kontrola

Prvi prolaz gradi analizu. Drugi prolaz, uz kontrolni prompt, pokušava osporiti ili suziti zaključak. Čovjek zatim provjerava svaki ključni citat, broj, datum, pravni izvor i poveznicu prema originalu.

## 6. Dnevnik AI upotrebe

Za objavljene ili složene predmete bilježe se datum, model/alati kada su poznati, oznaka prompta, opis ulaza, izlaz korišten u radu, ljudske korekcije i ime/verzija konačnog dokumenta. Osjetljivi ulazi se ne objavljuju.

