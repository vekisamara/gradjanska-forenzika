# Šablon GFO prompta

**Oznaka:** GF-PROMPT-TEMPLATE 1.0  
**Primjenjuje:** `00_forenzicko_jezgro.md` i `../metodologija/13_standard_kvaliteta_promptova.md`

Ovaj dokument je obrazac za nove i revidirane promptove. Ne koristi se kao samostalan analitički prompt bez popunjavanja specifičnog zadatka.

```text
# CONTEXT
Predmet:
Jurisdikcija:
Datum analize:
Vrsta dokumenta / izvora:
Poznate činjenice:
Otvorene praznine:

# TASK
Centralno pitanje:
Primarni rezultat koji treba proizvesti:

Izvrši samo analitičke radnje potrebne za taj rezultat.

# EVIDENCE RULES
- Primijeni GF-PROMPT-CORE.
- Ne dopunjavaj nedostajuće činjenice nagađanjem.
- Za svaku ključnu tvrdnju navedi dokaz i locator kada je dostupan.
- Ako pravni izvor, datum, broj ili činjenica nisu provjereni, označi ih kao potrebne za provjeru.
- Razdvoji ČINJENICU, TVRDNJU IZVORA, TUMAČENJE, PRETPOSTAVKU i NEPOZNATO.

# ANALYTICAL TESTS
1. [test specifičan za zadatak]
2. [test specifičan za zadatak]
3. [test specifičan za zadatak]

# OUTPUT SCHEMA
1. Predmet i centralno pitanje
2. Ključni nalaz
3. Dokazna matrica
4. Rezultati specifičnih testova
5. Kontradikcije i alternativna objašnjenja
6. Nedostajući dokazi
7. Nivo pouzdanosti
8. Sljedeći dokazni/procesni koraci
9. Tvrdnje koje zahtijevaju ljudsku provjeru

# UNCERTAINTY
Za svaki ključni zaključak označi pouzdanost kao VISOKA / SREDNJA / NISKA i ukratko navedi zašto.
Ako odlučna činjenica nedostaje, koristi uslovni zaključak i navedi šta ga može potvrditi ili opovrgnuti.

# ACCEPTANCE CRITERIA / SELF-CHECK
Prije završetka provjeri:
- da li si odgovorio na centralno pitanje;
- da li svaka ključna tvrdnja ima dokaz ili jasnu oznaku nepotvrđenosti;
- da li su činjenice i tumačenja odvojeni;
- da li postoji zanemaren protivdokaz ili razumno alternativno objašnjenje;
- da li je neki datum, broj, citat, pravilo ili događaj neprovjereno pretpostavljen;
- da li je zaključak proporcionalan dokazima;
- šta bi moglo promijeniti zaključak;
- da li drugi analitičar može rekonstruisati nalaz.

# INPUT
[unesi materijal]
```
