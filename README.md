# 🏛️ Građanska Forenzika (Civic Forensics)

Zvanični repozitorijum sa otvorenim metodološkim materijalima, strukturisanim AI promptovima i praktičnim alatima iz priručnika **„Vještačka inteligencija i birokratija – terenski priručnik za građansku forenziku“** autora Velimira Samare.

Građanska forenzika pretvara administrativnu netransparentnost, javne tvrdnje i institucionalne propuste u provjerljive činjenice, dokazne matrice i konkretne korake građanskog nadzora.

🔗 **Glavni portal:** [gradjanskaforenzika.org](https://gradjanskaforenzika.org)

## Metodološka osnova

- 🔬 [Metodologija Građanske Forenzike 2.0](metodologija_gradjanske_forenzike.md)
- ⚖️ [Standard Otvorene Javne Politike 2.0](standard_otvorene_javne_politike.md)
- 🧠 [Zajedničko forenzičko jezgro AI promptova](promptovi/00_forenzicko_jezgro.md)

Osnovni operativni ciklus je:

> **problem → uzroci → akteri → dokazi → analiza → intervencija → rezultat → učenje**

Analiza nije završena objavljivanjem nalaza. Novi odgovor ili dokument postaje novi dokazni unos, a prethodni zaključak se označava kao potvrđen, izmijenjen, opovrgnut ili dopunjen.

## Struktura repozitorijuma

- 🤖 [`promptovi/`](promptovi/README.md) — prompt biblioteka za analizu akata, javnih izjava, dokaznih praznina, žalbi, FOI zahtjeva i kontrole kvaliteta.
- 🧭 [`promptovi/disciplinovani-administrativni-pritisak/`](promptovi/disciplinovani-administrativni-pritisak/README.md) — alati za detekciju formalizma, dokaz iza fraze, neodgovorena pitanja, rokove i dokumentovanu eskalaciju.
- 🗣️ [`promptovi/izjave-funkcionera/`](promptovi/izjave-funkcionera/README.md) — višeslojna analiza javnih izjava, saopštenja i obećanja.
- 🎛️ [`promptovi/dashboard/`](promptovi/dashboard/revizor_narativa.md) — prototipovi za analizu institucionalnih narativa i kontradikcija.
- 🛠️ [`alati/`](alati/README.md) — lokalni alati za digitalni integritet, PDF metapodatke i anonimizaciju.
- 🌐 [`research-concepts/`](research-concepts/README.md) — strateški koncepti za Civic Intelligence Dashboard, MVP, partnerstva i data šeme.
- 📋 `sheme/` — prostor za strukturisanje tvrdnji, dokaza, formalističkih obrazaca i indikatora javnog interesa.

## Operativni tok rada

1. **Definiši predmet i centralno pitanje.**
2. **Sačuvaj izvorni materijal i napravi anonimizovanu radnu kopiju.**
3. **Uradi brzu trijažu** pomoću `promptovi/02_brza_provjera.md`.
4. **Napravi plan dokazivanja** pomoću `promptovi/06_plan_dokazivanja.md`.
5. **Mapiraj tvrdnje, aktere, nadležnosti i nedostajuće dokumente.**
6. **Uradi dubinsku analizu** pomoću `promptovi/01_analiza_rjesenja.md` ili odgovarajućeg specijalizovanog prompta.
7. **Provjeri lanac** pitanje → činjenica → dokaz → pravilo → obrazloženje → zaključak.
8. **Pribavi dodatne dokaze** kroz FOI, uvid u spis, terensku provjeru ili drugi odgovarajući postupak.
9. **Preduzmi dokumentovanu intervenciju**: dopuna, žalba, urgencija, prijava, zahtjev za nadzor ili javna analiza.
10. **Uradi nezavisnu kontrolu** pomoću `promptovi/07_kontrolna_analiza.md`.
11. **Evidentiraj rezultat** i označi šta je potvrđeno, izmijenjeno, opovrgnuto i novo.
12. **Ažuriraj bazu obrazaca, prompt ili metodologiju** kada predmet donese novo provjerljivo saznanje.

## Pravilo dokazivanja

Svaka važna tvrdnja mora biti povezana sa citatom, dokumentom, brojem predmeta, datumom, potpisnikom, zapisnikom, mjerenjem, metapodatkom ili drugim provjerljivim tragom. Odsustvo dokaza nije automatski dokaz odsustva.

## Privatnost i etika

Dokumenti sa osjetljivim ličnim podacima ne smiju se javno objavljivati niti slati komercijalnim AI modelima bez anonimizacije. Fokus je na institucionalnom postupanju, javnom interesu i dokazivim administrativnim tragovima, ne na privatnom životu pojedinaca.

## Civic Intelligence Dashboard

**Status: konceptualna i istraživačka faza.** Razvija se osnova za AI-asistiranu platformu koja strukturisane tvrdnje, dokaze, kontradikcije, rokove i institucionalne reakcije pretvara u mjerljive indikatore rizika i odgovornosti. Pogledajte [research-concepts/VISION.md](research-concepts/VISION.md).

## Otvorena saradnja

Za prijavu anomalije ili prijedlog novog prompta koristite strukturisan opis: dokument, organ, datum, centralno pitanje, tvrdnje, dokazni trag, nedostajući dokaz, javni interes i prethodno preduzete radnje.

## Licenca

Materijali su licencirani pod **Creative Commons Autorstvo-Nekomercijalno-Dijeliti pod istim uslovima 4.0 (CC BY-NC-SA 4.0)**. Detalji su u datoteci [LICENSE](LICENSE).