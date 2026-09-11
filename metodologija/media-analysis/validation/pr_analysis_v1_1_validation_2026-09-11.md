# GFO MEDIA — PR Analysis v1.1 validation

**Datum:** 11. septembar 2026.
**Predmet:** regresiona validacija canonical institucionalnog PR prompta v1.1
**Prethodna verzija:** v1.0
**Protokol:** GF-PROMPT-EVAL 1.0
**Odluka:** STABILAN / CURRENT
**Kritične greške:** 0

## 1. Obuhvat izmjene

V1.1 ne mijenja postojeću skalu 0–3, nivoe institucionalnog prikrivanja 0–6, routing ni Source 16 metrike. Dodaje:

- forenzički komunikacijski lanac;
- razdvajanje `CLAIMED / SUPPORTED / OMITTED / IMPLIED`;
- kontinuum `PUBLIC INFORMATION / INSTITUTIONAL PR / PERSONAL-POLITICAL PROMOTION`;
- kvalitativni `PR–Outcome Gap (POG)` bez novog numeričkog scorea;
- kvalitativni `Public Information Utility (PIU)`;
- test superlativa i mjerljivog benchmarka;
- uslovnu provjeru tajminga, ponavljanja i distribucije;
- eksplicitnu razliku između komunikacijskog outputa, dokazivog outcomea i dugoročnog učinka.

Teorijska osnova provjerena je u Dennis L. Wilcox, Glen T. Cameron i Bryan H. Reber, *Public Relations: Strategies & Tactics*, 11. izdanje: RACE proces; izbor i oblikovanje poruke; source credibility; timing/context; razlika između komunikacijskih outputa i outcomes; te ograničenja pretjeranog/promotivnog jezika. Knjiga je korištena kao konceptualni izvor, ne kao dokaz za pojedinačne institucionalne slučajeve.

## 2. A/B hipoteza

V1.0 pouzdano prepoznaje dokazne praznine, zamjenu aktivnosti rezultatom, transparentnost, personalizaciju i krizni PR. V1.1 treba da doda novu vrijednost samo ako:

1. rekonstruiše kako poruka proizvodi utisak, a ne samo da li je tvrdnja provjerljiva;
2. razlikuje visoku informativnu vrijednost od visokog promotivnog intenziteta;
3. razlikuje komunikacijski doseg od stvarnog ishoda;
4. ne duplira Source 16 scoring;
5. ne izvodi namjeru iz tajminga, ponavljanja, superlativa ili medijskog prenosa.

## 3. Evaluacioni set i unaprijed određene granice

| ID | Javni PR predmet | Tip testa | Minimalni očekivani nalaz | Zabranjeni zaključak |
|---|---|---|---|---|
| PR11-01 | Tunjice 1 i 2 — puštanje vodovodnog sistema u rad | pozitivan rezultat + prenaglašen dugoročni učinak | fizički rezultat postoji; „trajno riješeno“ zahtijeva vremenski niz i tehničke pokazatelje | sistem ne radi ili je tvrdnja namjerno lažna |
| PR11-02 | Školske uniforme — spor Grada i direktora | kontradiktoran/politički okvir | događaj i političko tumačenje moraju biti razdvojeni; nedostaju zapisnik, ovlaštenja i druga institucionalna perspektiva | politička opstrukcija je dokazana |
| PR11-03 | Manjača — promotivna turistička vožnja | nedostajući ključni dokazi | promotivni događaj nije dokaz turističkog razvoja; trošak, plan i indikatori ostaju otvoreni | turistički efekat ne postoji |
| PR11-04 | „Besplatni placevi“ — pravo građenja | zavodljiva pravna/semantička kompresija | naziv mjere implicira vlasnički prenos širi od prava građenja; pravni dokument mora imati prednost | mjera je nezakonita ili bezvrijedna |
| PR11-05 | Javni poziv za prevoz nakon najave „najveće reforme“ | granični/proceduralni slučaj | javni poziv jeste novi proceduralni trag, ali ne dokazuje puni reformski model | reforma ne postoji ili je poziv dokaz kompletne realizacije |

## 4. Sažeti rezultat v1.1

| ID | Dominantna funkcija | POG | PIU | Nova vrijednost u odnosu na v1.0 | Granica očuvana |
|---|---|---|---|---|---|
| PR11-01 | institucionalno informisanje + promocija rezultata | srednji | srednja | odvaja izgrađen/pušten sistem od nedokazanog trajnog učinka i označava „trajno“ kao benchmark tvrdnju | da |
| PR11-02 | institucionalni PR + personalno/političko uokviravanje | visok za prikaz institucionalne prepreke kao dokazane političke opstrukcije; N/P za fizičku realizaciju | niska | razdvaja događaj, eksplicitnu političku tvrdnju i implikaciju da su interes djece i partijska lojalnost jedina dva objašnjenja | da |
| PR11-03 | institucionalna/turistička promocija | visok za razvojni učinak, nizak za činjenicu da je tura održana | niska do srednja | pokazuje da međunarodni učesnici, slike i najava ponavljanja povećavaju output, ali ne dokazuju outcome | da |
| PR11-04 | javno informisanje + političko-promotivna kompresija | srednji do visok za „riješeno stambeno pitanje“; nizak za postojanje konkursa | srednja | CLAIMED/IMPLIED razdvaja pravo građenja bez naknade od razumnog utiska da građanin dobija plac u vlasništvo | da |
| PR11-05 | javno informisanje o proceduri + reformski PR kontekst | srednji | srednja do visoka za rok/kontakt; niska za model reforme | PIU razlikuje praktično korisne podatke javnog poziva od nedostajućeg ugovornog i finansijskog modela | da |

