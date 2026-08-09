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

KAIT v0.1 ima status radnog modula u validaciji. [Prijedlog za Standard 3.3](kait/standard_v3.3_kandidat.md) ne mijenja važeći Standard 3.2 dok ne budu završeni dodatni regresioni i inter-analyst testovi na korpusima odobrenim za tu namjenu.

## Operativni ciklus

> predmet → centralno pitanje → tvrdnje → dokazi → praznine → intervencija → novi dokaz → kontrola → objava → učenje

Svaki novi odgovor ili dokument je novi dokazni unos. Prethodni nalaz se ne briše, nego dobija status: potvrđen, izmijenjen, opovrgnut, dopunjen ili i dalje otvoren.

## Obrasci

- [`obrasci/matrica_dokaza.csv`](obrasci/matrica_dokaza.csv)
- [`obrasci/registar_izvora.csv`](obrasci/registar_izvora.csv)
- [`obrasci/rokovnik.csv`](obrasci/rokovnik.csv)
- [`obrasci/dnevnik_ai_upotrebe.csv`](obrasci/dnevnik_ai_upotrebe.csv)

## Odnos prema postojećim dokumentima

Ovaj paket ne zamjenjuje `standard_otvorene_javne_politike.md`, `metodologija_gradjanske_forenzike.md`, `metod_disciplinovanog_administrativnog_pritiska.md` ni zajedničko forenzičko jezgro u `promptovi/00_forenzicko_jezgro.md`. On ih povezuje u operativni minimum koji se može primijeniti na svaki novi predmet.
