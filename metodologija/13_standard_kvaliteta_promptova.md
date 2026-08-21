# Standard kvaliteta GFO promptova

**Oznaka:** GF-PROMPT-QS 1.0  
**Status:** važeći operativni standard  
**Datum:** 22. avgust 2026.

## 1. Svrha

Ovaj standard definiše minimalnu strukturu, dokazna pravila i kriterijume prihvatanja za svaki prompt Građanske forenzike. Primjenjuje se zajedno sa `promptovi/00_forenzicko_jezgro.md`.

Cilj nije da prompt bude što duži, nego da zadatak bude dovoljno jasno ograničen da drugi analitičar može razumjeti šta je ulaz, šta je izlaz i po kojim kriterijumima se rezultat smatra prihvatljivim.

## 2. Jedan prompt — jedan primarni rezultat

Svaki prompt mora imati jedan jasno definisan primarni rezultat. Ako zadatak zahtijeva više različitih proizvoda ili različite faze zaključivanja, dijeli se na više promptova ili modula.

Dozvoljeni su pomoćni izlazi samo kada direktno služe primarnom rezultatu.

## 3. Obavezna struktura

Svaki novi ili revidirani prompt mora eksplicitno ili putem nasljeđivanja sadržati sljedećih sedam blokova:

1. **Context** — predmet, jurisdikcija, datum, vrsta izvora i ono što je već poznato.
2. **Task** — jedna precizna analitička radnja i centralno pitanje.
3. **Evidence rules** — koje izvore i tvrdnje AI smije koristiti i kako označava nedostajuće informacije.
4. **Analytical tests** — konkretni testovi koji se moraju izvršiti.
5. **Output schema** — unaprijed definisana struktura rezultata.
6. **Uncertainty** — šta nije potvrđeno, koje pretpostavke postoje i šta zahtijeva provjeru.
7. **Self-check / Acceptance criteria** — provjera da li izlaz zadovoljava minimalne kriterijume kvaliteta.

Specijalizovani prompt ne mora ponavljati puni tekst zajedničkog jezgra, ali mora jasno navesti da ga nasljeđuje.

## 4. Minimalni acceptance criteria

Rezultat se ne smatra završenim dok nije provjereno:

- svaka ključna tvrdnja ima dokaz ili je označena kao nepotvrđena;
- činjenice, tvrdnje izvora, tumačenja, pretpostavke i nepoznato nisu pomiješani;
- nijedan datum, broj akta, iznos, citat ili pravna norma nisu izmišljeni;
- ključni zaključak nije širi od dokaza koji ga nose;
- važni protivdokazi i razumna alternativna objašnjenja nisu prećutani;
- nedostajući dokument nije tretiran kao dokaz nepostojanja;
- svaki važan otvoreni nalaz ima predložen način provjere;
- izlaz odgovara traženom formatu i centralnom pitanju;
- jasno je označeno šta zahtijeva ljudsku provjeru.

## 5. Pravilo izvora

Za činjenične i pravno osjetljive zadatke prompt mora tražiti oslonac na dostavljeni ili provjereni izvor. Kada je moguće, nalaz se veže za citat, stranicu, pasus, tabelu, broj akta, URL ili drugi stabilni locator.

AI ne smije popunjavati praznine opštim znanjem kada bi ta praznina mogla promijeniti pravni ili činjenični zaključak.

## 6. Pravilo neizvjesnosti

Za svaki ključni zaključak koristi se kvalitativni nivo pouzdanosti: **visok**, **srednji** ili **nizak**, uz kratko obrazloženje.

Kada nedostaje odlučna činjenica, zaključak se formuliše uslovno i navodi se dokaz koji bi ga mogao potvrditi ili opovrgnuti.

## 7. Samokontrola prije završetka

Svaki složeni prompt mora završiti internom kontrolom najmanje ovih pitanja:

1. Jesam li odgovorio na centralno pitanje?
2. Koje tvrdnje počivaju na direktnom dokazu, a koje na tumačenju?
3. Postoji li protivdokaz ili razumno alternativno objašnjenje koje nisam uzeo u obzir?
4. Jesam li izmislio ili neprovjereno pretpostavio datum, broj, pravilo, citat ili događaj?
5. Šta bi moglo promijeniti moj zaključak?
6. Može li drugi analitičar rekonstruisati kako sam došao do nalaza?

## 8. Verzije promptova

Materijalna izmjena zadatka, dokaznih pravila, izlazne strukture ili acceptance criteria zahtijeva novu verziju prompta. Kozmetičke izmjene ne zahtijevaju novu glavnu verziju.

Nova verzija složenog prompta ne dobija status stabilne verzije prije validacije prema `14_validacija_promptova.md`.

## 9. Referentna osnova

Standard je usklađen sa principima jasnog scoping-a, eksplicitnog konteksta, instrukcija, ograničenja, kriterijuma uspjeha i evaluacije promptova iz OpenAI vodiča *ChatGPT Enterprise: Practical prompt engineering for everyday work*, uz strožija dokazna pravila potrebna za Građansku forenziku.
