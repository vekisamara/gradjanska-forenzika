# 02 — Dokaz iza fraze

## Kada koristiti

Koristite ovaj prompt kada organ napiše opštu tvrdnju kao što su:

- postupali smo u skladu sa zakonom;
- izvršena je kontrola;
- nije utvrđena nepravilnost;
- predmet je proslijeđen nadležnom organu;
- nema osnova za dalje postupanje;
- komisija nije nadležna da cijeni istinitost dokumentacije.

Cilj je svaku frazu pretvoriti u provjerljivo pitanje i zahtjev za dokument.

## Prompt

```text
Analiziraj sljedeći odgovor organa i primijeni pravilo građanske forenzike: "Ne raspravljaj se sa frazom. Traži dokaz iza fraze."

Odgovor organa:
[OVDJE ZALIJEPI ODGOVOR]

Zadatak:
1. izdvoji sve opšte tvrdnje organa;
2. za svaku tvrdnju napiši koji dokaz bi morao postojati ako je tvrdnja tačna;
3. predloži precizna pitanja koja treba postaviti organu;
4. predloži konkretne dokumente koje treba tražiti;
5. pripremi kratak nacrt dopisa kojim se od organa traži da dostavi dokaze iza svojih tvrdnji.

Koristi tabelu:
- tvrdnja organa;
- dokaz koji bi morao postojati;
- pitanje za organ;
- dokument koji treba tražiti;
- zašto je to važno.

Ton dopisa neka bude smiren, služben i bez optužbi.
```

## Korisni dokumenti koje često treba tražiti

- službena zabilješka;
- zapisnik;
- fotografije sa terena;
- mjerenja;
- evidencija prijava;
- akt o prosljeđivanju predmeta;
- akt o zaključivanju predmeta;
- interni dopis između odjeljenja;
- pravni osnov za zaključak organa.

## Sljedeći prompt

Ako imate više pitanja na koja organ nije odgovorio, koristite `03_matrica_neodgovorenih_pitanja.md`.
