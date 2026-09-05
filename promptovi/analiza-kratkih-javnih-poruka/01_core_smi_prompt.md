# GFO SHORT MESSAGE ANALYSIS — CORE-SMI prompt

**Oznaka:** GF-SMA-CORE 0.2  
**Status:** U VALIDACIJI  
**Primjenjuje:** `../00_forenzicko_jezgro.md` i `../../metodologija/13_standard_kvaliteta_promptova.md`

```text
# CONTEXT
Predmet: kratka javna poruka / slogan / billboard / plakat / oglas
Datum analize:
Datum i lokacija poruke ako su poznati:
Autor/naručilac ako je potvrđen:
Vrsta izvora: fotografija / web / video / transkript / drugo
Kontekst: POLITICAL / COMMERCIAL / ACTIVIST / INSTITUTIONAL / NEUTVRĐENO

# TASK
Analiziraj konkretnu kratku javnu poruku i utvrdi njen dokazni sadržaj, implicitne pretpostavke, emocionalno i identitetsko uokviravanje, proizvedenu izvjesnost, binarizaciju, uzročno pojednostavljivanje i materijalno izostavljeni kontekst.

Primarni rezultat je SMI profil sa obrazloženjem, ne procjena autora.

Centralno pitanje:
Šta primalac poruke treba da osjeti, pretpostavi ili prihvati kao istinito, iako mu poruka za to nije ponudila odgovarajući dokaz ili kontekst?

# EVIDENCE RULES
- Primijeni GF-PROMPT-CORE.
- Analiziraj konkretnu poruku, ne reputaciju autora ili medija.
- Ne pripisuj namjeru bez nezavisnog dokaza.
- Ne tretiraj odsustvo dokaza kao dokaz suprotnog.
- Razdvoji ČINJENICU, TVRDNJU, TUMAČENJE, PRETPOSTAVKU i NEPOZNATO.
- Vrijeme objave, uključujući izborni period, samo je kontekst dok se ne poveže sa dodatnim dokazima.
- Neprovjerljivost sama po sebi nije manipulacija.
- Ne kažnjavaj poruku samo zato što je kratka, emocionalna ili uvjerljiva.

# MESSAGE ROLE CLASSIFICATION
Prije scoringa označi jednu ili više uloga:
DESCRIPTIVE CLAIM / ASPIRATIONAL / IMPERATIVE-MOBILIZING / IDENTITY-AFFILIATION / EVALUATIVE / PROMISE / THREAT-ACCUSATION.

Ne tretiraj ASPIRATIONAL ili IMPERATIVE-MOBILIZING konstrukciju kao opisnu tvrdnju o činjenici bez dodatnog jezičkog ili kontekstualnog osnova.

# MATERIALITY GATE
Prije VER i OMI bodovanja odgovori:
1. Koji konkretan zaključak poruka navodi primaoca da izvede?
2. Da li je taj zaključak materijalno važan za odluku primaoca?
3. Koji dokaz ili kontekst bi razumno mogao promijeniti tu odluku?

Ako poruka samo izražava opštu vrijednost, identitet ili aspiraciju bez materijalnog zaključka, VER i OMI su po pravilu 0–2.
Visoki VER/OMI (3–5) traže materijalno važan zaključak o rezultatu, prijetnji, cijeni, svojstvu, političkoj sposobnosti, institucionalnom ishodu ili slično, za koji nedostaje bitna osnova/kontekst.

# CORE-SMI TESTS
Ocijeni 0–5 i obrazloži svaki rezultat:

VER — Verification Deficit: nedostatak provjerljive osnove za materijalno važan zaključak.
PRE — Presupposition Loading.
EMO — Emotional Substitution.
IDA — Identity / Value Capture.
CER — Manufactured Certainty.
BIN — Binary Framing.
CAU — Causal Compression.
OMI — Omission / Context Suppression.

IDA anchor:
0 nema identitetskog/vrijednosnog elementa;
1–2 pozitivno povezivanje;
3 snažno simboličko povezivanje;
4 implicitno prisvajanje;
5 ekskluzivno prisvajanje koje protivnika implicitno izbacuje iz legitimnog kolektiva/moralne kategorije.

CER anchor:
0 nema ishoda/izvjesnosti;
1 aspiracija ili mobilizacijska formulacija;
2 snažno očekivanje;
3 implicitna izvjesnost;
4 gotovo gotov ishod;
5 neizvjestan politički/institucionalni/komercijalni ishod predstavljen kao činjenica/sigurnost.

BIN anchor:
visok BIN zahtijeva identifikovanu ili implicitno konstruisanu suprotnu stranu. Samo zajedništvo, kolektivni identitet ili poziv na jedinstvo nisu dovoljni.

Izračunaj SMI/40, ali uvijek prikaži i puni profil.

# PATTERN TAGS
Označi samo obrasce koji su stvarno prisutni:
IDENTITY_CAPTURE
MORAL_CAPTURE
UNIVERSAL_VALUE_CAPTURE
EMPTY_ENEMY
FALSE_CERTAINTY
OUTCOME_AS_FACT
INSTITUTIONAL_CHAIN_DELETION
PRESUPPOSITION_LOADING
EMOTIONAL_SUBSTITUTION
BINARY_FRAMING
SEMANTIC_FOG
ABSOLUTISM
CAUSAL_COMPRESSION
CONTEXT_SUPPRESSION

# VISUAL FRAMING
Ako postoji slika, analiziraj odnos teksta i vizuelnog sloja: osobe, simboli, zastave, grbovi, porodica/djeca, infrastruktura, proizvodi, hijerarhija veličine i položaja i implicitni zaključak kombinacije slike i teksta.
Ne povećavaj SMI samo zbog prisustva vizuelnih elemenata.

# DISTINCTION TEST
Za svaki problematičan element odredi da li je prvenstveno:
PERSUASION / SIMPLIFICATION / MANIPULATIVE PATTERN.

Manipulativni obrazac postoji samo kada poruka navodi na relevantan zaključak za koji ne daje odgovarajuću osnovu ili kada materijalno izostavljanje mijenja razumijevanje odluke primaoca.

# CONTEXT PROFILE
POLITICAL: provjeri izborna obećanja, identitetsko/moralno prisvajanje, konstrukciju protivnika, lažnu izvjesnost i institucionalni lanac.
COMMERCIAL: provjeri cijenu, uslove, rezultat, poređenja i materijalno izostavljene informacije.
ACTIVIST: provjeri šok, moralnu osudu, katastrofični okvir i mobilizacijsko pojednostavljivanje.
INSTITUTIONAL: provjeri plan→rezultat, javni novac→poklon/zasluga, početak→završetak i reputacijsko brendiranje.

# PUBLIC/MONOPOLY ADVERTISING TRIGGER
Ako je autor/naručilac institucija ili javno preduzeće, posebno monopolista/dominantan pružalac usluge, izvrši CNT i PMCT.

CNT — Commercial Necessity Test:
- izbor alternativnog pružaoca;
- tržišna konkurencija;
- konkretna nova usluga/proizvod;
- razumna veza sa prihodom/korištenjem;
- javnoinformativna svrha;
- dostupnost jeftinijih kanala.

PMCT — Public Money Communication Test:
NEC potreba;
PUB javna korisnost;
ALT alternativni kanali;
BEN stvarni reputacijski korisnik;
POL politička blizina;
TRA transparentnost troška/nabavke/plaćanja.

CNT/PMCT ne sabiraj sa SMI.

Postavi Beneficiary test:
Čije ponašanje poruka pokušava promijeniti i u čiju korist?

Izvrši Logo Removal i Actor Substitution test kao indikatore, nikada kao samostalne dokaze.

Ako postoji osnov za finansijsku provjeru, predloži lanac:
kampanja → naručilac → broj/lokacije → trajanje → budžetska stavka → nabavka/ugovor → agencija → oglasni prostor → plaćanje → dokumentovani cilj → mjerljivi rezultat.

# COUNTERFACTUAL BIAS TEST
Zamijeni autora hipotetičkim ideološki/politički suprotnim akterom uz istu strukturu poruke. Provjeri da li bi tehnike i bodovi ostali isti. Ako ne, revidiraj analizu ili objasni dokazno relevantnu razliku.

# OUTPUT SCHEMA
1. Poruka i kontekst
2. Message role
3. Doslovno značenje
4. Implicitna poruka
5. Presupozicije
6. Emocije i vrijednosti
7. Visual framing
8. Pattern tags
9. Materiality gate: PASS / LOW MATERIALITY / NOT APPLICABLE + obrazloženje
10. SMI profil: VER/PRE/EMO/IDA/CER/BIN/CAU/OMI + ukupno /40
11. Obrazloženje svakog boda
12. Persuasion / simplification / manipulative pattern razgraničenje
13. Materijalno nedostajući kontekst
14. Alternativno benigno tumačenje
15. Rezultat kontekstualnog profila
16. CNT/PMCT ako je aktiviran
17. Nivo pouzdanosti
18. Nedostajući dokazi
19. Sljedeći dokazni/forenzički korak
20. Namjera: UTVRĐENA / NIJE UTVRĐENA / NIJE MOGUĆE UTVRDITI, sa dokazom ako je utvrđena

# UNCERTAINTY
Za ključne nalaze koristi VISOKA / SREDNJA / NISKA pouzdanost.
Ako nedostaje kontekst originalne kampanje, naručilac, datum, trošak ili potpuni vizuelni prikaz, navedi ograničenje.

# ACCEPTANCE CRITERIA
- rezultat analizira poruku, ne autora;
- message role je određen prije scoringa;
- materiality gate je primijenjen prije visokih VER/OMI ocjena;
- aspiracija nije bodovana kao lažna izvjesnost bez dodatnog osnova;
- pozitivna identitetska asocijacija nije automatski tretirana kao ekskluzivno prisvajanje;
- BIN ima stvarnu ili implicitno konstruisanu suprotnu stranu;
- svaki SMI bod je obrazložen;
- legitimno ubjeđivanje i nužno pojednostavljivanje nisu automatski penalizovani;
- namjera nije izvedena iz efekta poruke;
- politički/ideološki counterfactual ne mijenja rezultat bez dokaznog razloga;
- kod javnog novca tržišna nepotrebnost nije automatski proglašena zloupotrebom;
- SMI i drugi GFO scoring sistemi nisu spojeni;
- jasno je šta bi moglo potvrditi, ograničiti ili opovrgnuti nalaz.

# INPUT
[unesi tekst, fotografiju i dostupni kontekst]
```
