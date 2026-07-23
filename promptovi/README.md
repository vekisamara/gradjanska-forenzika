# Promptovi za građansku forenziku

Ovaj folder sadrži operativnu biblioteku za analizu upravnih akata, javnih izjava, dokaznih praznina i institucionalnih reakcija.

## Zajedničko pravilo

Svaki prompt mora primjenjivati `00_forenzicko_jezgro.md` (**GF-PROMPT-CORE 1.0**). Posebni prompt može proširiti zadatak, ali ne smije ukinuti obavezno razdvajanje činjenica, tvrdnji izvora, tumačenja, pretpostavki i nepoznatih okolnosti.

## Preporučeni redoslijed rada

1. `02_brza_provjera.md` — početna trijaža dokumenta.
2. `06_plan_dokazivanja.md` — definiše odlučne činjenice, potrebne dokaze, njihove izvore i redoslijed pribavljanja.
3. `01_analiza_rjesenja.md` — dubinska analiza akta i lanca pitanje–činjenica–dokaz–pravilo–obrazloženje–zaključak.
4. `disciplinovani-administrativni-pritisak/` — detektor formalizma, dokaz iza fraze, matrica neodgovorenih pitanja, rokovnik i eskalacija.
5. `04_foi_generator.md` — priprema preciznog zahtjeva za postojeće dokumente, evidencije i procesne tragove.
6. `05_urgencija_cutanje_uprave.md` — reakcija na propušten rok ili nerazumno odlaganje.
7. `03_pisanje_zalbe.md` — nacrt pravnog podneska zasnovan na prethodno utvrđenim činjenicama i dokazima.
8. `07_kontrolna_analiza.md` — nezavisni red-team pregled koji pokušava osporiti, ograničiti ili precizirati prvi nalaz.
9. `analiza-izjava-iz-medija/`, `izjave-funkcionera/`, `izborni-kontekst-2026/`, `analiza-medijske-manipulacije/` i `analiza-pr-saopstenja/` — specijalizovane analize javnih komunikacija.
10. `dashboard/revizor_narativa.md` — poređenje javnog narativa sa dokumentima i priprema indikatora.

## Građanski forenzički ciklus

> problem → uzroci → akteri → dokazi → analiza → intervencija → rezultat → učenje

Prompt nije završen objavljivanjem zaključka. Novi dokument ili odgovor mora se uporediti sa prethodnim nalazom i označiti kao: potvrđeno, izmijenjeno, opovrgnuto, novo ili i dalje otvoreno.

## Dokazni standard

Svaka važna tvrdnja dobija oznaku T1, T2, T3... i vezu sa konkretnim dokazom. Obavezni statusi su:

- potvrđeno;
- djelimično potvrđeno;
- nepotvrđeno;
- kontradiktorno;
- opovrgnuto;
- nije moguće provjeriti.

Odsustvo dokumenta nije automatski dokaz da dokument ne postoji.

## Izlazni standard

Kada je primjenjivo, rezultat sadrži:

1. predmet i centralno pitanje;
2. pouzdano utvrđene činjenice;
3. registar tvrdnji i dokaznu matricu;
4. procesne radnje i nedostajuće tragove;
5. uočene obrasce;
6. uzroke, posljedice i alternativna objašnjenja;
7. nivo pouzdanosti;
8. sljedeći dokazni ili procesni korak;
9. test ponovljivosti.

## Privatnost

Prije unosa u AI ukloniti JMBG, brojeve ličnih dokumenata, privatne adrese, telefone, medicinske podatke i podatke o maloljetnicima kada nisu neophodni za javni interes. Izvorni dokument čuva se odvojeno od anonimizovane radne kopije.