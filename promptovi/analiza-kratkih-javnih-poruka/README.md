# GFO SHORT MESSAGE ANALYSIS — analiza kratkih javnih poruka

**Oznaka:** GF-SMA 0.1  
**Status:** U VALIDACIJI  
**Datum:** 2026-09-06

Ovaj modul analizira kratke javne poruke projektovane za brzu recepciju: političke slogane i plakate, jumbo reklame, komercijalne oglase, aktivističke poruke, institucionalne kampanje, poruke javnih preduzeća i slične vizuelno-tekstualne formate.

Modul ne polazi od identiteta autora, već od konkretne poruke, njenog dokaznog sadržaja, implicitnih pretpostavki, emocionalnog i vizuelnog uokviravanja, izostavljenog konteksta i efekta koji poruka može proizvesti kod primaoca.

## Centralno pitanje

> Šta primalac poruke treba da osjeti, pretpostavi ili prihvati kao istinito, iako mu poruka za to nije ponudila odgovarajući dokaz ili kontekst?

## Arhitektura

`ulaz: fotografija / slogan / plakat / kratka poruka`

→ identifikacija teksta i vizuelnog konteksta  
→ CORE-SMI analiza  
→ klasifikacija konteksta  
→ POLITICAL / COMMERCIAL / ACTIVIST / INSTITUTIONAL profil  
→ po potrebi routing prema drugim GFO modulima.

Modul je horizontalan. Ne mijenja postojeće scoring sisteme MEDIA, izbornog, PR ili PPT modula i ne spaja njihove bodove.

## SMI — Short Message Manipulation Index

SMI mjeri **manipulativni komunikacijski potencijal konkretne poruke**, a ne karakter, namjeru ili vjerodostojnost autora.

Osam dimenzija ocjenjuje se od 0 do 5:

1. **VER — Verification Deficit** — nedostatak provjerljivog sadržaja. Neprovjerljivost sama po sebi nije manipulacija.
2. **PRE — Presupposition Loading** — nedokazane pretpostavke koje primalac mora prihvatiti da bi poruka funkcionisala.
3. **EMO — Emotional Substitution** — stepen u kojem emocija zamjenjuje informaciju ili argument.
4. **IDA — Identity / Value Capture** — prisvajanje kolektivnog identiteta ili univerzalnih vrijednosti poput naroda, države, pravde, sigurnosti ili slobode.
5. **CER — Manufactured Certainty** — predstavljanje željenog ishoda, obećanja ili procjene kao izvjesnosti.
6. **BIN — Binary Framing** — svođenje složene stvarnosti na mi/oni, dobro/loše, patriote/izdajnici i slične dihotomije.
7. **CAU — Causal Compression** — svođenje složenog uzročnog lanca na jednostavnu vezu bez dovoljne dokazne osnove.
8. **OMI — Omission / Context Suppression** — izostavljanje informacije koja je bitna za pravilno razumijevanje poruke.

`SMI = VER + PRE + EMO + IDA + CER + BIN + CAU + OMI`

Maksimum je 40. Orijentaciona klasifikacija za validaciju:

- 0–7: minimalan;
- 8–14: nizak;
- 15–21: umjeren;
- 22–28: značajan;
- 29–34: visok;
- 35–40: vrlo visok manipulativni komunikacijski potencijal.

Ukupan broj se nikada ne objavljuje bez profila, npr. `SMI 27/40 [VER4 PRE5 EMO5 IDA4 CER1 BIN3 CAU2 OMI3]`.

## Taksonomija obrazaca

Modul može označiti, između ostalog:

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

Kod fotografije/plakata tekst se ne analizira izolovano. Posebno se evidentiraju:

- dominantne osobe i objekti;
- zastave, grbovi, institucionalni i politički simboli;
- porodica, djeca, uniforma, infrastruktura i drugi emocionalni markeri;
- hijerarhija veličine i položaja;
- odnos slike i teksta;
- implicitni zaključak koji nastaje njihovom kombinacijom.

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

Provjerava:

1. može li korisnik realno izabrati drugog pružaoca;
2. postoji li konkurencija kojoj oglašavanje može oduzeti tržišni udio;
3. promoviše li se konkretna nova usluga/proizvod;
4. može li oglašavanje razumno povećati prihod ili korištenje usluge;
5. postoji li jasna javnoinformativna svrha;
6. da li se ista informacija mogla prenijeti znatno jeftinijim institucionalnim kanalima.

Slabo tržišno opravdanje nije dokaz zloupotrebe; ono je trigger za dublju analizu.

