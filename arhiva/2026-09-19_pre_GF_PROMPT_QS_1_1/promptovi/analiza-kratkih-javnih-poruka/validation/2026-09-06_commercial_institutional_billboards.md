# GF-SMA validacija 02 — komercijalne i institucionalne billboard poruke

**Datum:** 2026-09-06  
**Status:** VALIDACIONI DATASET  
**Model:** GF-SMA 0.2 + GF-SMA-TUT 0.1

## Cilj

Provjeriti da li GF-SMA:

1. daje nizak SMI legitimnim komercijalnim i javno-korisnim porukama;
2. razlikuje emocionalnu mobilizaciju od manipulativnog zaključivanja;
3. ne proglašava javno oglašavanje problematičnim samo zato što koristi javni novac;
4. prepoznaje reputacijsko oglašavanje javnog monopoliste kao trigger za CNT/PMCT, a ne kao automatsku zloupotrebu;
5. razlikuje display transparency od auditabilne transparentnosti.

## Izvori uzorka

- BH Telecom — Moj webshop: https://www.bhtelecom.ba/usluge-za-privatne-korisnike/2021/02/kupujete-li-i-vi-putem-moj-webshop-bh-telecoma-moj-webshop-online-prodajno-mjesto-bh-telecoma/
- m:tel — najbolja mreža / Net Check: https://mtel.ba/Press-centar/a35132-m-tel-je-najbolja-mreza-u-BiH-i-u-2024.-godini.html
- Net Check benchmark: https://nc-group.net/en/mobile-network-test-bosnia-and-herzegovina-2024/
- m:tel — Ako me voliš, ostavi telefon dok voziš: https://mtel.ba/Press-centar/a28573-Ako-me-volis.-ostavi-telefon-dok-vozis.html
- m:tel — Ne gledaj ekran, gledaj put: https://mtel.ba/Press-centar/a38436-Ne-gledaj-ekran-gledaj-put.html
- TORS — I ovo je Srpska: https://lat.rtrs.tv/vijesti/vijest.php?id=564445
- EP BiH OOH nabavka: https://www.nabavke.com/javne-nabavke-tenderi-bih/usluga-ooh-kampanje-oglasavanja/javno-preduzece-elektroprivreda-bosne-i-hercegovine-dd-sarajevo/sarajevo/1713615
- EP HZHB — reklamiranje/promidžba: https://ephzhb.ba/reklamiranje-javni-poziv/
- TI BiH — Nije kasno za bolji život: https://ti-bih.org/zloupotrebom_javnih_sredstava_do_izbornih_poena/
- Banja Luka — računi/citylight: https://istinomjer.ba/predizborna-obecanja/transparentnost-gradske-uprave/
- Banja Luka — objavljeni računi: https://istinomjer.ba/objavljeni-racuni-gradske-uprave-banje-luke/

## Rezultati

### 1. BH Telecom — Moj webshop / sve na jednom mjestu

**Uloga:** COMMERCIAL / DESCRIPTIVE + PROMOTIONAL  
**SMI:** 2/40  
`[VER1 PRE0 EMO0 IDA0 CER0 BIN0 CAU0 OMI1]`

Nalaz: jasna prodajna svrha, realna tržišna konkurencija i konkretna usluga. Kratkoća poruke ne stvara materijalno pogrešan zaključak. CNT: opravdanje oglašavanja postoji.

### 2. m:tel — „Ponovo najbolji“ / najbolja mreža

**Uloga:** COMMERCIAL / COMPARATIVE CLAIM  
**SMI:** 7/40  
`[VER1 PRE1 EMO1 IDA0 CER1 BIN1 CAU0 OMI3]`

Nalaz: riječ „najbolji“ je materijalna komparativna tvrdnja, ali postoji eksterni benchmark Net Check sa rangiranjem i bodovima. OMI ostaje ograničen jer billboard tipično ne prikazuje metodologiju, ali se tvrdnja može eksterno provjeriti. Model mora nagraditi dostupnu dokaznu osnovu.

### 3. m:tel — „Ako me voliš, ostavi telefon dok voziš“

**Uloga:** CSR / ACTIVIST / IMPERATIVE  
**SMI:** 10/40  
`[VER1 PRE2 EMO4 IDA1 CER0 BIN1 CAU1 OMI0]`

