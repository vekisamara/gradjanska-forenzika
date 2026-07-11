# Forenzika brojeva

## Cilj

Provjeriti izvore, periode, osnovice i kontekst svih brojčanih i statističkih tvrdnji.

## Prompt

```text
Analiziraj sve brojeve, procente, iznose i statističke tvrdnje u sljedećoj izjavi:

[unesi izjavu]

Za svaki broj utvrdi:

1. izvor podatka,
2. period na koji se odnosi,
3. početnu i krajnju vrijednost,
4. apsolutnu i procentualnu promjenu,
5. da li je podatak prilagođen inflaciji kada je to relevantno,
6. da li je poređenje izvršeno sa odgovarajućim periodom,
7. da li se koristi ukupan iznos ili iznos po stanovniku,
8. da li se prikazuje plan, obezbijeđena sredstva, ugovorena vrijednost, isplata ili stvarna realizacija,
9. da li prosjek prikriva velike razlike,
10. koji kontekst nedostaje.

Ne pretpostavljaj da je broj tačan samo zato što je precizno naveden.

Posebno označi razliku između:
- planirano,
- obezbijeđeno,
- ugovoreno,
- isplaćeno,
- realizovano,
- završeno.

Na kraju ocijeni transparentnost upotrebe podataka od 0 do 5:
0 — brojke su bez izvora i konteksta;
1 — gotovo potpuno neprovjerljive;
2 — djelimični izvori ili neodgovarajuća poređenja;
3 — uglavnom razumljive, ali sa važnim nedostacima;
4 — jasno predstavljene i uglavnom provjerljive;
5 — potpuni izvori, metodologija, period i odgovarajući kontekst.

Obrazloži ocjenu.
```