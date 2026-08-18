# Operativni standardi Građanske forenzike

**Oznaka paketa:** GF-MET 1.0  
**Status:** metodološka osnova  
**Datum:** 5. avgust 2026.  
**Urednik:** Velimir Šamara

Ovaj direktorij pretvara opšta načela Građanske forenzike u ponovljiv radni postupak. Dokumenti su opšti: ne sadrže dokazne zaključke iz pojedinačnih predmeta. Studije slučaja ostaju u `studije-slucaja/` i služe za testiranje i unapređivanje metode.

## Redoslijed korištenja

1. [`00_povelja_metodologije.md`](00_povelja_metodologije.md) — svrha, granice i obavezna načela.
2. [`01_standard_dokazivanja.md`](01_standard_dokazivanja.md) — šta se može tvrditi na osnovu kojeg dokaza.
3. [`02_standard_oznacavanja.md`](02_standard_oznacavanja.md) — jedinstvene oznake tvrdnji, izvora, statusa i pouzdanosti.
4. [`03_metod_analize_odgovora_i_pr_saopstenja.md`](03_metod_analize_odgovora_i_pr_saopstenja.md) — analiza službenih odgovora, javnih izjava i institucionalnog PR-a.
5. [`04_metod_zahtjeva_za_informacije.md`](04_metod_zahtjeva_za_informacije.md) — pretvaranje dokazne praznine u precizan zahtjev za postojeći zapis.
6. [`05_metod_rokova_i_urgencija.md`](05_metod_rokova_i_urgencija.md) — računanje, dokazivanje i praćenje rokova.
7. [`06_metod_eskalacije.md`](06_metod_eskalacije.md) — proporcionalni prelaz od razjašnjenja do javnog djelovanja.
8. [`07_ai_protokol_i_promptovi.md`](07_ai_protokol_i_promptovi.md) — dozvoljena uloga AI-a, obavezni ulazi i kontrola izlaza.
9. [`08_matrica_dokaza.md`](08_matrica_dokaza.md) — struktura registra tvrdnji i dokaza.
10. [`09_kontrola_kvaliteta_i_ponovljivost.md`](09_kontrola_kvaliteta_i_ponovljivost.md) — drugi analitički prolaz i kriterijumi objave.
11. [`10_sablon_studije_slucaja.md`](10_sablon_studije_slucaja.md) — standardni javni format studije slučaja.
12. [`11_registar_izvora_i_verzionisanje.md`](11_registar_izvora_i_verzionisanje.md) — porijeklo dokumenta, izmjene nalaza i verzije metodologije.
13. [`12_kait_kriticka_analiza_institucionalne_tvrdnje.md`](12_kait_kriticka_analiza_institucionalne_tvrdnje.md) — rekonstrukcija institucionalnih tvrdnji i provjera da li opravdanje nosi sadržaj, sigurnost i domet zaključka.
14. [`ppt/`](ppt/README.md) — PR-to-Payment Trace (GF-PPT 0.1), nezavisan modul u validaciji za povezivanje PR objave sa nabavkom, ugovorom, izvršenjem i plaćanjem.

KAIT v0.1 i GF-PPT 0.1 imaju status radnih modula u validaciji. [Prijedlog za Standard 3.3](kait/standard_v3.3_kandidat.md) ne mijenja važeći Standard 3.2 dok ne budu završeni dodatni regresioni i inter-analyst testovi na korpusima odobrenim za tu namjenu.

## Operativni ciklus

> predmet → centralno pitanje → tvrdnje → dokazi → praznine → intervencija → novi dokaz → kontrola → objava → učenje

Svaki novi odgovor ili dokument je novi dokazni unos. Prethodni nalaz se ne briše, nego dobija status: potvrđen, izmijenjen, opovrgnut, dopunjen ili i dalje otvoren.

## Obrasci

- [`obrasci/matrica_dokaza.csv`](obrasci/matrica_dokaza.csv)
- [`obrasci/registar_izvora.csv`](obrasci/registar_izvora.csv)
- [`obrasci/rokovnik.csv`](obrasci/rokovnik.csv)
- [`obrasci/dnevnik_ai_upotrebe.csv`](obrasci/dnevnik_ai_upotrebe.csv)

## Odnos prema postojećim dokumentima

Ovaj paket je operativni dio šireg [`Democratic Resilience & AI Literacy Programa`](../program/README.md). Primjenjuje se zajedno sa [`Standardom za analizu javnih odluka v3.2`](osnovni-dokumenti/standard_za_analizu_javnih_odluka_v3.2.md), [`Metodom disciplinovanog administrativnog pritiska v3.2`](osnovni-dokumenti/metod_disciplinovanog_administrativnog_pritiska_v3.2.md) i zajedničkim forenzičkim jezgrom u [`promptovi/00_forenzicko_jezgro.md`](../promptovi/00_forenzicko_jezgro.md).

Ranija objedinjena metodologija v2.0 povučena je u [`arhivu/`](../arhiva/metodologija/metodologija_gradjanske_forenzike_v2.0.md) radi sljedivosti i nije aktuelni standard.


## Hijerarhija i verzionisanje

GF-MET 1.0 je naziv operativnog paketa i organizacionog okvira. Unutar njega su Standard za analizu javnih odluka 3.2 i Metod disciplinovanog administrativnog pritiska 3.2 važeći osnovni dokumenti. Njihova verzija 3.2 ne znači da je GF-MET u verziji 3.2.

KAIT 0.1 i prijedlog Standarda 3.3 imaju status kandidata u validaciji. Civic Decision Engine koristi njihove strukture kao istraživački prototip, ali ne mijenja metodološki status nalaza. Jedini centralni registar statusa je [STATUS.md](../STATUS.md).

Promjena broja važeće verzije zahtijeva dokumentovane testove, zapis izmjena, uredničku odluku i ažuriranje registra statusa.