Nalaz: izrazito emocionalna poruka koristi ljubav i bliskost kao motivator, ali cilj je javno-koristan i povezan sa dokumentovanim rizikom korištenja telefona u vožnji. Emocionalnost sama po sebi ne znači visok manipulativni potencijal.

### 4. m:tel — „Ne gledaj ekran, gledaj put!“

**Uloga:** CSR / IMPERATIVE  
**SMI:** 2/40  
`[VER0 PRE0 EMO2 IDA0 CER0 BIN0 CAU0 OMI0]`

Nalaz: direktna preventivna poruka sa minimalnim inferencijskim teretom. Dobar negativni kontrolni slučaj.

### 5. TORS — „I ovo je Srpska“

**Uloga:** INSTITUTIONAL + TOURISM PROMOTION / IDENTITY-AFFILIATION  
**SMI:** 5/40  
`[VER1 PRE0 EMO2 IDA2 CER0 BIN0 CAU0 OMI0]`

Nalaz: javni subjekt koristi identitetski okvir, ali kampanja ima jasnu svrhu — promociju turističkih lokacija i podsticanje posjeta. Na 22 billboarda prikazuju se konkretni turistički motivi. CNT/PMCT ne daju alarm samo zato što je naručilac javni subjekt.

### 6. JP Elektroprivreda BiH — OOH nabavka 2018.

**SMI:** N/A — INSUFFICIENT MESSAGE ARTIFACT

Poznato je da je nabavljana OOH kampanja za billboard/citylight/stajališta, ali bez konkretnog sadržaja poruke nije metodološki dozvoljeno izračunati SMI.

**Korekcija modela:** uveden je princip `MESSAGE ARTIFACT SUFFICIENCY`: nabavka oglašavanja ili opis kampanje može aktivirati CNT/PMCT, ali ne i SMI bez sadržaja poruke.

### 7. EP HZHB — cilj „stvaranje pozitivnog odnosa“ prema javnom preduzeću

**SMI:** N/A — nema konkretnog oglasa u izvoru.

**CNT/PMCT:** dodatna provjera opravdana. Javni poziv eksplicitno navodi da je cilj reklamiranja/promidžbe stvaranje pozitivnog odnosa prema javnom preduzeću kao pružaocu javne usluge električnom energijom.

Nalaz: reputacijska korist je dokumentovani cilj. To nije dokaz zloupotrebe, ali kod pružaoca javne usluge opravdava Beneficiary Test, provjeru tržišne potrebe, troška, kanala i mjerljivog javnog rezultata.

### 8. „Nije kasno za bolji život“ — energetska kampanja 2010.

**Uloga:** INSTITUTIONAL/POLITICAL proximity  
**SMI:** 13/40  
`[VER3 PRE2 EMO3 IDA0 CER2 BIN0 CAU2 OMI1]`

Nalaz: slogan sam po sebi ima umjeren SMI; glavni rizik ne proizlazi iz teksta nego iz konteksta javnog novca, promocije rezultata vlasti i blizine izbora. TI BiH je problematizovao kampanju i tražio podatke o nabavci i cijeni. Elektroprivreda BiH je navela da nije organizovala niti finansirala kampanju i uputila na resorno ministarstvo. Zato odgovornost za finansiranje ne smije biti pripisana EP BiH bez dodatnog dokaza.

Ovaj slučaj potvrđuje da SMI i PMCT moraju ostati odvojeni.

### 9. Grad Banja Luka — prikazivanje računa na citylight/LED panelima

**Uloga:** INSTITUTIONAL / TRANSPARENCY CLAIM

Grad je od februara 2021. objavljivao račune na web stranici i pojedinim reklamnim panelima. Gradonačelnik je to predstavljao kao „revoluciju u transparentnosti“ i tvrdio da javno objavljivanje sprečava mogućnost manipulacije. Predizborno obećanje je bilo šire: svaki račun, trošak i ugovor biće prikazani, što je povezano sa tvrdnjom da će time biti uklonjena mogućnost korupcije i kriminala.

**SMI za širu tvrdnju transparentnost → nema manipulacije/korupcije:** 20/40  
`[VER2 PRE3 EMO2 IDA1 CER3 BIN1 CAU4 OMI4]`

Ključni problem nije nužno istinitost pojedinačnog računa. Problem je inferencijski skok:

