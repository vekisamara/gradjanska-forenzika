# Alati za građansku forenziku

Folder `alati/` sadrži lokalne softverske alate za tehničku provjeru dokumenata, evidenciju dokaza, praćenje rokova i pripremu podataka za budući Civic Intelligence Dashboard. Osnovno pravilo je da se osjetljivi dokumenti prvo obrađuju lokalno, prije bilo kakvog slanja prema vanjskim servisima ili AI modelima.

Alati su tehnički sloj [`Democratic Resilience & AI Literacy Programa`](../program/README.md). Oni proizvode pomoćne tragove i strukturisane podatke; ne utvrđuju nezakonitost, namjeru ili odgovornost bez dodatnih dokaza i ljudske provjere. Povučeni prototipovi nalaze se u [`arhiva/`](../arhiva/README.md).

## Instalacija

```bash
python -m venv .venv
source .venv/bin/activate
pip install pypdf
```

Na Windows sistemu:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pypdf
```

`pypdf` je potreban za PDF alate. Ostali alati koriste standardnu Python biblioteku.

## Dostupni alati

### `forenzika_pdf.py`

Interaktivna analiza jednog PDF dokumenta. Izvlači autora, aplikaciju, producer softver, datum kreiranja, datum izmjene, broj stranica i dodatne skrivene tagove.

```bash
python forenzika_pdf.py
```

### `pdf_batch_metadata.py`

Batch analiza svih PDF dokumenata u folderu. Pravi CSV i opcioni JSON izvještaj.

```bash
python pdf_batch_metadata.py dokazi/ --recursive --csv pdf_metadata_report.csv --json pdf_metadata_report.json
```

### `hash_dokaza.py`

Izračun SHA-256 hash vrijednosti za jedan ili više fajlova/foldera.

```bash
python hash_dokaza.py dokazi/ --recursive --csv hash_report.csv --json hash_report.json
```

### `metadata_risk_score.py`

Dodaje indikator za dodatnu provjeru na osnovu CSV izvještaja iz `pdf_batch_metadata.py`. Ovaj alat ne utvrđuje nezakonitost; samo označava metapodatkovne signale koje treba ručno provjeriti.

```bash
python metadata_risk_score.py pdf_metadata_report.csv --output metadata_risk_report.csv
```

### `anonimizator_teksta.py`

Osnovna lokalna anonimizacija TXT/MD fajlova. Prepoznaje neke česte obrasce: JMBG, email, telefon i brojeve ličnih dokumenata. Rezultat uvijek treba ručno pregledati.

```bash
python anonimizator_teksta.py dokument.txt --output dokument_anonimizovan.txt
```

### `rokovi_kalkulator.py`

Kalkulator rokova od datuma podnošenja.

```bash
python rokovi_kalkulator.py --datum 2026-05-13 --rok 30
```

### `foi_tracker.py`

Lokalni CSV tracker FOI zahtjeva i statusa.

```bash
python foi_tracker.py add --datum 2026-05-13 --rok 30 --organ "Grad Banja Luka" --predmet "Šaht"
python foi_tracker.py status
python foi_tracker.py update --id ABC123 --status odgovoreno
```

### `evidencioni_dnevnik.py`

CSV dnevnik dokaza u predmetu. Može automatski izračunati hash fajla.

```bash
python evidencioni_dnevnik.py add --case-id PRIMJER-2026 --file dokument.pdf --institution "Primjer institucije" --document-number "UP-01-123/26" --document-date 2026-05-09 --source "FOI odgovor"
python evidencioni_dnevnik.py list --case-id PRIMJER-2026
```

### `timeline_builder.py`

Generiše Markdown hronologiju iz CSV evidencije.

```bash
python timeline_builder.py evidencija_dokaza.csv --output hronologija.md
```

### `case_json_builder.py`

Pravi osnovni `case.json` za dashboard-ready predmet.

```bash
python case_json_builder.py --case-id sime-solaje-1b-2026 --title "Sime Šolaje 1b" --institution "Komunalna policija" --issue-type cutanje_uprave --public-interest "zaštita stanara" --risk-level high --output case.json
```

### `markdown_case_report.py`

Generiše Markdown studiju slučaja iz `case.json` i opcione CSV evidencije.

```bash
python markdown_case_report.py case.json --evidence-csv evidencija_dokaza.csv --output case_report.md
```

## Preporučeni workflow

1. Dokumente staviti u lokalni folder `dokazi/`.
2. Pokrenuti `hash_dokaza.py` radi dokaznog integriteta.
3. Pokrenuti `pdf_batch_metadata.py` radi digitalnog traga PDF dokumenata.
4. Pokrenuti `metadata_risk_score.py` radi indikatora za dodatnu provjeru.
5. Voditi predmet kroz `evidencioni_dnevnik.py` i `foi_tracker.py`.
6. Generisati hronologiju pomoću `timeline_builder.py`.
7. Kreirati `case.json` pomoću `case_json_builder.py`.
8. Napraviti javni Markdown nacrt pomoću `markdown_case_report.py`.

## Pravila tumačenja

Metapodaci, hash vrijednosti i lokalni izvještaji nisu sami po sebi dokaz nezakonitosti. Oni su dokazni tragovi i indikatori za dodatnu provjeru. Nalaze treba kombinovati sa sadržajem akta, brojem protokola, potpisom, pečatom, pravnim osnovom, rokovima i službenom prepiskom.

## Privatnost

Ne objavljujte neobrađene dokumente koji sadrže JMBG, broj lične karte, privatnu adresu, privatni telefon, medicinske podatke ili podatke o maloljetnicima. Prije javnog objavljivanja dokumente treba anonimizovati i ručno pregledati.