## 5. A/B nalaz

| Provjera | v1.0 | v1.1 | Odluka |
|---|---|---|---|
| Događaj nasuprot poruci | prisutno kroz neutralnu rekonstrukciju | eksplicitno i sljedivo kroz komunikacijski lanac | zadržati v1.1 |
| Eksplicitna tvrdnja nasuprot implikaciji | djelimično | jasno razdvojeno uz lokator i uncertainty guardrail | zadržati v1.1 |
| Output nasuprot outcomeu | aktivnost/rezultat je dobro pokriven | dodata distribucija i dugoročni učinak bez miješanja sa realizacijom | zadržati v1.1 |
| Informativna vrijednost | 12 pitanja javne vrijednosti | dodat sažeti PIU koji ne mjeri popularnost | zadržati v1.1 |
| Superlativi/hype | pokriveni kroz prenaglašavanje | uveden obavezni benchmark | zadržati v1.1 |
| Tajming i ponavljanje | rasuto kroz kontekst/hronologiju | uslovni, dokazno ograničen test | zadržati v1.1 |
| Složenost izlaza | visok rizik dužine već u v1.0 | inicijalni kandidat dodatno širio kratki izlaz | korigovano: najviše 8 materijalnih redova; N/P i nepoznato se izostavljaju kada nisu odlučni |
| Rizik nagađanja o publici | nije posebno formalizovan | inicijalni IMPLIED mogao preći dokaznu granicu | korigovano: obavezan lokator; nesigurna implikacija se označava ili izostavlja |
| Dvostruko bodovanje | postoji opšte pravilo | POG je mogao ponoviti postojeće indikatore | korigovano: POG ostaje opisni sažetak i ne povećava druge ocjene |

## 6. Ocjenjivanje prema GF-PROMPT-EVAL 1.0

Skala: `2 = prolaz`, `1 = djelimično`, `0 = pad`.

| ID | Tačnost | Potpunost | Dokazna disciplina | Kalibracija | Format | Akcionabilnost | Ukupno |
|---|---:|---:|---:|---:|---:|---:|---:|
| PR11-01 | 2 | 2 | 2 | 2 | 2 | 2 | 12/12 |
| PR11-02 | 2 | 2 | 2 | 2 | 2 | 2 | 12/12 |
| PR11-03 | 2 | 2 | 2 | 2 | 1 | 2 | 11/12 |
| PR11-04 | 2 | 2 | 2 | 2 | 2 | 2 | 12/12 |
| PR11-05 | 2 | 2 | 2 | 2 | 2 | 2 | 12/12 |

**Prosjek:** 1,97/2.
**Testovi bez nule u tačnosti ili dokaznoj disciplini:** 5/5 (100%).
**Kritične greške:** 0.
**Ponavljajući nekorigovani tip greške:** 0.

Ocjena formata 1 u PR11-03 odnosi se na rizik da kratka promotivna objava proizvede predug izlaz. Korekcija proporcionalnosti ugrađena je u završnu verziju, ali se rezultat testa ne povećava retroaktivno.

## 7. Regresiona i arhitektonska provjera

- postojeća skala 0–3 ostala je neizmijenjena;
- nivoi institucionalnog prikrivanja 0–6 ostali su neizmijenjeni;
- POG i PIU nisu paralelni numerički scoring sistemi;
- Source 16 ORS/FDS/SID/PDS/APD/SVD nije prepisan niti izmijenjen;
- `broj_objava` nije izjednačen sa nezavisnim dokaznim lancima;
- tajming nije korišten kao dokaz namjere;
- hype riječ nije korištena kao dokaz neistinitosti;
- nedostajući dokument nije pretvoren u tvrdnju da dokument ne postoji;
- politička, obmanjujuća, koruptivna ili prikrivajuća namjera nije pripisana bez neposrednih dokaza;
- v1.0 jezgro za akutni rizik, krizni PR, korekciju, štetu, dokazni status i institucionalno prikrivanje ostalo je očuvano.

## 8. Zaključak

**PASS — GFO MEDIA PR Analysis v1.1 može dobiti status CURRENT — STABILAN.**

V1.1 daje materijalno bolju rekonstrukciju komunikacijskog mehanizma bez promjene postojećeg canonical scoringa. Validacija podržava zaključak da novi POG, PIU, CLAIMED/SUPPORTED/OMITTED/IMPLIED i output/outcome testovi dodaju forenzičku vrijednost na heterogenom skupu javnih PR objava. Potrebna je buduća inter-analyst provjera i širi benchmark za naučnu ili reprezentativnu validaciju; trenutna odluka znači operativnu stabilnost unutar GFO metodologije, ne eksternu certifikaciju.

## 9. Trajni regresioni zahtjevi

Naredne verzije moraju ponoviti najmanje PR11-01, PR11-04 i PR11-05 jer zajedno testiraju:

- stvarni rezultat nasuprot dugoročnom učinku;
- semantičku/pravnu kompresiju;
- prelazak iz najave u proceduru bez lažnog proglašavanja konačne realizacije.
