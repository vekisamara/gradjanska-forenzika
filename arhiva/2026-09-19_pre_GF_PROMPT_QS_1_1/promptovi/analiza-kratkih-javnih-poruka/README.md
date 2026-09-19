# GFO SHORT MESSAGE ANALYSIS — analiza kratkih javnih poruka

**Oznaka:** GF-SMA 0.2  
**Status:** U VALIDACIJI  
**Datum:** 2026-09-06

Ovaj modul analizira kratke javne poruke projektovane za brzu recepciju: političke slogane i plakate, jumbo reklame, komercijalne oglase, aktivističke poruke, institucionalne kampanje, poruke javnih preduzeća i slične vizuelno-tekstualne formate.

Modul ne polazi od identiteta autora, već od konkretne poruke, njenog dokaznog sadržaja, implicitnih pretpostavki, emocionalnog i vizuelnog uokviravanja, izostavljenog konteksta i efekta koji poruka može proizvesti kod primaoca.

## Centralno pitanje

> Šta primalac poruke treba da osjeti, pretpostavi ili prihvati kao istinito, iako mu poruka za to nije ponudila odgovarajući dokaz ili kontekst?

## Arhitektura

`ulaz: fotografija / slogan / plakat / kratka poruka`

→ identifikacija teksta i vizuelnog konteksta  
→ klasifikacija jezičke uloge poruke  
→ materiality gate  
→ CORE-SMI analiza  
→ klasifikacija konteksta  
→ POLITICAL / COMMERCIAL / ACTIVIST / INSTITUTIONAL profil  
→ po potrebi routing prema drugim GFO modulima.

Modul je horizontalan. Ne mijenja postojeće scoring sisteme MEDIA, izbornog, PR ili PPT modula i ne spaja njihove bodove.

## SMI — Short Message Manipulation Index

SMI mjeri **manipulativni komunikacijski potencijal konkretne poruke**, a ne karakter, namjeru ili vjerodostojnost autora.

### Obavezna preklasifikacija poruke

Prije bodovanja poruka se označava kao jedna ili više uloga:

- DESCRIPTIVE CLAIM — opisna/provjerljiva tvrdnja;
- ASPIRATIONAL — želja, cilj ili vizija;
- IMPERATIVE / MOBILIZING — poziv ili mobilizacija;
- IDENTITY / AFFILIATION — identitetsko povezivanje;
- EVALUATIVE — vrijednosna ocjena;
- PROMISE — obećanje budućeg ishoda;
- THREAT / ACCUSATION — prijetnja, optužba ili konstrukcija protivnika.

Ova klasifikacija sprečava da se aspiracija automatski tretira kao tvrdnja o činjenici.

### Materiality gate

VER i OMI ne dobijaju visoke bodove samo zato što je slogan kratak. Prije bodovanja mora se utvrditi postoji li **materijalno važan zaključak** koji može uticati na odluku primaoca.

Ako poruka samo izražava opštu vrijednost ili aspiraciju bez konkretnog zaključka, VER i OMI su po pravilu 0–2.

Ako poruka navodi primaoca na zaključak o rezultatu, prijetnji, cijeni, svojstvu proizvoda/usluge, političkoj sposobnosti, institucionalnom ishodu ili drugoj odluci, VER/OMI mogu biti 3–5 kada relevantna dokazna osnova ili kontekst nedostaju.

### Osam dimenzija

1. **VER — Verification Deficit** — nedostatak provjerljive osnove za materijalno važan zaključak. Neprovjerljivost sama po sebi nije manipulacija.
2. **PRE — Presupposition Loading** — nedokazane pretpostavke koje primalac mora prihvatiti da bi poruka funkcionisala.
3. **EMO — Emotional Substitution** — stepen u kojem emocija zamjenjuje informaciju ili argument.
4. **IDA — Identity / Value Capture** — prisvajanje kolektivnog identiteta ili univerzalnih vrijednosti. Pozitivno povezivanje sa identitetom nije isto što i ekskluzivno prisvajanje.
5. **CER — Manufactured Certainty** — predstavljanje željenog ishoda, obećanja ili procjene kao izvjesnosti. Aspiracija ili mobilizacijska formulacija ne dobija visok CER bez deklarativne tvrdnje o izvjesnosti.
6. **BIN — Binary Framing** — svođenje složene stvarnosti na mi/oni, dobro/loše, patriote/izdajnici i slične dihotomije. Samo prisustvo kolektivnog identiteta nije dovoljno.
7. **CAU — Causal Compression** — svođenje složenog uzročnog lanca na jednostavnu vezu bez dovoljne dokazne osnove.
8. **OMI — Omission / Context Suppression** — izostavljanje informacije koja je materijalno bitna za pravilno razumijevanje poruke.

