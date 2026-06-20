# 🏛️ Građanska Forenzika (Civic Forensics)

Dobrodošli u zvanični repozitorijum sa otvorenim materijalima, strukturisanim AI promptovima i praktičnim alatima iz priručnika **„Vještačka inteligencija i birokratija – terenski priručnik za građansku forenziku“** autora Velimira Šamare.

Ovaj prostor obezbjeđuje tehničke i metodološke instrumente za primjenu **građanske forenzike** u svakodnevnom nadzoru rada javnih institucija, pretvarajući administrativnu netransparentnost u provjerljive činjenice.

🔗 **Glavni portal:** [gradjanskaforenzika.org](https://gradjanskaforenzika.org)

---

## 🌐 Future Roadmap: Civic Intelligence Dashboard (`civicforensics.org`)

**Status: Conceptual & Research Phase**

We are actively developing the foundation for the **Civic Intelligence Dashboard** — an AI-assisted platform designed to monitor public narratives, institutional decisions, and governance risks through structured data analysis and Civic Forensics methodology.

### 📊 Platform Objectives:
* **Visual Accountability:** Transforming bureaucratic text into quantifiable governance risk scores.
* **Inconsistency Auditing:** Automatically mapping contradictions between public institutional narratives and actual legal/administrative outputs.
* **Democratic Resilience:** Tracking patterns of misinformation and institutional opacity across regional ecosystems.

🤝 **Call for Collaboration:** We are actively seeking **strategic partners, technical collaborators (AI/data engineers), and funding support** to co-develop scalable democratic accountability infrastructure for EU and regional use cases. Review our full roadmap in the [VISION.md](VISION.md) file.

---

## 🔍 Šta je Građanska forenzika?

Građanska forenzika je analitički metod provjere javnih odluka koji kombinuje kritičko čitanje administrativnih dokumenata, upotrebu digitalnih alata i pozivanje na važeći pravni okvir. Vještačka inteligencija (AI) se koristi kao **analitičko ogledalo** za prepoznavanje ponavljajućih birokratskih obrazaca i bježanja od odgovornosti.

Pratimo stroge metodološke principe definisane u pratećim dokumentima:
* 🔬 [Metodologija Građanske Forenzike](metodologija_gradjanske_forenzike.md)
* ⚖️ [Standard Otvorene Javne Politike (Open Policy Standard)](standard_otvorene_javne_politike.md)

---

## 📂 Struktura repozitorijuma

Ovaj repozitorijum je organizovan na sljedeći način:

* 🤖 `promptovi/` — Gotovi "prompt skeletoni" za terenski rad (duboka analiza akata, brza trijaža, pisanje žalbi).
* 🎛️ `promptovi/dashboard/` — Rani AI prototipovi za analizu institucionalnih narativa i spin obrazaca.
* 🛠️ `alati/` — Lokalni softverski alati za bezbjednu [lokalnu anonimizaciju podataka](alati/README.md) i [ekstrakciju skrivenih PDF metapodataka](alati/README.md#upravljanje-pdf-metapodacima).
* 📋 `sheme/` — JSON Data šeme za strukturisanje i normalizaciju birokratskih anomalija na budućem dashboardu.

---

## 💡 Istaknuti alat: Ekstraktor PDF Metapodataka

Ako želite brzo testirati digitalni integritet dokumenta, naša skripta `forenzika_pdf.py` izvlači skrivene sistemske podatke o autoru računara i softveru koji je kreirao rješenje:

```text
==================================================
🔍 FORENZIČKI IZVJEŠTAJ METAPODATAKA DOKUMENTA
==================================================
📌 Autor (Korisnik računara): Milan_Privatni_PC
📌 Kreator (Aplikacija): Microsoft® Word 2019
📌 Kompanija: Privatna Pravna Radnja d.o.o.
==================================================
```
*Ako se sistemski autor razlikuje od potpisnika dokumenta, to je jasan digitalni trag učešća treće strane u donošenju javnih odluka.*

---

## 🤝 Otvorena saradnja (Open Source Civics)

Ako želite prijaviti anomaliju sa terena, predložiti novi prompt ili podijeliti zanimljive metapodatke, kliknite na opciju **Issues** i pokrenite naš strukturisani obrazac za prijavu.

## 📜 Licenca

Svi materijali su licencirani pod uslovima međunarodne licence **Creative Commons Autorstvo-Nekomercijalno-Dijeliti pod istim uslovima 4.0 (CC BY-NC-SA 4.0)**. Detalje pogledajte u datoteci [LICENSE](LICENSE).
