# Sigurnost i odgovorno prijavljivanje

## Prijava problema

Sigurnosni problem, izloženi token, privatni dokument ili mogućnost neovlašćenog pristupa ne prijavljujte kroz javni issue. Koristite privatni kontakt naveden na gradjanskaforenzika.org i uključite samo najmanji potreban opis. Ne šaljite stvarne lične podatke kao dokaz ranjivosti.

## Obuhvat

Posebno su važni:

- izloženi API ključevi, tokeni ili konfiguracije;
- slučajno objavljeni spisi i lični podaci;
- zaobilaženje anonimizacije;
- pogrešno rukovanje lokalnim dokazima;
- izvršavanje nepouzdanog sadržaja ili putanja;
- izmjena evidencije bez traga integriteta.

## Postupanje s dokumentima

1. Original čuvati odvojeno i ograničiti pristup.
2. Napraviti radnu kopiju i anonimizovati je.
3. Provjeriti metapodatke i skrivene slojeve.
4. Ne slati osjetljive podatke vanjskom servisu bez zakonitog osnova i procjene rizika.
5. U repozitorij unositi samo javnu, provjerenu i očišćenu verziju.
6. Ako dođe do incidenta, sačuvati trag, ograničiti pristup i procijeniti obavezu obavještavanja.

Objavljivanje u git istoriji može ostati dostupno i nakon brisanja fajla. Zbog toga se incident sa tajnom ili ličnim podacima ne rješava samo novim commitom.