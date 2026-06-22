# Alati za građansku forenziku

Folder `alati/` sadrži lokalne softverske alate za tehničku provjeru dokumenata. Osnovno pravilo je da se osjetljivi dokumenti prvo obrađuju lokalno, prije bilo kakvog slanja prema vanjskim servisima ili AI modelima.

## Trenutni alat

### `forenzika_pdf.py`

Python skripta za ekstrakciju PDF metapodataka. Alat čita PDF dokument i prikazuje:

- naziv fajla,
- broj stranica,
- autora dokumenta,
- aplikaciju kojom je dokument kreiran,
- softver koji je proizveo PDF,
- datum kreiranja,
- datum izmjene,
- dodatne skrivene PDF tagove.

Ovaj alat je koristan kada se želi provjeriti digitalni trag dokumenta, posebno kod javnih akata, rješenja, dopisa i odgovora organa vlasti.

## Instalacija

```bash
python -m venv .venv
source .venv/bin/activate
pip install pypdf
```

Na Windows sistemu aktivacija virtualnog okruženja može izgledati ovako:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pypdf
```

## Pokretanje

```bash
python forenzika_pdf.py
```

Nakon pokretanja unesite putanju do PDF dokumenta.

## Pravila tumačenja

Metapodaci nisu sami po sebi dokaz nezakonitosti. Oni su digitalni trag koji može otvoriti dodatna pitanja:

- Da li se autor računara razlikuje od potpisnika akta?
- Da li je dokument nastao u neočekivanoj aplikaciji ili kod trećeg lica?
- Da li je datum izmjene neobičan u odnosu na datum akta?
- Da li je dokument očišćen od metapodataka?

Nalaz iz alata treba kombinovati sa sadržajem akta, brojem protokola, potpisom, pečatom, pravnim osnovom i službenom prepiskom.

## Privatnost

Ne objavljujte neobrađene dokumente koji sadrže JMBG, broj lične karte, privatnu adresu, privatni telefon, medicinske podatke ili podatke o maloljetnicima. Prije javnog objavljivanja dokumente treba anonimizovati.

## Planirana unapređenja

- export nalaza u JSON,
- export nalaza u CSV,
- batch obrada više PDF fajlova,
- izračun SHA-256 hash vrijednosti dokumenta,
- osnovni izvještaj za prilaganje uz FOI, žalbu ili javnu studiju slučaja,
- lokalni alat za anonimizaciju osjetljivih podataka.