`objavljen račun → transparentno trošenje → nema mogućnosti manipulacije/korupcije`

Objavljeni račun pokazuje da je određena faktura evidentirana/plaćena. Sam po sebi ne dokazuje:

- da je ugovor zakonit;
- da je postupak nabavke zakonit;
- da je budžetska pozicija pravilno planirana i korištena;
- da je ugovorena roba/usluga stvarno izvršena u ugovorenom obimu;
- da nisu postojali aneksi ili povezana plaćanja;
- da je izbor dobavljača zakonit;
- da je cjelokupan budžet zakonit ili pravilno izvršen.

**TUT:**

- LEG: UNKNOWN/PARTIAL — tvrdnja da se sadržaj prebrzo smjenjuje mora biti dokumentovana mjerenjem/snimkom;
- PER: PASS/PARTIAL — web objava daje naknadni pristup, dok sam displej ne;
- SRC: PARTIAL/UNKNOWN — račun nije sam po sebi dokaz veze sa ugovorom, nabavkom i budžetskim osnovom;
- CTX: PARTIAL;
- COM: PARTIAL;
- REC: PARTIAL/FAIL ako se iz objave ne može rekonstruisati puni dokazni lanac;
- INF: FAIL za tvrdnju da sama objava računa uklanja mogućnost manipulacije;
- CHN: PARTIAL/FAIL za prikaz kompleksne finansijske dokumentacije na dinamičkom displeju ako je cilj stvarna provjera, a ne samo signaliziranje da podaci postoje.

**Pattern tags:** `DISPLAY_NOT_AUDITABILITY`, `TRANSPARENCY_OVERCLAIM`, `PARTIAL_DISCLOSURE`, potencijalno `FORMAL_DISCLOSURE_RISK`, `MISSING_SOURCE_LINKAGE`.

Važna zaštita: objavljivanje računa jeste pozitivan transparentni korak. Nalaz se odnosi na preširok zaključak koji se iz tog koraka izvodi i na eventualnu slabu auditabilnost, ne na tvrdnju da objava nema nikakvu vrijednost.

## Korekcije nakon validacije

### K1 — MESSAGE ARTIFACT SUFFICIENCY

SMI se ne smije računati ako nije dostupan konkretan tekst/slika poruke. Nabavka oglašavanja, iznos ili deklarisani cilj kampanje mogu aktivirati CNT/PMCT, ali ne zamjenjuju poruku.

### K2 — SUBSTANTIATED CLAIM CREDIT

Ako komercijalna komparativna tvrdnja ima jasno identifikovan eksterni dokaz (npr. benchmark), VER i OMI se smanjuju proporcionalno dostupnosti i relevantnosti dokaza. Billboard nije obavezan da sadrži cijelu metodologiju ako se tvrdnja može razumno provjeriti iz identifikovanog izvora.

### K3 — PUBLIC PURPOSE IS NOT A PENALTY

Javno finansirana kampanja sa jasnim mandatom i mjerljivom svrhom (npr. turistička promocija ili bezbjednost saobraćaja) ne dobija negativan tretman samo zbog javnog novca.

### K4 — DISPLAY TRANSPARENCY ≠ AUDITABLE TRANSPARENCY

Uveden GF-SMA-TUT 0.1. Tehnička objava podatka ne smije biti tretirana kao dokaz potpune transparentnosti ili zakonitosti. Za takav zaključak mora biti moguće rekonstruisati relevantni dokazni lanac.

### K5 — CHANNEL FITNESS

Kod LED/citylight formata analizira se da li je kanal prikladan složenosti informacije. Ako se gust finansijski sadržaj emituje u prolaznom formatu, potrebno je provjeriti trajanje prikaza, čitljivost i postojanje trajnog povezanog izvora.

## Zaključak validacije

GF-SMA je prošao drugi POC uz jednu važnu arhitektonsku dopunu: institucionalna komunikacija zahtijeva odvojeni TUT sloj. SMI dobro razlikuje legitimnu komercijalnu/promotivnu poruku od manipulativnog inferencijskog obrasca, ali nije dovoljan za procjenu kvaliteta javne transparentnosti.

Status modula ostaje **U VALIDACIJI**. Sljedeći prioritet je empirijski test 10+ aktuelnih institucionalnih/javnih kampanja sa dostupnim fotografijama i dokazima o trošku/nabavci.
