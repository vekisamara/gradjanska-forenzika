# Test prećutanog konteksta

## Cilj

Utvrditi koje informacije nedostaju i da li njihov izostanak može promijeniti način na koji javnost razumije izjavu.

## Prompt

```text
Analiziraj sljedeću izjavu sa stanovišta informacija koje su možda izostavljene:

[unesi izjavu]

Utvrdi:

1. koje informacije bi mogle promijeniti način na koji građanin razumije izjavu,
2. da li je izostavljen raniji period,
3. da li su izostavljeni troškovi, dugovanja ili obaveze,
4. da li se navodi korist bez navođenja rizika,
5. da li se navodi završena procedura, ali ne i stvarni rezultat,
6. da li se govori o ukupnoj vrijednosti bez izvora finansiranja,
7. da li je izostavljeno ko je donio odluku,
8. da li su izostavljene prethodne suprotne izjave,
9. da li se predstavlja jedan uspješan primjer bez prikaza ukupnog stanja,
10. koja dodatna pitanja novinar ili građanin treba da postavi.

Ne tvrdi da je nešto namjerno skriveno ako za to nema dokaza. Razlikuj:
- nedostajući kontekst,
- mogući previd,
- selektivno predstavljanje,
- dokazano prikrivanje.

Na kraju ocijeni potpunost konteksta od 0 do 5:
0 — ključni kontekst potpuno nedostaje;
1 — izjava stvara sliku gotovo isključivo kroz izostavljanje;
2 — nedostaje više važnih činjenica;
3 — osnovni kontekst postoji, ali nije potpun;
4 — kontekst je uglavnom dovoljan;
5 — izjava pruža cjelovit, uravnotežen i provjerljiv kontekst.

Obrazloži ocjenu.
```