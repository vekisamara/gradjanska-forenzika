# Promptovi za građansku forenziku

Ovaj folder sadrži operativnu biblioteku za analizu upravnih akata, javnih izjava, dokaznih praznina, institucionalnih reakcija i kvantitativnih tvrdnji.

## Zajedničko pravilo

Svaki prompt mora primjenjivati `00_forenzicko_jezgro.md` (**GF-PROMPT-CORE 1.1**). Posebni prompt može proširiti zadatak, ali ne smije ukinuti obavezno razdvajanje činjenica, tvrdnji izvora, tumačenja, pretpostavki i nepoznatih okolnosti.

Kada materijal sadrži broj, procenat, stopu, prosjek, trend, poređenje, budžetski iznos, indikator, procjenu ili uzročnu tvrdnju, obavezno se dodaje `08_kvantitativni_modul.md` (**GF-PROMPT-QUANT 1.0**).

## Preporučeni redoslijed rada

1. `02_brza_provjera.md` — početna trijaža dokumenta.
2. `06_plan_dokazivanja.md` — definiše odlučne činjenice, potrebne dokaze, njihove izvore i redoslijed pribavljanja.
3. `01_analiza_rjesenja.md` — dubinska analiza akta i lanca pitanje–činjenica–dokaz–pravilo–obrazloženje–zaključak.
4. `08_kvantitativni_modul.md` — uslovni modul za brojčane, komparativne, prediktivne i uzročne tvrdnje.
5. `09_analiza_izvjestaja_o_radu.md` — specijalizovana analiza izvještaja o radu, učinka, indikatora i budžetske realizacije.
6. `disciplinovani-administrativni-pritisak/` — detektor formalizma, dokaz iza fraze, matrica neodgovorenih pitanja, rokovnik i eskalacija.
7. `04_foi_generator.md` — priprema preciznog zahtjeva za postojeće dokumente, evidencije i procesne tragove.
8. `05_urgencija_cutanje_uprave.md` — reakcija na propušten rok ili nerazumno odlaganje.
9. `03_pisanje_zalbe.md` — nacrt pravnog podneska zasnovan na prethodno utvrđenim činjenicama i dokazima.
10. `07_kontrolna_analiza.md` — nezavisni red-team pregled koji pokušava osporiti, ograničiti ili precizirati prvi nalaz.
11. `analiza-izjava-iz-medija/`, `izjave-funkcionera/`, `izborni-kontekst-2026/`, `analiza-medijske-manipulacije/` i `analiza-pr-saopstenja/` — specijalizovane analize javnih komunikacija.
12. [`kait/`](kait/README.md) — KAIT-00 do KAIT-10 za rekonstrukciju tvrdnji, ocjenu veze opravdanje–zaključak, Linkage Tracker i regresiono testiranje.
13. [`../metodologija/ppt/01_prompt_library_v0.1.md`](../metodologija/ppt/01_prompt_library_v0.1.md) — PPT-01 do PPT-16 za rekonstrukciju lanca PR → nabavka → ugovor/nalog → situacija/faktura → plaćanje.

Rani prototip revizora narativa povučen je u [`arhivu/`](../arhiva/prototipovi/dashboard/revizor_narativa_rani_prototip.md) i nije dio aktuelne kontrolisane biblioteke.

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

Nalazi kvantitativnog formalizma dobijaju oznake KF-01, KF-02... i moraju sadržati sporni podatak, stvarno značenje, nedostajući kontekst, neopravdani zaključak i potreban dokaz.

Odsustvo dokumenta nije automatski dokaz da dokument ne postoji.

## Izlazni standard

Kada je primjenjivo, rezultat sadrži:

1. predmet i centralno pitanje;
2. pouzdano utvrđene činjenice;
3. registar tvrdnji i dokaznu matricu;
4. procesne radnje i nedostajuće tragove;
5. uočene obrasce;
6. uzroke, posljedice i alternativna objašnjenja;
7. kvantitativnu matricu i nalaze KF;
8. nivo pouzdanosti;
9. sljedeći dokazni ili procesni korak;
10. test ponovljivosti.

## Privatnost

Prije unosa u AI ukloniti JMBG, brojeve ličnih dokumenata, privatne adrese, telefone, medicinske podatke i podatke o maloljetnicima kada nisu neophodni za javni interes. Izvorni dokument čuva se odvojeno od anonimizovane radne kopije.

Ova biblioteka podržava stub odgovorne AI pismenosti u okviru [`Democratic Resilience & AI Literacy Programa`](../program/README.md).
