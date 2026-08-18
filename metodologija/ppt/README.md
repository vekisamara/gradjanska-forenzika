# PR-to-Payment Trace (PPT) — metod v0.1

**Oznaka:** GF-PPT 0.1  
**Status:** nezavisan modul — kandidat u validaciji  
**Datum:** 18. avgust 2026.  
**Urednik:** Velimir Šamara

PR-to-Payment Trace je metod za rekonstrukciju javnog novca od infrastrukturne PR objave do nabavke, ugovora, izvođača, situacije ili fakture i evidentiranog plaćanja.

> PR objava → projekat → nabavka → ugovor/nalog → izvođač → situacija/faktura → plaćanje

PPT može raditi samostalno, ali primjenjuje dokazna pravila Građanske forenzike. Ne utvrđuje automatski nezakonitost, korupciju niti namjeru. Mjeri sljedivost, dokumentovanost i međusobnu saglasnost javno dostupnih tragova.

## Četiri proizvoda

1. **PPT Method v0.1** — ovaj dokument: predmet, pravila, faze, statusi i kriterijumi.
2. [**PPT Prompt Library v0.1**](01_prompt_library_v0.1.md) — šesnaest kontrolisanih AI promptova.
3. [**PPT Project Card**](02_project_card.md) — obrazac za pojedinačni projekat.
4. [**Validation Case: Čokorska Polja–Goleši**](03_validation_case_cokorska_polja_golesi.md) — radni validacioni kandidat.

## Centralno pitanje

Može li se javna tvrdnja da se određeni projekat realizuje povezati sa konkretnom nabavkom, ugovorom ili nalogom, izvođačem i stvarnim plaćanjem?

## Obavezna načela

1. Isti izvođač nije dokaz da je riječ o istom projektu.
2. Sličan naziv radova nije dovoljan za potvrđenu vezu.
3. Okvirni sporazum ne dokazuje da je konkretna lokacija obuhvaćena.
4. Procijenjena, ugovorena i plaćena vrijednost su različite kategorije.
5. Zbirno ulaganje u područje nije cijena konkretnog projekta.
6. Medijska ili PR objava je trag o javnoj tvrdnji, ne finansijski dokaz.
7. Odsustvo pronađenog dokumenta ne dokazuje da dokument ne postoji.
8. AI mora razdvojiti činjenicu, navod izvora, inferenciju, pretpostavku i nepoznato.
9. Materijalni nalaz mora imati izvor, lokator i nivo pouzdanosti.
10. Kada spis ne daje odgovor, koristi se formulacija **„nije utvrđeno“**.

Modul koristi oznake izvora O/K/R/N i nivoe D1–D5 iz GF-MET-a. Rezultat AI-a je radni materijal koji se provjerava prema originalnom izvoru.

## Ulazni slojevi

| Sloj | Minimalni podaci |
|---|---|
| PR/javna komunikacija | datum, organ, naslov, lokacija, opis, javna vrijednost, izvođač, rok |
| Nabavka | broj postupka, predmet, vrsta postupka, procjena, kriterij, odluka, ponuđač |
| Ugovor/nalog | broj i datum, lokacija, predmet, vrijednost, rok, podizvođači |
| Izvršenje | predmjer, radni nalog, nadzor, privremena/okončana situacija |
| Plaćanje | dobavljač, faktura/situacija, datum, opis, iznos, veza sa ugovorom |

## Radni tok

### PPT-1 — PR Extractor

Izdvaja projekat, lokaciju, količinu, vrijednost, rok, izvođača i fazu. Finansijsku tvrdnju klasifikuje kao: konkretni projekat, faza, zbirno teritorijalno ulaganje, planirana vrijednost, procjena, ugovorena vrijednost ili neodređeno.

### PPT-2 — Procurement Resolver

Traži kandidate prema nazivu i sinonimima, lokaciji, vrsti radova, periodu, CPV oznaci, izvođaču i vrijednosti. Ne bira kandidat bez obrazloženja.

### PPT-3 — Contract Linker

Provjerava da li postupak, ugovor, pojedinačni ugovor iz okvirnog sporazuma, radni nalog, predmjer ili gradilišna tabla neposredno obuhvataju lokaciju i radove.

### PPT-4 — Payment Matcher

Povezuje dobavljača i ugovor sa fakturama, situacijama i plaćanjima. Ugovorena vrijednost se nikada ne prikazuje kao izvršeno plaćanje bez posebnog dokaza.

### PPT-5 — Consistency Checker

Provjerava vrijednost, lokaciju, vrijeme, izvođača, predmet, količinu, rok i plaćanje. Vremenski test može koristiti PPTC pravila, ali PPT i Parallel Proceedings / Temporal Consistency Check ostaju odvojeni moduli.

### PPT-6 — Trace Score

Dodjeljuje status veze i indeks javne sljedivosti. Bodovi mjere dostupnost i povezivost tragova, ne integritet aktera.

### PPT-7 — Missing Document Generator

Iz dokazne praznine izrađuje listu nedostajućih zapisa, plan provjere i precizan zahtjev za pristup informacijama.

## Status veze

| Status | Značenje |
|---|---|
| 🟢 **Verified Match** | ugovor i plaćanje potvrđeni neposrednim identifikatorom ili ekvivalentnim skupom primarnih dokaza |
| 🟡 **Probable Match** | jaka podudarnost lokacije, vremena, predmeta i aktera, ali nedostaje direktna veza |
| 🟠 **Partial Trace** | pronađen dio lanca, ali ne i pojedinačni ugovor/nalog ili plaćanje |
| 🔴 **Untraceable** | raspoloženi javni podaci ne omogućavaju pouzdano povezivanje |
| ⚫ **Contradictory Trace** | relevantni izvori sadrže materijalno nesaglasne podatke |

Status se ne određuje samo procentom pouzdanosti. Jedan nedostajući ključni dokument može onemogućiti Verified Match.

## Indeks javne sljedivosti: 0–100

| Element | Bodovi |
|---|---:|
| identifikovan projekat | 10 |
| identifikovana nabavka | 15 |
| dostupan ugovor ili pojedinačni nalog | 15 |
| potvrđena lokacija | 10 |
| potvrđen izvođač | 10 |
| potvrđena vrijednost konkretnog projekta | 10 |
| pronađena situacija/faktura | 10 |
| pronađeno plaćanje | 15 |
| međusobna saglasnost podataka | 5 |

Ocjena 25/100 znači slabu javnu sljedivost, ne korupciju.

## Minimalni dokaz za Verified Match

Potreban je najmanje jedan direktni zajednički identifikator kroz ugovor i plaćanje, ili kombinacija primarnih dokaza koja jednoznačno potvrđuje: istu lokaciju, isti predmet, istog ugovornog dobavljača, odgovarajući vremenski slijed i vezu situacije/fakture sa ugovorom.

## Kontrola kvaliteta

Prije objave drugi analitički prolaz mora:

- pokušati pronaći najmanje jedno alternativno podudaranje;
- provjeriti da li je zbirna PR vrijednost pogrešno pripisana projektu;
- provjeriti okvirne sporazume i pojedinačne naloge;
- ponoviti zbir plaćanja;
- označiti izvor i lokator svakog materijalnog podatka;
- ublažiti status ako ključni zaključak zavisi od R/N izvora;
- zabilježiti datum pretrage i granice registra.

## Izlaz

Svaki PPT nalaz sadrži Project Card, dokaznu matricu, status veze, indeks, kontradikcije, otvorene praznine, plan pribavljanja dokumentacije, datum pregleda i napomenu da rezultat nije automatska pravna kvalifikacija.
