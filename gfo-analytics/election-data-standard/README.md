# GFO Election Data Standard

**Current working version:** v0.1 Draft

Ovaj modul definiše kanonski format izbornih podataka za GFO Analytics. Ne sadrži pravila za zaključivanje o regularnosti izbora, političkoj namjeri ili anomalijama.

## Struktura

- `drafts/` — sve radne verzije standarda;
- `spec/` — data dictionary i buduće tehničke specifikacije;
- `schemas/` — JSON Schema definicije;
- `validation/` — pravila validacije i testovi na stvarnim izbornim podacima;
- `examples/` — primjeri normalizovanih ulaznih podataka.

## Granica odgovornosti

Data Standard definiše: identifikatore, strukturu, tipove, provenance, revizije i validaciju.

Election Analytics moduli će naknadno definisati: baseline, statističke pokazatelje, detekciju anomalija, LLM input pakete, promptove i korisničke interfejse.
