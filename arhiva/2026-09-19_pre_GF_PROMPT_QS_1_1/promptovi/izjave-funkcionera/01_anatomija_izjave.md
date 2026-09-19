# Anatomija izjave

## Cilj

Razdvojiti činjenične tvrdnje, političke stavove, obećanja, procjene i neprovjerljive formulacije.

## Prompt

```text
Analiziraj sljedeću izjavu javnog funkcionera.

IZJAVA:
[unesi izjavu]

Razdvoji sadržaj izjave na:

1. konkretne činjenične tvrdnje,
2. vrijednosne i političke stavove,
3. obećanja ili najave,
4. procjene i predviđanja,
5. tvrdnje koje se ne mogu provjeriti,
6. nejasne ili dvosmislene formulacije.

Za svaku činjeničnu tvrdnju napiši:
- šta se tačno tvrdi,
- da li je tvrdnja precizna,
- koji podatak nedostaje,
- kako bi se tvrdnja mogla provjeriti.

Nemoj ocjenjivati političku popularnost izjave. Analiziraj samo sadržaj i provjerljivost.

Na kraju ocijeni preciznost tvrdnje od 0 do 5:
0 — nema provjerljive tvrdnje;
1 — gotovo potpuno neodređena;
2 — djelimično određena, ali bez ključnih podataka;
3 — uglavnom jasna, uz nekoliko nejasnoća;
4 — jasna i skoro potpuno provjerljiva;
5 — precizna, vremenski određena i mjerljiva.

Obrazloži ocjenu u najviše tri rečenice.
```