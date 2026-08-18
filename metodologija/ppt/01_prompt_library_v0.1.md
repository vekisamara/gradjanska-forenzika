# PPT Prompt Library v0.1

**Oznaka:** GF-PPT-PROMPT 0.1  
**Status:** operativni dodatak modulu GF-PPT 0.1 — kandidat u validaciji

## Univerzalni omotač

> Radi po GF-PPT 0.1, GF-PROMPT-CORE 1.1 i, kada postoje iznosi ili količine, GF-PROMPT-QUANT 1.0. Ne izmišljaj projekat, dokument, identifikator, izvođača, vrijednost, datum ni citat. Odvoji činjenicu, navod izvora, inferenciju, pretpostavku i nepoznato. Za svaki materijalni podatak navedi izvor, lokator, O/K/R/N, D1–D5 i pouzdanost. Isti izvođač, sličan opis ili okvirni sporazum nisu sami po sebi dokaz veze. Kada podaci ne daju odgovor napiši „nije utvrđeno“.

## Zajednička izlazna šema

```json
{
  "project_id": "",
  "trace_status": "VERIFIED_MATCH|PROBABLE_MATCH|PARTIAL_TRACE|UNTRACEABLE|CONTRADICTORY_TRACE",
  "trace_score": 0,
  "confidence": 0.0,
  "confirmed_facts": [],
  "source_claims": [],
  "inferences": [],
  "unknowns": [],
  "contradictions": [],
  "candidate_matches": [],
  "missing_documents": [],
  "next_actions": [],
  "review_status": "AI_DRAFT|HUMAN_REVIEWED|VALIDATED"
}
```

## PPT-01 — PR Project Extractor

**Zadatak:** Iz dostavljene PR ili medijske objave izdvoji datum, autora/organ, naslov, projekat, lokaciju, radove, količine, fazu, vrijednosti, izvođača, rok i izjave. Sačuvaj tačan citat ili vjeran sažetak i lokator. Ne dopunjavaj podatke iz opšteg znanja.

## PPT-02 — Financial Claim Classifier

**Zadatak:** Svaki iznos klasifikuj kao vrijednost konkretnog projekta, faze, zbirno teritorijalno ulaganje, plan, procjenu, ugovorenu vrijednost, plaćanje ili neodređeno. Obrazloži klasifikaciju i upozori ako bi iznos mogao biti pogrešno pripisan projektu.

## PPT-03 — Project Name and Location Normalizer

**Zadatak:** Napravi kontrolisanu listu naziva i sinonima projekta, putnih pravaca, naselja, ulica i administrativnih varijanti. Ne proglašavaj dvije lokacije istim bez dokaza. Izdvoji ključne termine za pretragu.

## PPT-04 — Procurement Candidate Finder

**Zadatak:** Za projektni profil rangiraj postupke nabavke prema lokaciji, predmetu, vremenu, vrijednosti, CPV-u i akterima. Vrati sve razumne kandidate, dokaze za i protiv, izvor/lokator i podatke koji nedostaju.

## PPT-05 — Candidate Match Scorer

**Zadatak:** Za svaki kandidat ocijeni podudarnost lokacije, predmeta, vremena, vrijednosti, količine, izvođača i identifikatora. Koristi skalu 0–2 po dimenziji: 0 nema veze/kontradikcija, 1 djelimično ili neodređeno, 2 neposredno potvrđeno. Ne izjednačavaj zbir bodova sa Verified Match bez direktne veze.

## PPT-06 — Framework Agreement Resolver

**Zadatak:** Utvrdi da li je kandidat okvirni sporazum. Traži pojedinačni ugovor, narudžbenicu, radni nalog, predmjer ili drugi zapis koji potvrđuje konkretnu lokaciju. Bez njega označi vezu kao nepotpunu.

## PPT-07 — Contract and Work-Order Extractor

