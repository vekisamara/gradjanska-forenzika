# KAIT v0.1 — Kritička analiza institucionalne tvrdnje

**Oznaka:** GFO-KAIT-MET-001  
**Verzija:** 0.1  
**Status:** radni podmodul; `CONDITIONAL PASS` na predmetu ATA-1  
**Položaj:** primarno unutar GFO-05, uz podršku GFO-03/04/08/10/12

## 1. Svrha

KAIT odgovara na pitanje: **da li dokumentovano opravdanje nosi tačno onaj zaključak koji institucija iznosi?** Modul se primjenjuje poslije ekstrakcije činjenica i izvora, a prije konačnog forenzičkog nalaza. Ne mijenja statuse O/K/R/N, nivoe D1–D5, hronologiju ni Decision Graph.

Autentičan službeni dokument može pouzdano dokazati da je organ nešto tvrdio. To samo po sebi ne dokazuje da su sadržaj, sigurnost i domet te tvrdnje opravdani.

## 2. Jedinice analize

| Objekat | Definicija |
|---|---|
| Claim | Materijalno relevantna institucionalna tvrdnja. |
| Warrant | Dokaz, norma ili razlog ponuđen kao opravdanje. |
| Premise | Izrečena ili implicitna pretpostavka potrebna za zaključak. |
| Counterevidence | Materijal koji osporava ili sužava tvrdnju. |
| Scope | Granice vremena, prostora, predmeta i populacije. |
| Adequacy finding | Ocjena veze opravdanje–zaključak, odvojena od kvaliteta izvora. |

## 3. Režimi rada

| Režim | Kada se koristi | Obavezni sadržaj |
|---|---|---|
| Osnovni | Svaki relevantan dokument | tvrdnja, opravdanje, sigurnost, domet, praznina, adekvatnost |
| Dubinski | Odlučne tvrdnje, kontradikcije, javna objava ili high-impact nalaz | sva KAIT polja, protivdokaz, premise, alternativa i Linkage Tracker |

## 4. Radni tok

| ID | Korak | Rezultat |
|---|---|---|
| KAIT-00 | Forenzičko pitanje | Jedno provjerljivo pitanje i granice analize. |
| KAIT-01 | Ekstrakcija tvrdnji | Citat/parafraza, govornik, lokator i vrsta. |
| KAIT-02 | Rekonstrukcija opravdanja | Dokazi, norme, činjenice, premise i zaključak. |
| KAIT-03 | Sigurnost i domet | Kategoričnost i tačan obuhvat tvrdnje. |
| KAIT-04 | Pojmovi i pretpostavke | Definicije, promjene značenja i nužne premise. |
| KAIT-05 | Protivdokazi | Materijal koji osporava ili ograničava tvrdnju. |
| KAIT-06 | Alternativno objašnjenje | Neutralna alternativa i diskriminirajući dokaz. |
| KAIT-07 | Ocjena adekvatnosti | Jedan od četiri dozvoljena statusa. |
| KAIT-08 | Komparativna sinteza | Izvori grupisani po pitanju, ne po dokumentu. |
| KAIT-09 | Linkage Tracker | Trag od nalaza do pitanja, tvrdnje i izvora. |
| KAIT-10 | Samokritički izlaz | Zaključak, ograničenja i ono što se ne može tvrditi. |

## 5. Statusi adekvatnosti

| Status | Pravilo |
|---|---|
| Usklađeno | Opravdanje podržava sadržaj, sigurnost i domet tvrdnje. |
| Djelimično usklađeno | Podržan je uži, uslovni ili samo jedan dio zaključka. |
| Neusklađeno | Tvrdnja je sigurnija, šira ili drugačija od onoga što dokaz opravdava. |
| Nije moguće ocijeniti | Nedostaje ključni dokaz, norma, lokator ili potpun spis. |

Status `neusklađeno` nije automatski isto što i `nezakonito`.

## 6. Obavezna dokazna disciplina

- D1–D5 ocjenjuje težinu izvora, ne valjanost zaključka.
- O/K/R/N opisuje dostupnost i citabilnost izvora; R/N može otvoriti pitanje, ali ne može sam zatvoriti high-impact nalaz.
- Više dokumenata koji ponavljaju istu tvrdnju nisu nužno nezavisna potvrda.
- Vremenski slijed nije dovoljan za uzročnost ili motiv.
- Za svaki negativan high-impact nalaz navodi se neutralna alternativa i dokaz koji bi razlikovao tumačenja.
- Analiza se organizuje po materijalnim pitanjima, ne kao niz sažetaka dokumenata.

## 7. Minimalna matrica

| Polje | Minimalni sadržaj |
|---|---|
| ID i tvrdnja | Citat ili vjerna parafraza, autor i lokator. |
| Vrsta | factual, legal, causal, procedural, normative, predictive ili mixed. |
| Opravdanje | Dokazi, norme i razlozi na koje se tvrdnja oslanja. |
| Sigurnost i domet | Stepen kategoričnosti te predmet, period i lokacija. |
| Premise i protivdokazi | Nužne pretpostavke i materijal koji ih osporava. |
| Alternativa | Neutralno objašnjenje i test razdvajanja. |
| Adekvatnost | Status i obrazloženje veze opravdanje–zaključak. |
| Nedostatak | Dokument ili provjera potrebna za potvrdu ili opovrgavanje. |

## 8. Stop-uslovi

- nema izvornog dokumenta ili pouzdanog lokatora za ključnu tvrdnju;
- zaključak zavisi od nepotvrđenog R/N izvora;
- nije utvrđena relevantna verzija pravne norme;
- nije moguće razlikovati sadržaj dokumenta od interpretacije analitičara;
- postoji ozbiljan protivdokaz koji nije dostupan u cjelini.

## 9. Granice

KAIT ocjenjuje strukturu i dokaznu adekvatnost argumenta. Ne utvrđuje samostalno zakonitost ili motive, ne zamjenjuje sudsku ili stručnu procjenu i ne pretvara retoričku slabost u dokaz nepravilnosti.

## 10. Povezani resursi

- [Kandidat dopune Standarda 3.3](kait/standard_v3.3_kandidat.md)
- [KAIT prompt paket](../promptovi/kait/README.md)
- [CDE KAIT specifikacija](../research-concepts/kait_cde_specifikacija_v0.1.md)
- [ATA-1 validacija](../studije-slucaja/ata-1/kait_validacija_v0.1.md)