`SMI = VER + PRE + EMO + IDA + CER + BIN + CAU + OMI`

Maksimum je 40. Orijentaciona klasifikacija za validaciju:

- 0–7: minimalan;
- 8–14: nizak;
- 15–21: umjeren;
- 22–28: značajan;
- 29–34: visok;
- 35–40: vrlo visok manipulativni komunikacijski potencijal.

Ukupan broj se nikada ne objavljuje bez profila, npr. `SMI 25/40 [VER3 PRE4 EMO5 IDA4 CER1 BIN5 CAU0 OMI3]`.

## Dodatna pravila kalibracije v0.2

### IDA anchor

- 0: nema identitetskog/vrijednosnog elementa;
- 1–2: pozitivno povezivanje sa vrijednošću ili zajednicom;
- 3: snažno simboličko povezivanje;
- 4: implicitno prisvajanje vrijednosti/identiteta;
- 5: ekskluzivno prisvajanje koje protivnika implicitno izbacuje iz legitimnog kolektiva ili moralne kategorije.

### CER anchor

- 0: nema ishoda/izvjesnosti;
- 1: aspiracija ili mobilizacijska formulacija;
- 2: snažno očekivanje bez pune deklarativne izvjesnosti;
- 3: implicitna izvjesnost;
- 4: gotovo gotov ishod;
- 5: neizvjestan politički/institucionalni/komercijalni ishod predstavljen kao činjenica ili sigurnost.

### BIN anchor

Binarizacija traži identifikovanu ili implicitno konstruisanu suprotnu stranu. Poziv na jedinstvo ili zajedništvo sam po sebi ne dobija visok BIN.

## Taksonomija obrazaca

- `IDENTITY_CAPTURE`
- `MORAL_CAPTURE`
- `UNIVERSAL_VALUE_CAPTURE`
- `EMPTY_ENEMY`
- `FALSE_CERTAINTY`
- `OUTCOME_AS_FACT`
- `INSTITUTIONAL_CHAIN_DELETION`
- `PRESUPPOSITION_LOADING`
- `EMOTIONAL_SUBSTITUTION`
- `BINARY_FRAMING`
- `SEMANTIC_FOG`
- `ABSOLUTISM`
- `CAUSAL_COMPRESSION`
- `CONTEXT_SUPPRESSION`

Taksonomija je proširiva kroz validaciju i regresione testove.

## Kontekstualni profili

### POLITICAL

Dodatno provjerava izborna obećanja, identitetsko i moralno prisvajanje, konstrukciju protivnika, lažnu izvjesnost i brisanje institucionalnog lanca potrebnog za obećani ishod.

### COMMERCIAL

Provjerava tvrdnje o proizvodu, cijeni, rezultatu, poređenju, uslovima ponude i materijalno izostavljenim informacijama.

### ACTIVIST

Provjerava mobilizacijsko pojednostavljivanje, šok, moralnu osudu, katastrofični okvir i da li pojednostavljivanje proizvodi pogrešnu predstavu o problemu.

### INSTITUTIONAL

Provjerava da li institucija plan predstavlja kao rezultat, ulaganje kao vlastitu zaslugu, javni novac kao poklon, početak kao završetak ili reputacijski slogan kao javnu informaciju.

## Visual Framing Layer

Kod fotografije/plakata tekst se ne analizira izolovano. Posebno se evidentiraju dominantne osobe i objekti, simboli, zastave i grbovi, porodica/djeca, uniforma, infrastruktura, proizvodi, hijerarhija veličine i položaja, odnos slike i teksta i implicitni zaključak kombinacije slike i teksta.

Vizuelni sloj ne povećava automatski SMI. Mora se objasniti konkretna veza sa nalazom.

## Tri obavezne distinkcije

Analiza mora razlikovati:

- **PERSUASION** — legitimno ubjeđivanje;
- **SIMPLIFICATION** — nužno pojednostavljivanje zbog kratkog formata;
- **MANIPULATIVE PATTERN** — tehnika koja navodi na relevantan zaključak za koji poruka ne daje odgovarajuću osnovu.

Centralni test nije da li je poruka pojednostavljena, nego da li pojednostavljivanje mijenja razumijevanje stvarnosti na način bitan za odluku primaoca.

## Javni novac i monopolističko oglašavanje

Ako je naručilac institucija ili javno preduzeće, posebno kada ima monopolistički ili dominantan položaj, aktiviraju se dodatni testovi.

