# Civic Forensics Research Center — Concept v0.1

**Radni naziv:** CF Istraživački centar / Civic Forensics Research Center  
**Oznaka:** CF-RC 0.1  
**Status:** strateški razvojni koncept — nije postojeća organizaciona sposobnost  
**Datum:** 9. septembar 2026.

## 1. Vizija

CF Istraživački centar je dugoročni razvojni pravac Građanske forenzike: nezavisna istraživačka infrastruktura za razvoj, validaciju, primjenu i javno mjerenje metodologija koje povezuju dokaznu disciplinu, odgovornu upotrebu AI-a, građansku sposobnost provjere i kvalitet institucionalnog odgovora.

Centar nije zamišljen samo kao baza podataka niti samo kao edukativni program. Njegov razvojni ciklus je:

> **Develop → Teach → Apply → Measure → Validate → Publish → Improve**

## 2. Razvojna hipoteza

Početno istraživačko pitanje je:

> **Mogu li AI-potpomognute, dokazno disciplinovane metode pouzdano mjeriti i pomoći poboljšanju kvaliteta institucionalnog odgovora građanima?**

Ako validacija uspije, sljedeće pitanje je:

> **Može li se takvo mjerenje skalirati u transparentnu longitudinalnu dokaznu osnovu za Bosnu i Hercegovinu, uz jasno poznate granice uzorka i inferencije?**

CF-RC ne pretpostavlja pozitivan odgovor; razvoj mora biti empirijski testiran.

## 3. Pet stubova

### 3.1 Methodology & AI Research

- razvoj i održavanje CF metodologija, taksonomija i measurement protocol-a;
- razvoj ARCM/JARM i budućih domenskih modula;
- odgovorna upotreba AI-a za ekstrakciju, mapiranje, poređenje, signalizaciju i mjerenje;
- kalibracija, regression testing, inter-analyst provjera i false-positive/false-negative analiza;
- versioning metodologije, taksonomije i AI modela;
- istraživanje novih indikatora bez pretvaranja AI izlaza u dokaz.

### 3.2 Education & Real-World Validation

- learning design i praktična edukacija korisnika;
- obuka građana, civilnog društva, novinara, istraživača i drugih relevantnih grupa;
- kontrolisana primjena metodologije u stvarnim situacijama;
- mjerenje da li drugi korisnici mogu pravilno primijeniti metod;
- feedback loop prema metodološkom razvoju;
- razvoj budućih trenera tek nakon demonstrirane pravilne primjene.

Edukacioni partner ne mora biti dio organizacione strukture CF-RC; može djelovati kao **Education & User Validation Partner**.

### 3.3 Academic Research & Talent Network

Visokoškolske ustanove treba predvidjeti kao poseban razvojni kanal, a ne samo kao povremene konsultante.

Mogući nivoi saradnje:

**Studentska praksa i istraživačko osposobljavanje**
- praksa studenata prava, javne uprave, političkih nauka, novinarstva, sociologije, statistike, računarstva/data science i drugih relevantnih disciplina;
- rad na sintetičkim, anonimizovanim ili research-grade skupovima u skladu sa Data Governance pravilima;
- kodiranje institucionalnih odgovora, provjera AI klasifikacije, inter-rater testiranje, analiza podataka i razvoj istraživačkih pitanja.

Razvojni put može biti:

`Intern → Trained Coder → Validated Analyst → Research Assistant → Methodology Contributor`

**Akademska validacija metodologije**
- asistenti, istraživači i profesori mogu učestvovati u dizajnu i nezavisnoj provjeri measurement protocol-a;
- pravne discipline: granica response-quality analize i pravne ocjene;
- statistika/metodologija: sampling, denominatori, reprezentativnost, uncertainty i longitudinalna uporedivost;
- javna uprava: administrativni procesi i institutional-response design;
- computer/data science: AI evaluacija, deduplikacija, reproducibilnost i data engineering;
- druge oblasti prema domenu budućeg modula.

**Zajednički razvoj budućih metodologija**

Model:

`CF methodology researchers + domain academics + assistants + students + practitioners`

Razvojni ciklus:

