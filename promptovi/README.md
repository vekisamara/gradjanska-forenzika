# Promptovi za građansku forenziku

Ovaj folder sadrži operativnu biblioteku promptova za analizu upravnih akata, brzu terensku trijažu, izradu nacrta žalbi i pripremu indikatora za budući Civic Intelligence Dashboard.

## Preporučeni redoslijed rada

1. `02_brza_provjera.md` — petominutna procjena da li dokument predstavlja stvarno odlučivanje ili birokratski ritual.
2. `01_analiza_rjesenja.md` — dubinska analiza zakonitosti, obrazloženja, javnog interesa, rokova i pravne ranjivosti akta.
3. `03_pisanje_zalbe.md` — generisanje smirenog i pravno upotrebljivog nacrta žalbe na osnovu prethodne analize.
4. `04_foi_generator.md` — izrada zahtjeva za pristup informacijama kada je potrebno pribaviti dokaze, pravni osnov, zapisnike ili interne akte.
5. `05_urgencija_cutanje_uprave.md` — izrada urgencije ili prigovora kada organ ne odgovori u zakonskom ili razumnom roku.
6. `disciplinovani-administrativni-pritisak/` — praktični primjeri koji prate stručni rad o metodu disciplinovanog administrativnog pritiska: detektor formalizma, dokaz iza fraze, matrica neodgovorenih pitanja, FOI za dokumente, rokovnik, eskalacija i javna objava zasnovana na dokumentima.
7. `dashboard/revizor_narativa.md` — poređenje javnog narativa institucije sa stvarnim administrativnim aktima i priprema indikatora za dashboard.
8. `analiza-izjava-iz-medija/` — detaljni i pojednostavljeni AI promptovi za provjeru javnih izjava, sa uputstvima za novinare, NVO sektor i građane.

## Pravilo provjerljivosti

Svaki rezultat dobijen pomoću ovih promptova mora biti vezan za konkretan dokaz: citat iz akta, broj predmeta, datum, potpisnika, rok, pravni osnov ili drugi provjerljiv administrativni trag. Zaključci bez dokaza ne smatraju se građanskom forenzikom.

## Privatnost i anonimizacija

Prije unošenja dokumenata u AI alat potrebno je ukloniti ili zamijeniti osjetljive lične podatke, naročito JMBG, broj lične karte, privatnu adresu, privatni telefon, medicinske podatke i podatke o maloljetnicima.

Fokus analize mora ostati na zakonitosti postupanja institucije, zaštiti javnog interesa i provjerljivim dokumentima, a ne na privatnom životu pojedinaca.

## Izlazni standard

Kada god je moguće, rezultat treba sadržavati:

- kratak zaključak običnim jezikom,
- tabelu nalaza,
- citatni trag,
- razdvajanje povreda postupka od materijalnopravnih problema,
- preporučeni naredni korak,
- procjenu rizika za javni interes.
