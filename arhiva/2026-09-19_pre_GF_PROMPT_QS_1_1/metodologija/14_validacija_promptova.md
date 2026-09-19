# Validacija GFO promptova

**Oznaka:** GF-PROMPT-EVAL 1.0  
**Status:** važeći operativni protokol  
**Datum:** 22. avgust 2026.

## 1. Svrha

Ovaj protokol određuje kako se nova ili značajno izmijenjena verzija prompta testira prije nego što dobije status stabilnog dijela Prompt Library.

Validacija ne dokazuje da je prompt nepogrešiv. Ona provjerava da li prompt dovoljno pouzdano proizvodi traženi tip analize na poznatim slučajevima i da li greške postaju vidljive prije javne ili procesne upotrebe.

## 2. Minimalni evaluacioni set

Za složeni prompt koristi se najmanje 5 testova; preporučeno 8–10. Set treba, gdje je moguće, sadržati:

- najmanje 2 jasna pozitivna slučaja;
- najmanje 2 negativna ili kontradiktorna slučaja;
- najmanje 1 slučaj sa nedostajućim ključnim dokazom;
- najmanje 1 slučaj sa potencijalno zavodljivim jezikom, brojkom ili formalističkim obrazloženjem;
- najmanje 1 granični slučaj kod kojeg je ispravan rezultat ograničen ili uslovan zaključak.

Jedan stvarni predmet može dati više testova samo ako su pitanja dovoljno nezavisna.

## 3. Ground truth / očekivani rezultat

Za svaki test prije pokretanja prompta evidentira se:

- centralno pitanje;
- minimalni skup činjenica koje bi prompt morao prepoznati;
- ključna činjenica ili zaključak koji ne smije izmisliti;
- očekivani status ključnih tvrdnji;
- prihvatljivi raspon zaključka;
- poznati protivdokaz ili alternativno objašnjenje, ako postoji.

Očekivani rezultat ne mora biti jedna unaprijed napisana formulacija. Dovoljno je unaprijed definisati granice ispravnog nalaza.

## 4. Kriterijumi ocjenjivanja

Svaki test ocjenjuje se po šest dimenzija:

| Dimenzija | Pitanje |
|---|---|
| Tačnost | Da li su činjenice i citati ispravno korišteni bez izmišljanja? |
| Potpunost | Da li su prepoznate ključne činjenice, kontradikcije i praznine? |
| Dokazna disciplina | Da li su činjenica, izvorna tvrdnja, tumačenje i pretpostavka razdvojeni? |
| Kalibracija | Da li je sigurnost zaključka proporcionalna dokazima? |
| Format | Da li rezultat prati propisanu strukturu i odgovara centralnom pitanju? |
| Akcionabilnost | Da li su naredni dokazni koraci konkretni i provjerljivi? |

Ocjena za svaku dimenziju: `2 = prolaz`, `1 = djelimično`, `0 = pad`.

## 5. Kritične greške

Bez obzira na zbir bodova, test automatski pada ako prompt:

- izmisli dokument, citat, broj akta, datum, iznos, događaj ili pravnu normu;
- predstavi nedokazanu tvrdnju kao potvrđenu činjenicu;
- zanemari poznati protivdokaz koji mijenja centralni zaključak;
- iz odsustva dokumenta zaključi da dokument ili radnja ne postoje;
- pripiše unutrašnju namjeru bez dokaza;
- proizvede pravni ili činjenični zaključak suprotan jasnom sadržaju testnog materijala.

## 6. Pragovi

Prompt može dobiti status **STABILAN** samo ako:

- nema kritičnih grešaka;
- najmanje 80% testova nema nijednu ocjenu `0` u tačnosti ili dokaznoj disciplini;
- prosječna ocjena po svim dimenzijama iznosi najmanje 1,6/2;
- nijedan ponavljajući tip greške nije ostao bez korekcije ili dokumentovanog ograničenja.

U suprotnom status je **U VALIDACIJI**.

## 7. Regresiono testiranje

Kada se mijenja stabilan prompt, isti benchmark se ponavlja. Nova verzija ne smije pogoršati ranije uspješne testove bez jasno obrazloženog razloga.

Ako je izmjena napravljena da popravi konkretnu grešku, taj slučaj ostaje trajni regresioni test.

## 8. Inter-analyst provjera

Za promptove koji utiču na objavu, žalbu, pravnu strategiju ili javnu optužbu preporučuje se da najmanje dva analitičara nezavisno pregledaju najmanje dio evaluacionog seta i uporede:

- status ključnih tvrdnji;
- širinu zaključka;
- nivo pouzdanosti;
- koje dodatne dokaze smatraju odlučnim.

Velika odstupanja nisu samo problem analitičara; mogu ukazivati da je prompt nedovoljno precizan.

## 9. Evidencija testa

Za svaku verziju čuva se najmanje:

- oznaka i verzija prompta;
- datum testa;
- model/alati kada su poznati;
- ID testnog slučaja;
- očekivani rezultat;
- rezultat prompta;
- ocjene 0/1/2;
- kritične greške;
- ljudske korekcije;
- odluka: STABILAN / U VALIDACIJI / POVUĆEN.

Osjetljivi testni podaci se ne objavljuju. Javni benchmark može koristiti anonimizovane ili sintetičke slučajeve.

## 10. Predloženi početni GFO benchmark

Prvi benchmark treba graditi iz već obrađenih tipova predmeta, ali samo iz materijala prikladnog za tu namjenu:

1. upravno rješenje sa jasnom dokaznom prazninom;
2. upravno rješenje sa jakim protivdokazom;
3. institucionalni odgovor koji formalno odgovara, ali ne daje traženi zapis;
4. PR saopštenje sa brojčanom tvrdnjom bez dovoljnog obuhvata;
5. izvještaj o radu koji miješa aktivnosti i ishode;
6. FOI slučaj sa nedostajućim dokumentom, gdje se ne smije zaključiti da dokument ne postoji;
7. hronologija sa paralelnim postupcima i vremenskom nekonzistentnošću;
8. predmet sa potpunim lancem pitanje → činjenica → dokaz → pravilo → obrazloženje → zaključak.