`real-world problem → CF research question → domain expertise → methodology prototype → controlled testing → real-world validation → data → independent/peer review → methodology release`

Akademski partnerstvo ne daje automatski pristup sirovim predmetima. Pristup podacima zavisi od svrhe, minimizacije, pravne osnove, privacy/security pravila i Data Governance protokola.

Nijedna konkretna visokoškolska ustanova ne smatra se partnerom dok saradnja nije stvarno dogovorena.

### 3.4 Data & Measurement Infrastructure

Ovaj stub koristi CF Institutional Response Data & Measurement Architecture (CF-IR-DMA).

Predviđeni ulazni kanali:

`Citizens | CSO/legal-aid organisations | Public institutions | Controlled research samples`

Funkcije uključuju provenance, privacy-by-design, `MATTER → CASE → SOURCE_RECORD` model, deduplikaciju, source-specific statistiku, validation levels i longitudinalno čuvanje podataka.

Preklapanje izvora se koristi i kao mogućnost cross-source validacije. Jedan stvarni predmet ostaje jedna case-level statistička jedinica, ali može imati više odvojenih source zapisa.

### 3.5 Institutional Response Observatory

Dugoročna funkcija je periodično javno mjerenje kvaliteta institucionalnog odgovora kroz validirane indikatore, transparentnu metodologiju i jasno navedena ograničenja.

Mogući izlazi:

- periodični izvještaji;
- javni dashboard;
- source-specific i sektorska mjerenja;
- longitudinalni trendovi;
- institucionalni feedback;
- istraživački datasetovi gdje governance to dozvoljava.

Centar u ranoj fazi ne uvodi jedan zbirni "CF Score" institucije. Rezultati treba da zadrže pojedinačne dimenzije kao što su Question Coverage, Evidence Trace, New Evidence Responsiveness, Closure Integrity i Citizen Actionability.

Svaki javni rezultat mora, gdje je relevantno, prikazati najmanje: `N`, period, source composition, sampling method, coverage/limitations, validation level i methodology version.

## 4. Dvije klase javnog mjerenja

### 4.1 Observed CF Dataset Statistics

Kontinuirani agregati nad predmetima koji su stvarno ušli u CF sistem. Formulacija mora biti ograničena na analizirani dataset, npr. "među predmetima analiziranim kroz CF metodologiju".

Veliki `N` ne znači reprezentativnost.

### 4.2 CF Representative Measurement

Populaciona inferencija je dozvoljena samo kada postoji posebno dizajniran i dokumentovan uzorak, poznat denominator/coverage i statistički opravdana metodologija.

Self-selected citizen/CSO dataset ne smije se predstavljati kao reprezentativan za sve institucionalne odgovore.

## 5. Institutional Administrative Data Registry

CF-RC može razvijati registar koji za relevantne institucije dokumentuje:

`what is recorded | classification | period | denominator | methodology | machine-readable availability | missing fields`

Javno dostupni izvještaji, FOI podaci, šifarnici i metodologije mogu činiti **Institutional Data Layer**. Individualni/multi-source predmeti čine odvojeni **Case Evidence Layer**. Ta dva sloja se mogu povezivati radi coverage-a i istraživačkog dizajna, ali se ne smiju metodološki stapati.

## 6. Stakeholder model

CF-RC je zamišljen kao istraživački ekosistem u kojem različiti akteri imaju različite uloge:

- **Citizens** — korisnici metodologije i dobrovoljni data contributors;
- **Civil society / legal-aid organisations** — education, user validation, nezavisni korpusi, research/data contribution;
- **Public institutions** — institutional data and improvement partners, self-check i kontrolisani uzorci;
- **Universities / higher-education institutions** — academic validation, domain expertise, studentski research pathway i zajednički razvoj metodologija;
- **CF Research Center** — methodology stewardship, measurement protocol, data/statistical governance, integracija istraživanja i javno izvještavanje.

Doprinos podataka ili finansiranje ne daju kontrolu nad metodološkim rezultatom.

## 7. Governance i nezavisnost

Razvoj Centra zahtijeva najmanje četiri odvojena governance područja:

1. **Methodology Governance** — šta se mjeri, kako se instrument mijenja i validira;
2. **Data Governance** — provenance, pristup, privacy, deduplikacija, retention i korekcije;
3. **Statistical Governance** — sampling, denominatori, agregiranje, uncertainty i uslovi za populacionu inferenciju;
4. **Publication Governance** — javni pragovi, suppression, verzije, korekcije i institucionalni right of response.

Princip:

> **data contribution ≠ funding ≠ methodological control ≠ validation ≠ publication control**

Institucija ili drugi akter mora imati mogućnost da ukaže na činjeničnu grešku i pruži dokumentovani odgovor, ali ne i pravo veta na metodološki validan nalaz.

## 8. Institucionalno učenje, ne samo rangiranje

CF-RC nije zamišljen samo kao infrastruktura za kritiku institucija. Measurement results treba koristiti i za:

- identifikaciju sistemskih response-quality problema;
- razvoj jasnijih response templates i evidence-trace prakse;
- institucionalni self-check;
- obuke i prije/poslije mjerenja;
- provjeru da li se kvalitet odgovora tokom vremena poboljšava.

Razvojni model:

`baseline → intervention/training → follow-up measurement → learning → methodology/process improvement`

## 9. Veza sa CF metodologijom

CF-RC je budući istraživački i organizacioni krov; ne zamjenjuje postojeće metodologije.

- GF-MET i povezani standardi uređuju dokaznu disciplinu;
- CF-IRQF definiše measurement framework za institucionalni odgovor;
- ARCM/JARM su domenske primjene;
- CF-IR-DMA definiše višekanalnu data/measurement arhitekturu;
- MDAP određuje procesne posljedice, prioritete, rokove i eskalaciju u konkretnim administrativnim predmetima;
- NIR se aktivira samo nakon routing gate-a i ne može odgoditi MDAP zaštitu ili rok.

## 10. Razvojne faze

### CURRENT CAPABILITY

CF ima metodološke komponente i razvojne module koji se primjenjuju/kalibrišu. CF-RC kao istraživački centar još nije uspostavljena sposobnost.

### VALIDATION PHASE

Cilj je testirati:

- pouzdanost instrumenta;
- transferability prema drugim korisnicima;
- multi-source validity;
- AI/human reproducibility;
- mogućnost metodološki odbranjivih agregatnih indikatora;
- institucionalnu korisnost rezultata;
- mogućnost uključivanja akademskih partnera i studentskog research pathway-a.

### LONG-TERM VISION

Ako validacija uspije:

`validated methods → CF Research Center MVP → scaled multi-source acquisition → public measurement → longitudinal observatory → continuous methodology development`

## 11. Donorski i EU razvojni okvir

CF-RC se ne predstavlja kao već postojeći centar niti kao zahtjev da donor odmah finansira punu infrastrukturu.

Prva moguća donorska faza je **multi-stakeholder validation pilot** koji ispituje da li postoji pouzdana osnova za budući istraživački i measurement kapacitet.

Centralno pitanje za potencijalnog partnera/donora:

> **Can a transparent, independently validated methodology reliably measure institutional response quality across different users, institutions and data sources, and can the resulting evidence support measurable institutional learning?**

Dugoročna vizija može se predstaviti kao razvoj **Civic Forensics Research Center** koji povezuje građane, civilno društvo, javne institucije i akademsku zajednicu oko razvoja, validacije i primjene evidence-disciplined, responsible AI-assisted metoda.

## 12. Status i safeguards

CF-RC 0.1 je strateški razvojni koncept.

Ne tvrdi da trenutno postoje:

- formalno uspostavljen istraživački centar;
- ugovoreni univerzitetski ili institucionalni partneri;
- produkcioni centralni Data Hub;
- reprezentativni nacionalni dataset;
- pravno/tehnički odobren sistem centralnog prikupljanja osjetljivih podataka;
- validirani javni institucionalni ranking.

Svaka od tih sposobnosti zahtijeva zaseban razvoj, validaciju, governance i odgovarajuću pravnu/tehničku provjeru.