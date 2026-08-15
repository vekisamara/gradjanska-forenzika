# Etika, privatnost i odgovorna upotreba AI-a

1. Prikupiti najmanju količinu podataka potrebnu za definisan javni interes.
2. Izvorne dokumente odvojiti od anonimizovanih radnih kopija.
3. Ne unositi osjetljive podatke u vanjski AI servis bez zakonitog osnova i procjene rizika.
4. Evidentirati model, datum, svrhu i ljudske korekcije.
5. AI izlaz tretirati kao radni prijedlog, nikada kao dokaz.
6. Provjeriti citate, brojeve, pravne tvrdnje i zaključke u primarnim izvorima.
7. Omogućiti ispravku i pravo na odgovor prije štetne javne atribucije kada je to bezbjedno i razumno.
8. Ne automatizovati rangiranje ljudi, optuživanje ni odluke sa pravnim ili reputacionim posljedicama.

Podaci o maloljetnicima, zdravlju, biometriji, privatnim adresama, dokumentima i ranjivim grupama zahtijevaju strožu procjenu nužnosti. Detaljni postupak je u [`AI protokolu`](../metodologija/07_ai_protokol_i_promptovi.md).


## Operativna klasifikacija podataka

| Klasa | Primjeri | Pravilo |
|---|---|---|
| Javno | objavljeni akti i javna saopštenja | provjeriti autentičnost i prava trećih lica |
| Interno | radne bilješke i nacrti | ograničiti pristup i ne objavljivati bez pregleda |
| Povjerljivo | neobjavljeni spisi i identifikacioni podaci | lokalna obrada, kontrolisan pristup i evidencija prenosa |
| Posebno osjetljivo | zdravlje, biometrija, maloljetnici i ugrožene osobe | obrađivati samo kada je nužno, zakonito i uz pojačane mjere |

## Životni ciklus

Za svaki skup podataka odrediti svrhu, pravni osnov, minimalni obim, mjesto čuvanja, pristup, rok zadržavanja i način sigurnog brisanja. Vanjski servis smije se koristiti tek nakon provjere ugovornih uslova, lokacije obrade, zadržavanja podataka i mogućnosti treniranja na sadržaju.

## Incidenti

Kod pogrešnog objavljivanja ili pristupa: zaustaviti dalje širenje, sačuvati dokazni trag, ograničiti pristup, procijeniti pogođene osobe i zakonske obaveze, dokumentovati korekciju i spriječiti ponavljanje. Sigurnosni kanal opisan je u [SECURITY.md](../SECURITY.md).