### Commercial Necessity Test — CNT

Provjerava: izbor alternativnog pružaoca; tržišnu konkurenciju; konkretnu novu uslugu/proizvod; razumnu vezu sa prihodom/korištenjem; javnoinformativnu svrhu; dostupnost jeftinijih institucionalnih kanala.

Slabo tržišno opravdanje nije dokaz zloupotrebe; ono je trigger za dublju analizu.

### Public Money Communication Test — PMCT

Analizira:

- **NEC — Necessity**;
- **PUB — Public Utility**;
- **ALT — Alternative Channels**;
- **BEN — Beneficiary**;
- **POL — Political Proximity**;
- **TRA — Transparency**.

PMCT je odvojen od SMI i njegovi bodovi se ne sabiraju sa SMI.

## Beneficiary test

> Čije ponašanje ova poruka pokušava promijeniti i u čiju korist?

Kod monopoliste posebno se provjerava da li kampanja realno promoviše uslugu ili prvenstveno reputaciju institucije, rukovodstva ili političkih aktera povezanih sa njom.

## Logo Removal i Actor Substitution test

Kod institucionalnog/javnog billboarda mentalno ukloniti logo institucije i provjeriti da li ostatak izgleda kao politička promocija; zatim hipotetički zamijeniti logo institucije logom političkog subjekta i provjeriti da li poruka i vizuelni jezik i dalje prirodno funkcionišu.

Rezultat je indikator za dodatnu provjeru, nikada samostalan dokaz političke propagande.

## Izborni period

Vrijeme objave tokom izborne kampanje je kontekst, ne dokaz namjere. Jači nalaz zahtijeva konvergenciju nezavisnih indikatora.

## Routing prema finansijskoj i institucionalnoj forenzici

`kampanja → naručilac → broj/lokacije plakata → trajanje → budžetska stavka → nabavka/ugovor → marketinška agencija → vlasnik oglasnog prostora → plaćanje → dokumentovani cilj → mjerljivi rezultat`

Za infrastrukturne ili projektne tvrdnje routing može nastaviti u GFO PPT lanac PR → nabavka → ugovor/nalog → izvršenje → plaćanje → rezultat.

## Zaštite od političke i analitičke pristrasnosti

### Counterfactual test

Model mora pitati da li bi istu tehniku i isti broj bodova dodijelio kada bi identičnu strukturu poruke koristio ideološki ili politički suprotan akter.

### Namjera i uzročnost

SMI analizira strukturu i mogući komunikacijski efekat. Rezultat nije dokaz da je autor namjeravao manipulisati primaocima, niti procjena političkog subjekta, institucije, kompanije ili organizacije u cjelini.

Odsustvo dokaza o tržišnoj/javnoj potrebi nije dokaz da potreba ne postoji. Odsustvo pronađene nabavke ili ugovora nije dokaz da dokument ne postoji.

## Standardni izlaz

Svaka analiza treba sadržati:

1. identifikaciju poruke, autora/naručioca ako je poznat, datum i lokaciju/izvor;
2. jezičku ulogu poruke;
3. doslovno značenje;
4. implicitnu poruku;
5. ključne presupozicije;
6. dominantne emocije i vrijednosti;
7. vizuelno uokviravanje kada postoji;
8. označene obrasce;
9. rezultat materiality gate-a;
10. SMI profil i obrazloženje svakog boda;
11. materijalno nedostajući kontekst;
12. alternativno benigno tumačenje;
13. kontekstualni profil i dodatne testove;
14. nivo pouzdanosti;
15. nedostajuće dokaze i sljedeći korak;
16. eksplicitnu napomenu da namjera nije utvrđena ako za nju nema nezavisnih dokaza.

## Validacija

Prvi politički kalibracioni test izveden je 6.9.2026. na sloganima kampanje za Opšte izbore 2026. i dokumentovan u [`validation/2026-09-06_political_slogans_rs.md`](validation/2026-09-06_political_slogans_rs.md).

Test je doveo do tri korekcije v0.2: materiality gate za VER/OMI, razdvajanje aspiracije od proizvedene izvjesnosti u CER i preciznije razdvajanje pozitivnog identitetskog povezivanja od ekskluzivnog prisvajanja u IDA/BIN.

Prije stabilizacije modul i dalje treba testirati na najmanje 20–30 poruka iz različitih kategorija, uključujući komercijalne, aktivističke i institucionalne/javne kampanje.

Vidi operativni prompt: [`01_core_smi_prompt.md`](01_core_smi_prompt.md).
