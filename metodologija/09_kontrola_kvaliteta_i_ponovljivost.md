# Kontrola kvaliteta i ponovljivost

**Oznaka:** GF-MET-QA 1.1

## 1. Nezavisni drugi prolaz

Kontrolor ne pokušava potvrditi početni rezultat. Njegov zadatak je pronaći pogrešan citat, preširok zaključak, zanemaren protivdokaz, neprovjeren pravni izvor, nejasnu oznaku, pogrešno računanje roka ili razumno alternativno objašnjenje.

Za složene AI analize kontrolor provjerava i da li su zadatak, izlaz i acceptance criteria bili dovoljno jasno definisani prema `13_standard_kvaliteta_promptova.md`.

## 2. Obavezna checklista prije objave

- [ ] Predmet i centralno pitanje su precizni.
- [ ] Primarni rezultat prompta je jasno definisan.
- [ ] Sve ključne tvrdnje imaju stabilan ID.
- [ ] Citati su provjereni prema originalu i imaju lokaciju.
- [ ] Datumi, brojevi akata, iznosi i poveznice su ponovo provjereni.
- [ ] Tvrdnje izvora nisu predstavljene kao utvrđene činjenice.
- [ ] Pravni izvor je provjeren prema jurisdikciji i datumu.
- [ ] Planska i konačna vrijednost nisu pomiješane.
- [ ] Aktivnost nije predstavljena kao učinak bez indikatora.
- [ ] Odsustvo dostavljenog dokaza nije predstavljeno kao nepostojanje.
- [ ] Najmanje jedno alternativno objašnjenje je razmotreno kada je relevantno.
- [ ] Poznati protivdokaz nije prećutan.
- [ ] Zaključak je proporcionalan dokazima.
- [ ] Nivo pouzdanosti je obrazložen.
- [ ] Navedeno je šta bi moglo promijeniti zaključak.
- [ ] Tvrdnje koje zahtijevaju ljudsku provjeru su jasno označene.
- [ ] Osjetljivi podaci su uklonjeni ili opravdano zadržani.
- [ ] Instituciji/pogođenoj strani je omogućeno pravo na odgovor kada je primjenjivo.
- [ ] Čitalac može razlikovati činjenicu, tumačenje i otvoreno pitanje.

## 3. Acceptance test izlaza

Kontrolor mora moći odgovoriti sa `DA` na sljedeća pitanja:

1. Da li izlaz direktno odgovara centralnom pitanju?
2. Da li je svaka ključna tvrdnja dokazno klasifikovana?
3. Da li su neizvjesnosti vidljive umjesto prikrivene uvjerljivim jezikom?
4. Da li se iz istog materijala može rekonstruisati osnovni put do zaključka?
5. Da li je jasno koji novi dokaz može potvrditi ili opovrgnuti otvoreni nalaz?

Ako je odgovor `NE`, dokument ne može dobiti status `SPREMNO`.

## 4. Test ponovljivosti

Drugi analitičar mora iz registra izvora moći:

1. pronaći korišteni dokument i njegovu verziju;
2. locirati citat ili podatak;
3. rekonstruisati status tvrdnje;
4. ponoviti računanje roka ili iznosa;
5. razumjeti zašto je alternativno objašnjenje prihvaćeno ili odbačeno;
6. razlikovati dokaz od AI prijedloga i ljudske procjene;
7. razumjeti šta je bio primarni zadatak prompta i po kojim kriterijumima je izlaz prihvaćen.

## 5. Regresiona kontrola prompta

Ako QA otkrije grešku koja je posljedica nejasne ili nedovoljne instrukcije prompta, greška se ne ispravlja samo ručno u jednom predmetu. Potrebno je:

1. evidentirati tip greške;
2. po potrebi izmijeniti prompt;
3. dodati slučaj u regresioni set;
4. ponoviti relevantne testove prema `14_validacija_promptova.md`.

Time stvarni predmeti postaju kontrolisani izvor učenja bez pretvaranja pojedinačnog nalaza u univerzalno pravilo.

## 6. Ishod kontrole

Dokument dobija jedan status: `SPREMNO`, `SPREMNO UZ OGRANIČENJA`, `DOPUNITI DOKAZE`, `REVIDIRATI ZAKLJUČAK` ili `NE OBJAVLJIVATI`.

Prompt ili njegova nova verzija zasebno dobija status: `STABILAN`, `U VALIDACIJI` ili `POVUČEN` prema `14_validacija_promptova.md`.
