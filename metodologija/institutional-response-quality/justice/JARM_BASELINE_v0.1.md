# Justice Accountability Response Monitor — Baseline v0.1

**Oznaka:** CF-JARM 0.1  
**Status:** razvojni modul — u kalibraciji  
**Datum:** 9. septembar 2026.

## 1. Svrha

Justice Accountability Response Monitor (JARM) je domenska primjena CF-IRQF-a za analizu kvaliteta odgovora mehanizama institucionalne odgovornosti u pravosuđu.

JARM ne pita da li je sudska ili tužilačka odluka u meritumu pravilna. Njegovo centralno pitanje je:

> **Da li je accountability mehanizam individualizovano, relevantno i provjerljivo odgovorio na navod koji mu je upućen, uz dovoljno jasan trag između navoda, primijenjenog standarda, razloga i zaključka?**

## 2. Obavezni safeguard

> **response quality ≠ merits review ≠ legality determination ≠ misconduct finding**

JARM ne utvrđuje:

- pravilnost sudske ili tužilačke odluke;
- povredu zakona;
- postojanje disciplinskog prekršaja;
- korupciju ili motiv;
- namjerno izbjegavanje odgovornosti.

Takve kvalifikacije zahtijevaju zaseban pravni i dokazni osnov izvan JARM-a.

## 3. Položaj prema CF-IRQF, KAIT, MDAP i NIR

JARM nasljeđuje CF-IRQF dekompoziciju i zajedničke IRA/FCA signale. KAIT se koristi kada treba procijeniti da li ponuđeni razlog ili pravni princip nosi konkretni zaključak i njegov domet.

MDAP ostaje nadređen za dokazni status, rokove, zaštitu, procesni instrument i eskalaciju. NIR se uključuje samo ako stvarna interakcija prolazi routing gate; simulirana reakcija nije dokaz.

## 4. Jedinice JARM analize

- **A1…An — allegation:** materijalni navodi iz pritužbe/predstavke;
- **S1…Sn — standard:** pravilo, kriterijum ili granica nadležnosti na koju se odgovor poziva;
- **R1…Rn — reason:** individualizovani razlog zbog kojeg navod jeste ili nije relevantan;
- **E1…En — evidence engagement:** vidljiva veza sa dostavljenim dokazom ili činjenicom;
- **C1…Cn — conclusion:** zaključak accountability mehanizma.

Minimalno mapiranje:

> `A → S → R → E (kada je relevantno) → C`

Nedostajuća karika je signal za analizu, ne automatski dokaz pogrešne odluke.

## 5. JARM domenski signali

### J-01 — Merits Reframing

Procesni, conduct ili accountability navod tretiran je kao puko nezadovoljstvo meritumom odluke bez dovoljno vidljivog objašnjenja zašto je izvršena ta klasifikacija.

**Safeguard:** ako navod stvarno zahtijeva preispitivanje merituma izvan nadležnosti tijela, nema anomalije pod uslovom da je granica individualizovano objašnjena.

### J-02 — Allegation Bundling

Više sadržajno različitih materijalnih navoda dobija jedan zbirni razlog tako da iz odgovora nije moguće rekonstruisati kako je svaki važan navod klasifikovan.

### J-03 — Generic Independence / Discretion Substitution

Pozivanje na nezavisnost, diskreciju, slobodnu ocjenu ili sličan opšti princip zamjenjuje individualizovano objašnjenje njegove veze sa konkretnim accountability navodom.

**Veza sa KAIT:** kada postoji individualizovan razlog, ali je sporno da li nosi zaključak, koristiti KAIT umjesto automatske J-03 klasifikacije.

### J-04 — Allegation–Reason Mapping Gap

Za materijalni navod nije moguće rekonstruisati lanac:

`navod → relevantni standard → razlog → zaključak`.

Ovo je strukturni signal kvaliteta obrazloženja, ne merits finding.

### J-05 — Procedural Conduct / Merits Conflation

Navod o načinu postupanja, izvršenju dužnosti ili procesnom ponašanju i pitanje pravilnosti konačne odluke tretiraju se kao ista kategorija bez jasnog razgraničenja.

### J-06 — Evidence Engagement Gap

Materijalni dostavljeni dokaz ili konkretna dokazna tvrdnja nije vidljivo povezana sa odgovorom, iako bi mogla biti relevantna za klasifikaciju accountability navoda.

**Safeguard:** ne zahtijeva se da institucija odgovori na svaki prilog ili argument; mora se pokazati materijalnost.

### J-07 — Accountability Closure Gap

Predmet je formalno zatvoren, ali iz dostupnog odgovora nije moguće utvrditi kako su centralni accountability navodi riješeni ili zašto izlaze iz nadležnosti mehanizma.

J-07 se može koristiti zajedno sa FCA-01 kada su ispunjeni i opšti closure uslovi.

## 6. Razlikovanje tri analize

JARM mora razdvojiti:

1. **jurisdiction/competence finding** — šta mehanizam tvrdi da može ili ne može ispitivati;
2. **response-quality finding** — da li je taj odgovor individualizovan i provjerljiv;
3. **merits/legal finding** — pitanje koje JARM ne rješava.

Čak i potpuno jasan JARM nalaz ne daje odgovor na treću kategoriju.

## 7. Standardni izlaz

```text
Scope / vrsta accountability odgovora:
Materijalni navodi A1…An:
Mapiranje A→S→R→E→C:
Zajednički CF-IRQF signal(i):
JARM signal(i):
[EVIDENCE]:
[INFERENCE]:
[MISSING EVIDENCE]:
Alternativno objašnjenje:
Pouzdanost / materiality:
Šta se može tvrditi o kvalitetu odgovora:
Šta se ne može tvrditi o meritumu, zakonitosti ili misconductu:
Human-review status:
MDAP handoff, ako postoji procesna posljedica:
```

## 8. Stop-uslovi

JARM ne daje high-confidence negativni signal kada:

- nedostaje ključni dio pritužbe ili odgovora;
- nije moguće utvrditi koji su navodi stvarno bili pred institucijom;
- analiza zavisi od neprovjerenog pravnog standarda;
- zaključak bi zahtijevao preispitivanje merituma umjesto kvaliteta accountability odgovora;
- ozbiljan protivdokaz ili relevantni dio spisa nije dostupan.

Tada se koristi `MISSING EVIDENCE` ili `nije moguće ocijeniti`.

## 9. Poređenje i monitoring

JARM može agregirati odgovore samo uz unaprijed definisan uzorak, period, jedinicu analize i pravila kodiranja. Ne smiju se porediti tijela ili pojedinci prostim brojem signalnih kodova bez kontrole vrste predmeta i dostupnosti spisa.

Preporučeni agregatni izlazi u validaciji su distribucije po tipu signala, question/allegation coverage i udio nalaza `nije moguće ocijeniti`, a ne rang-liste misconducta.

## 10. Case-neutrality i validacija

Ovaj baseline ne sadrži podatke konkretnih disciplinskih, sudskih ili tužilačkih predmeta. Stvarni materijal korišten za internu kalibraciju i regresiono testiranje ne objavljuje se kroz ovaj paket.

JARM ostaje `U VALIDACIJI` dok ne prođe različite accountability-response testove, uključujući jasne negativne kontrole gdje je generički izgled odgovora ipak dovoljan, missing-evidence slučajeve i inter-analyst provjeru. Promocija zahtijeva uredničku odluku i ažuriranje centralnog statusnog registra.