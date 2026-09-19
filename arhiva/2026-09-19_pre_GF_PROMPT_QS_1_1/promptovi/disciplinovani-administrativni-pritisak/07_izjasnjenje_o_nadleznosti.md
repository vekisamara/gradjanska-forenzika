# 07 — Izjašnjenje o nadležnosti

## Kada koristiti

Koristite ovaj prompt kada organ izbjegava postupanje tvrdnjom da nije nadležan, ali ne navodi jasno koji organ jeste nadležan ili ne dostavlja dokaz da je predmet proslijeđen.

Cilj je spriječiti administrativni ping-pong.

## Prompt

```text
Napiši kratak zahtjev organu da se jasno izjasni o nadležnosti.

Kontekst:
- organ kojem se obraćam: [NAZIV ORGANA]
- predmet: [KRATAK OPIS PREDMETA]
- prethodni odgovor organa: [ZALIJEPI RELEVANTNI DIO ODGOVORA]

Zadatak:
1. traži da organ jasno navede da li je nadležan;
2. ako organ nije nadležan, traži da navede koji organ jeste nadležan;
3. traži pravni osnov za stav o nenadležnosti;
4. traži informaciju da li je predmet proslijeđen nadležnom organu;
5. traži datum, broj akta i naziv organa kojem je predmet proslijeđen;
6. traži kopiju akta o prosljeđivanju, ako postoji;
7. ton neka bude služben i kratak.
```

## Korisna formulacija

"Ukoliko organ smatra da nije nadležan za postupanje, molim da precizno navedete koji organ jeste nadležan, pravni osnov za takav stav i da li je predmet proslijeđen nadležnom organu po službenoj dužnosti."

## Sljedeći korak

Ako organ ne odgovori jasno, koristite `03_matrica_neodgovorenih_pitanja.md` ili `08_rokovnik_i_urgencija.md`.
