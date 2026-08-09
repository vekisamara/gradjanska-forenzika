# 🏛️ Građanska Forenzika (Civic Forensics)

Zvanični repozitorijum sa otvorenim metodološkim materijalima, strukturisanim AI promptovima i praktičnim alatima iz priručnika **„Vještačka inteligencija i birokratija – terenski priručnik za građansku forenziku“** autora Velimira Samare.

Građanska forenzika pretvara administrativnu netransparentnost, javne tvrdnje i institucionalne propuste u provjerljive činjenice, dokazne matrice i konkretne korake građanskog nadzora.

🔗 **Glavni portal:** [gradjanskaforenzika.org](https://gradjanskaforenzika.org)

## Metodološka osnova

- 🧰 [Operativni standardi Građanske forenzike 1.0](metodologija/README.md)
- ⚖️ [Standard za analizu javnih odluka i institucionalnog postupanja 3.2](standard_otvorene_javne_politike.md)
- 🧭 [Metod disciplinovanog administrativnog pritiska 3.2](metod_disciplinovanog_administrativnog_pritiska.md)
- 🔬 [Metodologija Građanske Forenzike 2.0](metodologija_gradjanske_forenzike.md)
- 🔎 [KAIT v0.1 — kritička analiza institucionalne tvrdnje](metodologija/12_kait_kriticka_analiza_institucionalne_tvrdnje.md)
- 🧠 [Zajedničko forenzičko jezgro AI promptova](promptovi/00_forenzicko_jezgro.md)
- 📊 [Univerzalni modul za kvantitativne tvrdnje](promptovi/08_kvantitativni_modul.md)
- 📈 [Forenzička analiza izvještaja o radu](promptovi/09_analiza_izvjestaja_o_radu.md)

Osnovni operativni ciklus je:

> **problem → uzroci → akteri → dokazi → analiza → intervencija → rezultat → učenje**

Analiza nije završena objavljivanjem nalaza. Novi odgovor ili dokument postaje novi dokazni unos, a prethodni zaključak se označava kao potvrđen, izmijenjen, opovrgnut ili dopunjen.

## Struktura repozitorijuma

- 🧰 [`metodologija/`](metodologija/README.md) — operativni standardi dokazivanja, označavanja, analize odgovora i PR-a, FOI zahtjeva, rokova, eskalacije, AI kontrole i verzionisanja.
- 🤖 [`promptovi/`](promptovi/README.md) — prompt biblioteka za analizu akata, javnih izjava, dokaznih praznina, žalbi, FOI zahtjeva, kvantitativnih tvrdnji i kontrole kvaliteta.
- 🧭 [`promptovi/disciplinovani-administrativni-pritisak/`](promptovi/disciplinovani-administrativni-pritisak/README.md) — alati za detekciju formalizma, dokaz iza fraze, neodgovorena pitanja, rokove i dokumentovanu eskalaciju.
- 🔎 [`promptovi/kait/`](promptovi/kait/README.md) — KAIT promptovi za rekonstrukciju tvrdnji, protivdokaze, domet i adekvatnost zaključka.
- 🗣️ [`promptovi/izjave-funkcionera/`](promptovi/izjave-funkcionera/README.md) — višeslojna analiza javnih izjava, saopštenja i obećanja.
- 🎛️ [`promptovi/dashboard/`](promptovi/dashboard/revizor_narativa.md) — prototipovi za analizu institucionalnih narativa i kontradikcija.
- 🛠️ [`alati/`](alati/README.md) — lokalni alati za digitalni integritet, PDF metapodatke i anonimizaciju.
- 🌐 [`research-concepts/`](research-concepts/README.md) — strateški koncepti za Civic Intelligence Dashboard, MVP, partnerstva i data šeme.
- 📋 `sheme/` — prostor za strukturisanje tvrdnji, dokaza, formalističkih obrazaca i indikatora javnog interesa.

## Kvantitativna građanska forenzika

Standard 3.2 uvodi provjeru brojčanih, komparativnih, prediktivnih i uzročnih tvrdnji. Analiza razlikuje stvarnu pojavu od korištenog pokazatelja, provjerava brojilac i imenilac, izvor i obuhvat, odgovarajuće poređenje, pristrasnost, šum, uzročnost i praktični ili pravni značaj.

Posebno se uvodi pojam **kvantitativni formalizam**: korištenje brojeva, procenata, statistike, rangiranja, grafikona ili AI rezultata radi stvaranja privida objektivnosti, iako podatak ne dokazuje stvarni javni rezultat.

Metod 3.2 dodaje Protokol jednog podatkovnog pitanja, kvantitativni dokazni trag i procesne okidače za procenat bez imenioca, aktivnost predstavljenu kao ishod i promjenu metodologije.

## Operativni tok rada

1. **Definiši predmet i centralno pitanje.**
2. **Sačuvaj izvorni materijal i napravi anonimizovanu radnu kopiju.**
3. **Uradi brzu trijažu** pomoću `promptovi/02_brza_provjera.md`.
4. **Napravi plan dokazivanja** pomoću `promptovi/06_plan_dokazivanja.md`.
5. **Mapiraj tvrdnje, aktere, nadležnosti i nedostajuće dokumente.**
6. **Aktiviraj kvantitativni modul** ako materijal sadrži broj, procenat, trend, indikator, poređenje ili uzročnu tvrdnju.
7. **Uradi dubinsku analizu** pomoću `promptovi/01_analiza_rjesenja.md` ili odgovarajućeg specijalizovanog prompta.
8. **Za izvještaje o radu koristi** `promptovi/09_analiza_izvjestaja_o_radu.md`.
9. **Provjeri lanac** pitanje → činjenica → dokaz → pravilo → obrazloženje → zaključak.
10. **Pribavi dodatne dokaze** kroz FOI, uvid u spis, terensku provjeru ili drugi odgovarajući postupak.
11. **Preduzmi dokumentovanu intervenciju**: dopuna, žalba, urgencija, prijava, zahtjev za nadzor ili javna analiza.
12. **Uradi nezavisnu kontrolu** pomoću `promptovi/07_kontrolna_analiza.md`.
13. **Evidentiraj rezultat** i označi šta je potvrđeno, izmijenjeno, opovrgnuto i novo.
14. **Ažuriraj bazu obrazaca, prompt ili metodologiju** kada predmet donese novo provjerljivo saznanje.

## Pravilo dokazivanja

Svaka važna tvrdnja mora biti povezana sa citatom, dokumentom, brojem predmeta, datumom, potpisnikom, zapisnikom, mjerenjem, metapodatkom ili drugim provjerljivim tragom. Odsustvo dokaza nije automatski dokaz odsustva.

Precizan broj nije automatski dokaz tačnosti zaključka. Mora se provjeriti šta je mjereno, ko je izostavljen, u odnosu na šta je rezultat prikazan i da li broj opisuje aktivnost ili stvarno ostvarenje javne misije.

## Privatnost i etika

Dokumenti sa osjetljivim ličnim podacima ne smiju se javno objavljivati niti slati komercijalnim AI modelima bez anonimizacije. Fokus je na institucionalnom postupanju, javnom interesu i dokazivim administrativnim tragovima, ne na privatnom životu pojedinaca.

## Civic Intelligence Dashboard

**Status: konceptualna i istraživačka faza.** Razvija se osnova za AI-asistiranu platformu koja strukturisane tvrdnje, dokaze, kontradikcije, rokove, kvantitativne pokazatelje i institucionalne reakcije pretvara u mjerljive indikatore rizika i odgovornosti. Pogledajte [research-concepts/VISION.md](research-concepts/VISION.md).

## Otvorena saradnja

Za prijavu anomalije ili prijedlog novog prompta koristite strukturisan opis: dokument, organ, datum, centralno pitanje, tvrdnje, dokazni trag, nedostajući dokaz, javni interes i prethodno preduzete radnje.

## Licenca

Materijali su licencirani pod **Creative Commons Autorstvo-Nekomercijalno-Dijeliti pod istim uslovima 4.0 (CC BY-NC-SA 4.0)**. Detalji su u datoteci [LICENSE](LICENSE).
