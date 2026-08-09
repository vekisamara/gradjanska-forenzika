# KAIT v0.1 — validacioni izvještaj ATA-1

**Oznaka:** GFO-KAIT-VAL-ATA1-001  
**Status:** `CONDITIONAL PASS`  
**Granica:** regresioni test strukture tvrdnji, ne konačna pravna kvalifikacija predmeta

## Izvršni rezultat

KAIT je prošao prvi funkcionalni test na devet claim klastera. Modul je dosljedno odvojio autentičnost i dokaznu težinu dokumenta od pitanja da li dokument opravdava sigurnost i domet institucionalnog zaključka. Najjači doprinos pokazao je kod tvrdnji „sva dokumentacija postoji“, „svi uslovi su ispunjeni“ i kod izvođenja uzročnosti iz vremenskog slijeda.

| Rezultat | Broj | Tumačenje |
|---|---:|---|
| Usklađeno | 1 | Opravdanje nosi užu tvrdnju u definisanom obuhvatu. |
| Djelimično usklađeno | 3 | Dokaz podržava dio zaključka ili uži domet. |
| Neusklađeno | 2 | Zaključak je širi ili procesno drugačiji od dokaza. |
| Nije moguće ocijeniti | 3 | Nedostaje pravni, tehnički ili procesni dokument. |

Ovi brojevi nisu skor institucije, stopa zakonitosti niti dokaz sistemskog obrasca.

## Korpus i ograničenja

Test koristi ATA-1 gold hronologiju, registar SRC-001 do SRC-015, Decision Graph v0.2, rezultate GFO-01 do GFO-14 i tekst rješenja 05-370-4373/25. Kompletan spis Republičkog inspektorata i pisani odgovor Vodovoda nisu bili dostupni. Test nije uključio slijepog drugog analitičara.

## Ključni nalazi

- Postojanje potrebnih dokumenata nije isto što i dokaz da su svi materijalni i procesni uslovi ispunjeni.
- D1 službeni akt dokazuje šta je organ tvrdio, ali ne automatski i istinitost ili dovoljnost tvrdnje.
- Pozitivan izvještaj Komisije podržava samo pitanja unutar dokumentovanog obuhvata Komisije.
- Odlaganje i kasniji lokacijski uslovi potvrđuju sukcesiju, ne uzročnost ili motiv.
- Novi godišnji predmet ne briše analitički kontinuitet istog fizičkog objekta i ponovljenih odlučnih pitanja.
- Naknadno priznato svojstvo stranke ne dokazuje djelotvorno učešće prije odluke.
- Rizik za kanalizacionu infrastrukturu ostaje neocjenjiv bez pisanog tehničkog dokaza.

## Rezultat kontrola

| Kontrola | Rezultat | Napomena |
|---|---|---|
| Odvajanje D nivoa i adekvatnosti | PASS | Nijedan status nije izveden automatski iz D1–D5. |
| Očuvanje O/K/R/N | PASS | R/N pitanja ostala su privremena ili neocjenjiva. |
| Sigurnost i domet | PASS uz kalibraciju | Potrebni primjeri za više analitičara. |
| Alternativno objašnjenje | PASS | Negativni ili neocjenjivi high-impact nalazi imaju neutralan test. |
| Causality lock | STRONG PASS | Vremenski slijed nije pretvoren u uzročnost. |
| Motive lock | PASS | Nema nedokazanih tvrdnji o namjeri ili koordinaciji. |
| Komparativna sinteza | PASS | Izvori su grupisani po tvrdnjama. |
| Inter-analyst reproducibility | NOT TESTED | Potreban slijepi drugi analitičar. |

## Metodološke korekcije

1. Zadržati vrstu tvrdnje `mixed`.
2. Domet razložiti najmanje na predmet, period i lokaciju.
3. Kod izraza „sva dokumentacija“ odvojiti postojanje, autentičnost, sadržajnu potpunost i pravnu dovoljnost.
4. Upozoriti kada warrant samo ponavlja istu tvrdnju.
5. Operativnu funkciju dokumenta zadržati kao pomoćnu hipotezu.
6. `misaligned` ne prevoditi automatski u `unlawful`.
7. Za pravne tvrdnje tražiti važeću normu i datum provjere prije statusa `confirmed`.
8. KAIT-10 mora uključiti drugi analitički prolaz i disagreement log.

## Odluka o integraciji

- Standard 3.2 se ne mijenja; prijedlog ostaje kandidat za 3.3.
- KAIT v0.1 ulazi kao radni podmodul GFO-05 i pomoćni sloj GFO-03/04/08/10/12.
- KAIT-00 do KAIT-09 mogu se koristiti odmah; KAIT-10 samo uz gold set.
- CDE MVP treba dobiti Claim/Warrant/Premise objekte i validacione lockove.
- ATA-1 claim matrix služi za regresiju, ne kao konačna analiza cijelog predmeta.

## Naredna validacija

Potrebni su kompletan inspekcijski spis, pisani odgovor Vodovoda, datum prijema presude i dokaz njenog tretmana u novom predmetu; zatim slijepi test drugog analitičara, test javne nabavke sa kvantitativnim tvrdnjama i test kratkog institucionalnog odgovora sa malo dokaza. Tek potom odlučuje se o Standardu 3.3 i kalibraciji AC-K07.

Strukturisani gold set: [`kait_claim_matrix_v0.1.json`](kait_claim_matrix_v0.1.json).

