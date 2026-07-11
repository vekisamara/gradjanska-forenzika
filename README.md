# 🏛️ Građanska Forenzika (Civic Forensics)

Dobrodošli u zvanični repozitorijum sa otvorenim materijalima, strukturisanim AI promptovima i praktičnim alatima iz priručnika **„Vještačka inteligencija i birokratija – terenski priručnik za građansku forenziku“** autora Velimira Šamare.

Ovaj prostor obezbjeđuje tehničke i metodološke instrumente za primjenu **građanske forenzike** u svakodnevnom nadzoru rada javnih institucija, pretvarajući administrativnu netransparentnost u provjerljive činjenice.

🔗 **Glavni portal:** [gradjanskaforenzika.org](https://gradjanskaforenzika.org)

---

## 🌐 Future Roadmap: Civic Intelligence Dashboard (`civicforensics.org`)

**Status: Conceptual & Research Phase**

Razvijamo osnovu za **Civic Intelligence Dashboard** — AI-asistiranu platformu za praćenje javnih narativa, institucionalnih odluka i governance rizika kroz strukturisanu analizu podataka i Civic Forensics metodologiju.

### 📊 Platform objectives

- **Visual Accountability:** pretvaranje birokratskog teksta u mjerljive indikatore rizika.
- **Inconsistency Auditing:** mapiranje kontradikcija između javnih izjava institucija i stvarnih pravnih/administrativnih akata.
- **Democratic Resilience:** praćenje obrazaca netransparentnosti, formalizma i institucionalnog izbjegavanja odgovornosti.

🤝 **Call for Collaboration:** Tražimo strateške partnere, tehničke saradnike (AI/data/UI/UX) i finansijsku podršku za razvoj skalabilne infrastrukture demokratske odgovornosti za regionalne i EU slučajeve. Pogledajte [research-concepts/VISION.md](research-concepts/VISION.md).

---

## 🔍 Šta je Građanska forenzika?

Građanska forenzika je analitički metod provjere javnih odluka koji kombinuje kritičko čitanje administrativnih dokumenata, digitalne alate i važeći pravni okvir. Vještačka inteligencija se koristi kao **analitičko ogledalo** za prepoznavanje ponavljajućih birokratskih obrazaca, izbjegavanja odgovornosti i raskoraka između forme i suštine.

Pratimo stroge metodološke principe definisane u pratećim dokumentima:

- 🔬 [Metodologija Građanske Forenzike](metodologija_gradjanske_forenzike.md)
- ⚖️ [Standard Otvorene Javne Politike](standard_otvorene_javne_politike.md)

---

## 📂 Struktura repozitorijuma

- 🤖 [`promptovi/`](promptovi/README.md) — glavna prompt biblioteka za terenski rad: analiza akata i javnih izjava, brza provjera, pisanje žalbe, FOI zahtjevi i urgencije zbog ćutanja uprave.
- 🧭 [`promptovi/disciplinovani-administrativni-pritisak/`](promptovi/disciplinovani-administrativni-pritisak/README.md) — praktični primjeri koji prate stručni rad **„Metod disciplinovanog administrativnog pritiska“**: detektor formalizma, dokaz iza fraze, matrica neodgovorenih pitanja, FOI za dokumente, rokovnik, eskalacija i javna objava zasnovana na dokumentima.
- 🗣️ [`promptovi/izjave-funkcionera/`](promptovi/izjave-funkcionera/README.md) — edukativni AI set za višeslojnu analizu javnih izjava, saopštenja i obećanja: anatomija tvrdnje, dokazna podloga, logika, retorika, brojevi, odgovornost, prećutani kontekst, formalizam, dosljednost i građanska provjera.
- 🎛️ [`promptovi/dashboard/`](promptovi/dashboard/revizor_narativa.md) — rani AI prototipovi za analizu institucionalnih narativa, kontradikcija i spin obrazaca.
- 🛠️ [`alati/`](alati/README.md) — lokalni softverski alati za digitalni integritet, PDF metapodatke i buduću anonimizaciju podataka.
- 🌐 [`research-concepts/`](research-concepts/README.md) — strateški koncepti za Civic Intelligence Dashboard, MVP, partnerstva i data šeme.
- 📋 `sheme/` — planirani prostor za JSON data šeme za strukturisanje birokratskih anomalija, formalističkih obrazaca i indikatora javnog interesa.

---

## 🧭 Operativni tok rada

1. **Pribavi dokument** — akt, rješenje, zaključak, odgovor, zapisnik ili javnu izjavu.
2. **Anonimizuj osjetljive podatke** — ukloni JMBG, broj lične karte, privatne adrese, telefone i podatke koji nisu nužni za javni interes.
3. **Uradi brzu trijažu** — koristi `promptovi/02_brza_provjera.md`.
4. **Uradi dubinsku analizu** — koristi `promptovi/01_analiza_rjesenja.md`.
5. **Prepoznaj formalistički odgovor** — koristi `promptovi/disciplinovani-administrativni-pritisak/01_detektor_formalizma.md`.
6. **Pretvori frazu u dokazni trag** — koristi `promptovi/disciplinovani-administrativni-pritisak/02_dokaz_iza_fraze.md` i `promptovi/disciplinovani-administrativni-pritisak/03_matrica_neodgovorenih_pitanja.md`.
7. **Pribavi dodatne dokaze** — koristi `promptovi/04_foi_generator.md` ili praktični FOI primjer `promptovi/disciplinovani-administrativni-pritisak/04_foi_dokumenti_ne_misljenja.md`.
8. **Reaguj na ćutanje uprave** — koristi `promptovi/05_urgencija_cutanje_uprave.md` ili `promptovi/disciplinovani-administrativni-pritisak/08_rokovnik_i_urgencija.md`.
9. **Napiši pravni nacrt** — koristi `promptovi/03_pisanje_zalbe.md`.
10. **Eskaliraj uredno i dokumentovano** — koristi `promptovi/disciplinovani-administrativni-pritisak/09_plan_eskalacije.md`.
11. **Analiziraj javnu izjavu iz više uglova** — koristi kompletan set u `promptovi/izjave-funkcionera/`, od anatomije tvrdnje do građanskog testa provjerljivosti.
12. **Izvuci dashboard indikator** — koristi `promptovi/dashboard/revizor_narativa.md`.

---

## 💡 Istaknuti alat: Ekstraktor PDF metapodataka

Ako želite brzo testirati digitalni integritet dokumenta, skripta `alati/forenzika_pdf.py` izvlači skrivene sistemske podatke o autoru računara i softveru koji je kreirao dokument.

```text
==================================================
🔍 FORENZIČKI IZVJEŠTAJ METAPODATAKA DOKUMENTA
==================================================
📌 Autor (Korisnik računara): Milan_Privatni_PC
📌 Kreator (Aplikacija): Microsoft® Word 2019
📌 Kompanija: Privatna Pravna Radnja d.o.o.
==================================================
```

Ako se sistemski autor razlikuje od potpisnika dokumenta, to nije automatski dokaz nezakonitosti, ali jeste važan digitalni trag za dodatnu provjeru.

---

## 🔒 Privatnost i etika

Dokumenti koji sadrže osjetljive lične podatke ne smiju se javno objavljivati niti slati AI modelima bez prethodne anonimizacije. Fokus analize je zakonitost rada institucija, javni interes i provjerljivi administrativni tragovi, a ne privatni život pojedinaca.

---

## 🤝 Otvorena saradnja (Open Source Civics)

Ako želite prijaviti anomaliju sa terena, predložiti novi prompt ili podijeliti zanimljive metapodatke, otvorite **Issue** i koristite strukturisan opis: dokument, organ, datum, problem, dokazni trag i javni interes.

## 📜 Licenca

Svi materijali su licencirani pod uslovima međunarodne licence **Creative Commons Autorstvo-Nekomercijalno-Dijeliti pod istim uslovima 4.0 (CC BY-NC-SA 4.0)**. Detalje pogledajte u datoteci [LICENSE](LICENSE).