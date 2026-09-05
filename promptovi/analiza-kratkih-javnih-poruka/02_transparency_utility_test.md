# GFO SMA — Transparency Utility Test (TUT)

**Oznaka:** GF-SMA-TUT 0.1  
**Status:** U VALIDACIJI  
**Datum:** 2026-09-06

## Svrha

TUT se aktivira kada institucija ili javno preduzeće predstavlja objavljivanje podataka kao dokaz transparentnosti, odgovornosti, zakonitosti, nekoruptivnosti ili pravilnog upravljanja javnim novcem.

TUT je odvojen od SMI. Istinita informacija može imati nizak SMI, a ipak biti loš ili formalistički instrument transparentnosti.

## Centralno pitanje

> Može li razuman građanin iz objavljene informacije stvarno rekonstruisati osnov, postupak i smisao javnog troška, ili mu je prikazan samo fragment koji stvara utisak transparentnosti?

## Dvije razine

### DISPLAY TRANSPARENCY

Da li je nešto tehnički prikazano, objavljeno ili javno vidljivo?

### AUDITABLE TRANSPARENCY

Da li je objava dovoljno trajna, čitljiva, povezana i potpuna da treća osoba može provjeriti zašto je trošak nastao, po kojem pravnom i ugovornom osnovu, da li je prošao odgovarajući postupak i da li odgovara budžetu?

Prva razina nije dokaz druge.

## TUT testovi

Svaka komponenta se ocjenjuje: PASS / PARTIAL / FAIL / UNKNOWN.

### 1. LEG — Legibility / čitljivost

- Da li je sadržaj moguće pročitati u realnim uslovima korištenja?
- Kod LED displeja: koliko dugo je podatak na ekranu, koliko teksta ima, sa koje udaljenosti se čita i da li je vrijeme prikaza dovoljno za razumijevanje?
- Tvrdnja da je sadržaj prebrz mora biti empirijski dokumentovana snimkom ili mjerenjem, ne pretpostavljena.

### 2. PER — Persistence / trajnost i naknadni pristup

- Može li građanin podatak ponovo otvoriti kasnije?
- Postoji li stabilna web arhiva, pretraga, datum i jedinstveni identifikator?

Dinamički ekran bez trajnog izvora može biti informativni prikaz, ali nije dovoljan audit trail.

### 3. SRC — Source linkage / veza sa izvornim dokumentom

Za račun/fakturu mora biti moguće, gdje je pravno i tehnički opravdano, povezati najmanje:

`račun/faktura → ugovor/narudžbenica → postupak nabavke ili drugi pravni osnov → budžetska pozicija/odobrenje → izvršenje/isporuka → plaćanje`

Objava samo računa ne dokazuje da su prethodni koraci postojali ili bili zakoniti.

### 4. CTX — Context sufficiency / dovoljnost konteksta

Da li građanin može razumjeti:

- šta je kupljeno ili plaćeno;
- zašto;
- kome;
- po kojem osnovu;
- u kojem periodu;
- da li je iznos dio većeg ugovora;
- da li postoje aneksi, izmjene ili povezana plaćanja?

### 5. COM — Completeness / potpunost relevantnog lanca

Ne traži se objava apsolutno svakog internog dokumenta. Traži se dovoljan skup javno dostupnih tragova da se ključna tvrdnja može provjeriti.

Parcijalna objava se ne smije predstavljati kao potpuna transparentnost ako ključne karike ostaju nedostupne.

### 6. REC — Reconstructability / mogućnost rekonstrukcije

Nezavisna osoba treba moći odgovoriti:

1. Koji događaj ili obaveza je proizvela trošak?
2. Ko je odobrio trošak?
3. Koji ugovor ili drugi pravni osnov ga pokriva?
4. Koja budžetska pozicija ga pokriva?
5. Koji postupak je prethodio izboru dobavljača, ako je primjenjivo?
6. Da li je isporuka/izvršenje evidentirano?
7. Kada i koliko je plaćeno?

Ako objava omogućava samo odgovor na posljednje pitanje, riječ je o slaboj rekonstruktivnoj transparentnosti.

### 7. INF — Inference discipline / disciplina zaključivanja

Posebno provjeri da li institucija iz činjenice:

`računi su objavljeni`

izvodi ili sugeriše širi zaključak:

`trošenje je zakonito / budžet je zakonit / nema korupcije / nema manipulacije / uprava je potpuno transparentna`.

Takav zaključak zahtijeva dodatne dokaze. Objavljivanje računa može povećati transparentnost, ali samo po sebi ne dokazuje zakonitost nabavke, ugovora, budžeta, izvršenja ili plaćanja.

### 8. CHN — Channel fitness / prikladnost kanala

Procijeni odgovara li kanal vrsti informacije.

- Billboard/LED je pogodan za kratko obavještenje ili upućivanje na izvor.
- Nije pogodan za gustu finansijsku dokumentaciju koja zahtijeva čitanje, poređenje i praćenje veza među dokumentima.

Ako se kompleksan finansijski podatak prikazuje u formatu koji ga čini praktično neprovjerljivim, označi `FORMAL_DISCLOSURE_RISK`.

## Posebni obrasci

- `DISPLAY_NOT_AUDITABILITY` — tehnička objava se predstavlja kao puna transparentnost.
- `PARTIAL_DISCLOSURE` — objavljen je samo fragment relevantnog dokaznog lanca.
- `TRANSPARENCY_OVERCLAIM` — iz ograničene objave izvodi se širi zaključak o transparentnosti ili zakonitosti.
- `FORMAL_DISCLOSURE_RISK` — forma objave postoji, ali je funkcionalna upotrebljivost slaba.
- `MISSING_SOURCE_LINKAGE` — račun/trošak nije povezan sa ugovorom, nabavkom, budžetom ili drugim relevantnim osnovom.
- `NON_RECONSTRUCTABLE_SPEND` — treća osoba ne može rekonstruisati tok odluke i novca.

## Zaštite

- Objavljivanje računa je pozitivan transparentni korak i ne smije se samo po sebi označiti kao manipulacija.
- Slaba čitljivost LED prikaza mora se dokazati konkretnim snimkom/mjerenjem ako je važna za nalaz.
- Nedostupan dokument nije dokaz da dokument ne postoji.
- Nedostatak ugovora u istom prikazu nije automatski nezakonitost; pitanje je da li je ugovor ili odgovarajući dokazni trag javno dostupan i povezan.
- TUT ne zaključuje o korupciji, zakonitosti budžeta ili zakonitosti nabavke bez zasebne provjere.

## Routing

Ako TUT pokaže PARTIAL ili FAIL na SRC/COM/REC, analiza se usmjerava prema:

`račun → ugovor → javna nabavka/drugi osnov → budžetska pozicija → izvršenje → plaćanje`

Za javne kampanje dodatno koristiti PMCT i Beneficiary Test.

## Standardni izlaz

1. Tvrdnja institucije o transparentnosti
2. Šta je stvarno objavljeno
3. Kanal objave
4. TUT matrica: LEG/PER/SRC/CTX/COM/REC/INF/CHN
5. Šta objava dokazuje
6. Šta objava ne dokazuje
7. Nedostajući dokazni linkovi
8. Rizik formalističke transparentnosti
9. Sljedeći dokazni korak
10. Nivo pouzdanosti