### Public Money Communication Test — PMCT

Analizira:

- **NEC — Necessity:** dokaziva potreba za kampanjom;
- **PUB — Public Utility:** konkretna korisna informacija za građanina;
- **ALT — Alternative Channels:** dostupnost razumno jeftinijih kanala;
- **BEN — Beneficiary:** ko prima stvarnu reputacijsku korist;
- **POL — Political Proximity:** vremenska, semantička, personalna i vizuelna blizina političkoj promociji;
- **TRA — Transparency:** cijena, naručilac, postupak, dobavljač i plaćanje.

PMCT je odvojen od SMI i njegovi bodovi se ne sabiraju sa SMI.

## Beneficiary test

Postavlja se pitanje:

> Čije ponašanje ova poruka pokušava promijeniti i u čiju korist?

Kod monopoliste posebno se provjerava da li kampanja realno promoviše uslugu ili prvenstveno reputaciju institucije, rukovodstva ili političkih aktera povezanih sa njom.

## Logo Removal i Actor Substitution test

Kod institucionalnog/javnog billboarda:

1. mentalno ukloniti logo institucije i provjeriti da li ostatak izgleda kao politička promocija;
2. hipotetički zamijeniti logo institucije logom političkog subjekta i provjeriti da li poruka i vizuelni jezik i dalje prirodno funkcionišu.

Rezultat je indikator za dodatnu provjeru, nikada samostalan dokaz političke propagande.

## Izborni period

Vrijeme objave tokom izborne kampanje je kontekst, ne dokaz namjere. Jači nalaz zahtijeva konvergenciju nezavisnih indikatora, npr. javni novac + izborni period + slaba javna/tržišna potreba + semantička sličnost političkoj kampanji + prisustvo funkcionera + dokumentovana nabavka/plaćanje.

## Routing prema finansijskoj i institucionalnoj forenzici

Kada postoji javni novac, analiza se može nastaviti lancem:

`kampanja → naručilac → broj/lokacije plakata → trajanje → budžetska stavka → nabavka/ugovor → marketinška agencija → vlasnik oglasnog prostora → plaćanje → dokumentovani cilj → mjerljivi rezultat`

Za infrastrukturne ili projektne tvrdnje routing može nastaviti u GFO PPT lanac PR → nabavka → ugovor/nalog → izvršenje → plaćanje → rezultat.

## Zaštite od političke i analitičke pristrasnosti

### Counterfactual test

Model mora pitati da li bi istu tehniku i isti broj bodova dodijelio kada bi identičnu strukturu poruke koristio ideološki ili politički suprotan akter. Promjena rezultata samo zbog identiteta autora znači da analiza nije dovoljno neutralna.

### Namjera i uzročnost

SMI analizira strukturu i mogući komunikacijski efekat. Rezultat nije dokaz da je autor namjeravao manipulisati primaocima, niti procjena političkog subjekta, institucije, kompanije ili organizacije u cjelini.

Odsustvo dokaza o tržišnoj/javnoj potrebi nije dokaz da potreba ne postoji. Odsustvo pronađene nabavke ili ugovora nije dokaz da dokument ne postoji.

## Standardni izlaz

Svaka analiza treba sadržati:

1. identifikaciju poruke, autora/naručioca ako je poznat, datum i lokaciju/izvor;
2. doslovno značenje;
3. implicitnu poruku;
4. ključne presupozicije;
5. dominantne emocije i vrijednosti;
6. vizuelno uokviravanje kada postoji;
7. označene obrasce;
8. SMI profil i obrazloženje svakog boda;
9. materijalno nedostajući kontekst;
10. alternativno benigno tumačenje;
11. kontekstualni profil i dodatne testove;
12. nivo pouzdanosti;
13. nedostajuće dokaze i sljedeći korak;
14. eksplicitnu napomenu da namjera nije utvrđena ako za nju nema nezavisnih dokaza.

## Validacija v0.1

Prije stabilizacije modul treba testirati na najmanje 20–30 stvarnih poruka iz različitih kategorija. Početni dataset može koristiti kampanju za Opšte izbore BiH 2026, ali validacija mora uključiti i komercijalne, aktivističke i institucionalne/javne kampanje.

Cilj validacije je provjeriti međuanalitičku konzistentnost, političku neutralnost, granicu persuasion/simplification/manipulative pattern, korisnost SMI profila i stabilnost CNT/PMCT testova.

Vidi operativni prompt: [`01_core_smi_prompt.md`](01_core_smi_prompt.md).
