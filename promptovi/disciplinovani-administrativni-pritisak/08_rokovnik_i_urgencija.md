# 08 — Rokovnik i urgencija

## Kada koristiti

Koristite ovaj prompt kada želite provjeriti da li je istekao rok za odgovor ili kada treba pripremiti urgenciju zbog ćutanja uprave, kašnjenja ili nepostupanja.

Rokovnik je dokazni alat. On pokazuje kada je građanin postupio, kada je organ trebalo da odgovori i šta se desilo nakon isteka roka.

## Prompt

```text
Na osnovu sljedećih podataka napravi rokovnik predmeta i pripremi prijedlog urgencije ako je rok istekao.

Podaci:
- organ: [NAZIV ORGANA]
- datum slanja podneska: [DATUM]
- vrsta podneska: [PRIJAVA / FOI / ZAHTJEV / ŽALBA / URGENCIJA]
- broj protokola, ako postoji: [BROJ]
- zakonski ili očekivani rok: [ROK]
- da li je odgovor stigao: [DA / NE]
- ako jeste, datum odgovora: [DATUM]
- kratak opis predmeta: [OPIS]

Zadatak:
1. napravi tabelu rokovnika;
2. izračunaj datum isteka roka ako je moguće;
3. označi status predmeta;
4. ako rok nije istekao, predloži kada provjeriti ponovo;
5. ako je rok istekao, napiši kratku urgenciju;
6. urgencija neka se poziva na datum slanja, predmet, rok i izostanak odgovora;
7. ton neka bude služben i činjeničan.
```

## Minimalni rokovnik

- datum slanja;
- organ;
- predmet;
- broj predmeta;
- rok;
- datum isteka;
- status;
- sljedeći korak.

## Napomena

Ako niste sigurni koji rok važi, AI može pomoći u organizovanju podataka, ali pravni rok provjerite u važećem propisu ili kod stručne osobe.
