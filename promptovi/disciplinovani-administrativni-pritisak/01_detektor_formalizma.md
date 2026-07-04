# 01 — Detektor formalizma

## Kada koristiti

Koristite ovaj prompt odmah nakon što dobijete odgovor lokalne uprave, inspekcije, komunalne policije, gradonačelnika, odjeljenja ili komisije, a odgovor vam djeluje opšte, nejasno ili izbjegavajuće.

Cilj je utvrditi da li je organ stvarno odgovorio ili je samo formalno zatvorio predmet.

## Šta pripremiti

- svoj prvobitni zahtjev, prijavu ili žalbu;
- odgovor organa;
- ako postoji, broj predmeta i datum akta.

## Prompt

```text
Analiziraj sljedeći odgovor lokalne uprave kao alat građanske forenzike.

Moj zahtjev/prijava/žalba:
[OVDJE ZALIJEPI SVOJ PODNESAK ILI KRATAK SAŽETAK]

Odgovor organa:
[OVDJE ZALIJEPI ODGOVOR ORGANA]

Zadatak:
1. utvrdi da li je odgovor stvaran ili formalistički;
2. izdvoji konkretne tvrdnje organa;
3. provjeri da li organ navodi činjenice, datume, dokaze, zapisnike, službene zabilješke i pravni osnov;
4. označi dijelove gdje organ koristi opšte fraze umjesto provjerljivih informacija;
5. utvrdi koja moja pitanja nisu odgovorena;
6. predloži sljedeći zakonit korak.

Odgovor organizuj u tabeli:
- navod organa;
- problem;
- zašto je formalistički ili nepotpun;
- koji dokaz nedostaje;
- sljedeći korak.

Na kraju napiši kratak zaključak običnim jezikom.
```

## Kako tumačiti rezultat

Ako AI označi da odgovor ne sadrži datume, dokaze, zapisnike ili pravni osnov, to ne znači automatski da je organ nezakonito postupao. To znači da postoji osnov za novi, precizniji zahtjev.

## Sljedeći prompt

Ako odgovor sadrži tvrdnje bez dokaza, koristite `02_dokaz_iza_fraze.md`.
