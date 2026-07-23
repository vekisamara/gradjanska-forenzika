# 🔬 Metodologija Građanske Forenzike 2.0

**Autor:** Velimir Samara  
**Verzija:** 2.0  
**Datum:** 23.07.2026.

Građanska forenzika je strukturisan metod analize odluka, akata, odgovora i javnih izjava institucija. Kombinuje pravnu analizu, provjeru činjenica, digitalne tragove i AI alate, ali zaključke uvijek vezuje za dokaz koji druga osoba može provjeriti.

Cilj nije samo prepoznati formalizam, nego sprovesti zatvoren i dokumentovan ciklus:

> **problem → uzroci → akteri → dokazi → analiza → intervencija → rezultat → učenje**

## Deset faza građanske forenzičke analize

### 1. Definisanje predmeta

Navesti: šta se dogodilo, koja odluka ili propuštanje je sporno, koja činjenica je odlučna, koja posljedica je nastala i šta bi bio provjerljiv rezultat analize.

### 2. Očuvanje izvornog materijala

Sačuvati originalni dokument, datum prijema ili objave, izvor, priloge, metapodatke, verzije i kontekst. Izvorni materijal se ne mijenja; anonimizovana radna kopija čuva se odvojeno.

### 3. Ekstrakcija tvrdnji i procesnih radnji

Izdvojiti i numerisati činjenične, pravne, brojčane i uzročne tvrdnje. Posebno evidentirati šta organ tvrdi da je uradio: uviđaj, pribavljanje dokaza, konsultaciju, prosljeđivanje, odlučivanje ili nadzor.

### 4. Razdvajanje simptoma, uzroka i posljedica

Za predmet navesti:

- vidljivi simptom;
- neposredne uzroke;
- sistemske uzroke;
- posljedice;
- najmanje jedno razumno alternativno objašnjenje.

Formalistička fraza je često simptom, dok stvarni uzrok može biti neizvršena procesna radnja, nejasna odgovornost ili odsustvo dokaznog traga.

### 5. Mapa aktera, nadležnosti i dokumenata

Za svakog aktera utvrditi formalnu nadležnost, stvarni uticaj, dokumente koje posjeduje, radnju koju može preduzeti i odnos prema drugim akterima. Razlikovati potpisnika, obrađivača predmeta, rukovodioca, donosioca odluke i nadzorni organ.

### 6. Dokazna matrica

Za svaku ključnu tvrdnju evidentirati:

| ID | Tvrdnja | Potreban dokaz | Dostupan dokaz | Nedostajući dokaz | Izvor | Status |
|---|---|---|---|---|---|---|
| T1 |  |  |  |  |  | potvrđeno / djelimično / nepotvrđeno / kontradiktorno / opovrgnuto |

Odsustvo dokaza nije automatski dokaz odsustva. Ono može potvrditi samo da dokaz nije dostavljen, pronađen ili evidentiran u dostupnom materijalu.

### 7. Test obrazloženja

Svaki akt ili odgovor provjerava se kroz lanac:

> **pitanje → utvrđena činjenica → dokaz → primijenjeno pravilo → obrazloženje → zaključak**

Analiza mora tačno označiti koja karika nedostaje. Opšta ocjena da je dokument „formalistički“ nije dovoljna bez pokazivanja konkretnog prekida u ovom lancu.

### 8. Nezavisna provjera i ponovljivost

Provjeriti da li druga osoba, koristeći isti materijal i isti protokol, može doći do uporedivog nalaza. Za važnije predmete koristiti drugi analitički prolaz ili kontrolni prompt koji pokušava osporiti, ograničiti ili precizirati prvi rezultat.

### 9. Akcioni plan

Svaku dokaznu prazninu povezati sa narednom radnjom:

| Praznina | Potrebna radnja | Adresat | Očekivani dokaz | Rok |
|---|---|---|---|---|

Radnja može biti FOI zahtjev, dopuna, uvid u spis, zahtjev za izlazak na teren, žalba, prijava, zahtjev za nadzor, javna analiza ili prijedlog sistemske izmjene.

### 10. Evaluacija i učenje

Nakon odgovora ili nove radnje označiti šta je potvrđeno, izmijenjeno, opovrgnuto i novo. Evidentirati koji dokaz je bio presudan, koje pitanje je proizvelo rezultat, šta nije djelovalo i šta treba izmijeniti u promptu, kontrolnoj listi ili standardu.

## Obavezni izlaz analize

Svaka potpuna analiza treba sadržavati:

1. predmet i ključno pitanje;
2. pouzdano utvrđene činjenice;
3. registar tvrdnji;
4. dokaznu matricu;
5. procesne radnje i propuste;
6. uočene obrasce formalizma;
7. uzroke, posljedice i alternativna objašnjenja;
8. nivo pouzdanosti;
9. sljedeće dokazne i procesne korake;
10. uputstvo za nezavisnu provjeru.

## Uloga vještačke inteligencije

AI je pomoćno analitičko ogledalo, ne konačni arbitar. Koristi se za ekstrakciju tvrdnji, poređenje dokumenata, prepoznavanje obrazaca, organizovanje dokaza i kontrolu dosljednosti. AI ne smije:

- izmišljati činjenice, izvore ili pravne odredbe;
- predstavljati pretpostavku kao činjenicu;
- zaključivati o unutrašnjoj namjeri osobe bez dokaza;
- izjednačiti odsustvo dokumenta sa dokazom da dokument ne postoji;
- dati konačnu pravnu kvalifikaciju bez odgovarajućeg izvora i stručne provjere.

## Verzije i trag izmjena

Svaki standard, metodologija i prompt mora sadržavati naziv, verziju, datum, autora, opis izmjena, poznata ograničenja i testne uzorke. Raniji rezultati se ne brišu nego ostaju povezani sa verzijom alata kojom su proizvedeni.

🔗 **Više informacija:** [gradjanskaforenzika.org](https://gradjanskaforenzika.org)