**Zadatak:** Iz ugovora/naloga izdvoji broj, datum, strane, predmet, lokaciju, količine, vrijednost bez i sa PDV-om, rok, podizvođače, nadzor, izmjene i vezu sa nabavkom.

## PPT-08 — Payment Record Matcher

**Zadatak:** Poveži registar plaćanja sa ugovorom koristeći broj ugovora/nabavke, fakturu/situaciju, dobavljača, opis, datum i iznos. Navedi direktni identifikator ili razlog zašto je veza samo vjerovatna. Ne sabiraj nepovezana plaćanja istom dobavljaču.

## PPT-09 — Temporal Consistency Check

**Zadatak:** Sastavi vremensku liniju: PR tvrdnja, postupak, odluka, ugovor, uvođenje u posao, radovi, situacija, faktura i plaćanje. Označi radove prije ugovora, nelogične datume i periode koje registar još ne obuhvata. Ne izvodi pravnu kvalifikaciju bez odgovarajuće norme i dokaza.

## PPT-10 — Value and Quantity Reconciliation

**Zadatak:** Uporedi procijenjenu, ponuđenu, ugovorenu, aneksiranu, fakturisanu i plaćenu vrijednost te dužinu/površinu/količinu. Prikaži osnovicu, PDV, valutu i formulu. Zbirno ulaganje u područje drži odvojeno.

## PPT-11 — Contradiction Detector

**Zadatak:** Izdvoji samo materijalne nesaglasnosti o lokaciji, radovima, izvođaču, vrijednosti, količini, roku ili fazi. Razlikuj kontradikciju od razlike u obuhvatu, datumu ili poreskoj osnovici.

## PPT-12 — Evidence Strength Assessor

**Zadatak:** Svakoj vezi dodijeli O/K/R/N, D1–D5 i pouzdanost. Objasni šta izvor dokazuje, a šta ne. Fotografija table može potvrditi sadržaj table, ali sama ne potvrđuje plaćanje.

## PPT-13 — Traceability Score

**Zadatak:** Izračunaj indeks 0–100 tačno prema GF-PPT tabeli. Za svaki dodijeljeni bod navedi dokaz. Zasebno odredi status veze. Ne tumači nizak rezultat kao dokaz nepravilnosti.

## PPT-14 — Missing Document Detector

**Zadatak:** Za svaku otvorenu vezu navedi minimalni dokument koji bi je potvrdio ili opovrgao, vjerovatnog imaoca, precizan opis zapisa i prioritet A/B/C.

## PPT-15 — FOI Request Generator

**Zadatak:** Od praznina prioriteta A sastavi zahtjev za postojeće dokumente i evidencije. Traži postupak, odluku, okvirni i pojedinačni ugovor, nalog, predmjer, nadzor, situacije, fakture i plaćanja uz projekat, lokaciju i period. Ne traži od organa da izrađuje novu analizu.

## PPT-16 — Human Review Report

**Zadatak:** Proizvedi neutralan završni izvještaj: potvrđene činjenice, javne tvrdnje, lanac, status, indeks, kontradikcije, nepoznato, alternativna podudaranja, nedostajući dokumenti i sljedeći korak. Dodaj datum pregleda i review status.

## Orkestracija

1. PPT-01 do PPT-03 nad PR izvorom.
2. PPT-04 nad dostupnim nabavkama.
3. PPT-05 i PPT-06 nad kandidatima.
4. PPT-07 nad ugovorom/nalogom.
5. PPT-08 nad registrom plaćanja.
6. PPT-09 do PPT-12 nad cijelim korpusom.
7. PPT-13 i PPT-14 za ocjenu i praznine.
8. PPT-15 kada lanac nije zatvoren.
9. PPT-16 tek nakon drugog analitičkog prolaza.

Aktiviraj STOP i ne dodjeljuj Verified Match ako nema direktne veze ugovora/naloga i plaćanja, ako ključni nalaz zavisi od neprovjerenog R/N izvora ili ako postoje nerazriješene materijalne kontradikcije.
