# Test dokazne podloge

## Cilj

Utvrditi koje tvrdnje zahtijevaju dokaz, koji dokaz je ponuđen i da li zaista potvrđuje javnu tvrdnju.

## Prompt

```text
Analiziraj da li su za sljedeću javnu izjavu ponuđeni dokazi.

IZJAVA:
[unesi izjavu]

PRATEĆI TEKST ILI DOKUMENTI:
[unesi dostupne podatke, linkove ili napiši „nisu ponuđeni“]

Utvrdi:

1. koje tvrdnje zahtijevaju dokaz,
2. koji dokaz je zaista ponuđen,
3. da li dokaz direktno potvrđuje tvrdnju,
4. da li se navodi izvor, datum, metodologija i autor podatka,
5. da li je naveden samo autoritet bez dokumenta,
6. koji dokumenti bi bili potrebni za nezavisnu provjeru,
7. da li postoji razlika između tvrdnje i onoga što dokaz stvarno pokazuje.

Razlikuj:
- dokaz,
- indiciju,
- mišljenje,
- političku tvrdnju,
- pozivanje na autoritet.

Ne zaključuj da je tvrdnja netačna samo zato što dokaz nije ponuđen. Napiši da je tvrdnja nedovoljno potkrijepljena kada je to odgovarajući zaključak.

Na kraju ocijeni snagu dokazne podloge od 0 do 5:
0 — nema nikakvog dokaza;
1 — samo pozivanje na autoritet ili neimenovane izvore;
2 — djelimični ili indirektni podaci;
3 — relevantan dokaz postoji, ali nije potpun ili potpuno provjerljiv;
4 — dokazi su konkretni i uglavnom dovoljni;
5 — dokazi su javni, potpuni, direktni i nezavisno provjerljivi.

Obrazloži ocjenu.
```