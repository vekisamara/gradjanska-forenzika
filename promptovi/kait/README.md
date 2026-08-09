# GFO-KAIT Prompt Pack v0.1

## Univerzalni omotač

> Radi po Standardu Građanske forenzike 3.2 i KAIT v0.1. Ne izmišljaj činjenice, dokumente, propise, datume ni citate. Odvoji činjenicu, inferenciju, navod i nepoznato. Za svaki materijalni nalaz navedi izvor/lokator, O/K/R/N, D1–D5, pouzdanost, nedostatak i alternativno objašnjenje. D1–D5 ne koristi kao automatsku ocjenu zaključka. Kada spis ne daje odgovor napiši „nije utvrđeno“.

## Promptovi

### KAIT-00 — Brza trijaža tvrdnji

Izdvoji materijalno relevantne institucionalne tvrdnje. Za svaku navedi citat ili vjernu parafrazu, autora, lokator, vrstu, da li nosi odluku i prioritet A/B/C. Ne ocjenjuj još zakonitost.

### KAIT-01 — Rekonstrukcija argumenta

Za `[CLM-ID]` rekonstruiši: dokaz/norma → utvrđena činjenica → pretpostavka → ocjena organa → zaključak. Svaku nevidljivu vezu označi kao dokazni ili logički jaz.

### KAIT-02 — Sigurnost i domet

Utvrdi eksplicitni ili implicitni stepen sigurnosti i tačan domet tvrdnje. Navedi užu, oprezniju formulaciju koju raspoloživi dokaz može podržati.

### KAIT-03 — Registar pojmova i pretpostavki

Izdvoji ključne pojmove i implicitne premise. Za svaki navedi značenje u dokumentu, mogući normativni izvor, varijacije upotrebe i posljedicu ako premisa nije tačna.

### KAIT-04 — Deklarisana i operativna funkcija

Odvoji deklarisanu svrhu od dokumentovane operativne funkcije. Ne pripisuj motiv. Funkcionalnu interpretaciju označi kao hipotezu i navedi test.

### KAIT-05 — Protivdokaz i alternativa

Navedi dostupne protivdokaze, način na koji ih je organ tretirao, najmanje jedno neutralno alternativno objašnjenje i dokaz koji bi razlikovao tumačenja.

### KAIT-06 — Ocjena adekvatnosti

Ocijeni samo vezu opravdanje–zaključak: usklađeno, djelimično usklađeno, neusklađeno ili nije moguće ocijeniti. Odvojeno obrazloži sadržaj, sigurnost i domet. Ne izvodi ocjenu iz autoriteta dokumenta.

### KAIT-07 — Komparativna sinteza

Grupiši dokumente po materijalnim pitanjima. Za svako prikaži saglasne tvrdnje, kontradikcije, promjene stava, protivdokaze, status izvora i otvorenu prazninu.

### KAIT-08 — Linkage Tracker

Za svaki pasus, tabelu, dokaz i nalaz provjeri: zašto je tu; kojem pitanju doprinosi; koju tvrdnju podržava ili osporava; postoji li lokator; govori li zaključak više od dokaza.

### KAIT-09 — Samokritički završni izlaz

Napiši neutralan sažetak: šta je utvrđeno; šta je inferencija; koje tvrdnje su dobro ili slabo opravdane; šta nije moguće zaključiti; koji dokaz bi najviše smanjio neizvjesnost.

### KAIT-10 — Regresioni test

Samo kada postoji ručno validiran gold set: uporedi novi izlaz sa referentnom claim matricom i izračunaj pokrivenost lokatora, očuvanje O/K/R/N, lažne uzročne veze, propuštene protivdokaze i materijalne korekcije recenzenta.

## Orkestracija

Primijeni KAIT-00 na cijeli korpus. Za tvrdnje prioriteta A izvrši KAIT-01 do KAIT-06, zatim KAIT-07 i KAIT-08. Završni tekst generiši kroz KAIT-09. Aktiviraj STOP i ublaži nalaz ako nema lokatora, nedostaje relevantna norma ili ključni nalaz zavisi od R/N izvora. KAIT-10 koristi samo uz gold set, drugi analitički prolaz i dnevnik neslaganja.

## Kontrolni primjer

Ispravno je zaključiti da D1/O rješenje dokazuje šta je organ naveo, ali da spisak dokumenata neposredno potvrđuje njihovo postojanje, ne nužno sadržajnu potpunost ili ispunjenost svih uslova. Pogrešno je zaključiti: „Rješenje je D1, zato su svi uslovi nesporno ispunjeni.“

