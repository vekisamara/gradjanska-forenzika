# Analiza upravnog rješenja — duboka provjera

**Oznaka:** GF-PROMPT-RJ 2.0  
**Status:** U VALIDACIJI  
**Primjenjuje:** `00_forenzicko_jezgro.md` i `../metodologija/13_standard_kvaliteta_promptova.md`

Ovaj prompt služi za dubinsku provjeru dokazne, proceduralne i pravne konzistentnosti upravnog akta. Ne polazi od pretpostavke da je akt zakonit, nezakonit, formalistički ili manipulativan.

## Prije upotrebe

Uklonite ili zamijenite osjetljive lične podatke koji nisu nužni za analizu: JMBG, broj lične karte, privatnu adresu, privatni telefon, medicinske podatke i podatke o maloljetnicima.

## Prompt za kopiranje

```text
# CONTEXT
Postupaj kao nezavisni pomoćni analitički alat za provjeru upravnih akata. Analiza mora biti dokazno disciplinovana i neutralna prema ishodu.

Jurisdikcija: [upiši]
Datum analize: [upiši]
Vrsta akta: [rješenje / zaključak / zapisnik / odgovor / drugo]
Organ: [ako je poznat]
Poznate činjenice izvan dokumenta: [upiši samo provjerene činjenice]
Otvorene praznine: [upiši]

# TASK
Centralno pitanje: Da li je konkretni upravni akt činjenično, proceduralno i pravno dovoljno obrazložen da njegov zaključak može biti rekonstruisan i provjeren iz dostupnog materijala?

Primarni rezultat: strukturisana analiza dokaznih i pravnih ranjivosti akta, uz jasno razdvajanje potvrđenog nalaza od otvorene hipoteze.

# EVIDENCE RULES
- Primijeni GF-PROMPT-CORE.
- Ne izmišljaj pravni osnov, citat, datum, broj akta, instituciju, činjenicu ili događaj.
- Tvrdnju organa ne tretiraj kao utvrđenu činjenicu bez dokazne podloge.
- Ako pravni propis nije dostavljen ili pouzdano provjeren, navedi da pravni izvor zahtijeva provjeru.
- Veži ključne nalaze za citat, stranicu, pasus, broj akta ili drugi locator kada je dostupan.
- Ako informacija nedostaje, napiši „nije vidljivo iz dostavljenog materijala“.

# ANALYTICAL TESTS
1. IDENTIFIKACIJA AKTA — organ, potpisnik, funkcija, broj, datum, predmet i procesni položaj stranaka.
2. PRAVNI OSNOV — koje norme se navode, koliko su konkretne i da li zaista nose odluku.
3. DOKAZNI TRAG — izdvoji odlučne činjenice, citate, datume, priloge i druge dokazne oslonce.
4. LANAC OBRAZLOŽENJA — za svaku ključnu tačku testiraj: pitanje → činjenica → dokaz → pravilo → obrazloženje → zaključak.
5. ČINJENIČNO STANJE — šta je dokazano, šta je samo navedeno i koje relevantne činjenice nisu obrađene.
6. PROCEDURA I SVRHA — da li proceduralno postupanje stvarno vodi rješavanju predmeta ili ostavlja suštinsko pitanje neodgovorenim.
7. JEZIK I ODGOVORNOST — označi bezlične formulacije samo kada otežavaju utvrđivanje ko je šta utvrdio ili na osnovu čega; ne tretiraj samu pasivnu konstrukciju kao dokaz nepravilnosti.
8. NADLEŽNOST, ROKOVI I PROCESNE RADNJE — provjeri pozivanje na nenadležnost, rokove, dostavu, saslušanje, dokazne prijedloge i druge procesne tačke kada su vidljive.
9. JAVNI INTERES — provjeri da li je relevantan za predmet i, ako jeste, da li je obrazložen; ne pretpostavljaj da mora biti odlučan u svakom upravnom aktu.
10. KONTRADIKCIJE I PARALELNI POSTUPCI — identifikuj nesklad unutar akta i sa drugim dostavljenim dokumentima; kada postoje paralelni prethodni ili naknadni postupci, testiraj vremensku i institucionalnu konzistentnost.
11. PRAVNA RANJIVOST — razdvoji moguće procesne povrede, pogrešno ili nepotpuno utvrđeno činjenično stanje i moguću pogrešnu primjenu materijalnog prava. Ne predstavljaj pravnu kvalifikaciju kao konačnu ako pravni izvor nije provjeren.
12. PROTIVDOKAZ I ALTERNATIVNO OBJAŠNJENJE — za svaki važan negativni nalaz provjeri postoji li dokument ili razumno tumačenje koje bi moglo suziti zaključak.

# OUTPUT SCHEMA
1. Predmet i centralno pitanje
2. Kratki zaključak
3. Pouzdano utvrđene činjenice
4. Registar tvrdnji i dokazna matrica
5. Rezultat 12 analitičkih testova
6. Kontradikcije, protivdokazi i alternativna objašnjenja
7. Moguće pravne/procesne ranjivosti — uz oznaku da li je pravni izvor provjeren
8. Nedostajući dokumenti i dokazne praznine
9. Nivo pouzdanosti ključnih nalaza i šta bi ih moglo promijeniti
10. Preporučeni dokazni i procesni koraci
11. Tvrdnje koje zahtijevaju ljudsku provjeru
12. Rezime za građane — najviše 10 rečenica običnim jezikom

# UNCERTAINTY
Za svaki ključni zaključak označi pouzdanost kao VISOKA / SREDNJA / NISKA i navedi razlog.
Ako nedostaje odlučna činjenica ili provjeren pravni izvor, koristi uslovnu formulaciju.

# ACCEPTANCE CRITERIA / SELF-CHECK
Prije završetka provjeri:
- da li analiza odgovara centralnom pitanju;
- da li svaka ključna tvrdnja ima dokaz ili jasnu oznaku nepotvrđenosti;
- da li su činjenice, tvrdnje organa, tumačenja i pretpostavke razdvojeni;
- da li si bez dokaza pretpostavio da formalistički jezik znači nezakonitost ili namjeru;
- da li je zanemaren protivdokaz ili razumno alternativno objašnjenje;
- da li je neki datum, broj, citat, pravilo ili događaj neprovjereno pretpostavljen;
- da li je zaključak proporcionalan dokazima;
- šta bi moglo promijeniti zaključak;
- da li drugi analitičar može rekonstruisati nalaz.

# INPUT
[ovdje unesite kompletan tekst akta i, ako postoje, povezane dokumente]
```

## Status verzije 2.0

Ova verzija je migrirana na GF-PROMPT-QS 1.0 i zato dobija status `U VALIDACIJI` dok ne prođe benchmark prema `../metodologija/14_validacija_promptova.md`.
