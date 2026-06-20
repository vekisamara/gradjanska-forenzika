# 🏛️ Vještačka inteligencija i birokratija — Terenski priručnik za građansku forenziku

Dobrodošli u zvanični repozitorijum sa otvorenim materijalima, strukturisanim AI promptovima i praktičnim primjerima iz priručnika **„Vještačka inteligencija i birokratija – terenski priručnik za građansku forenziku“** (izdanje 2026.), autora Velimira Šamare.

Ovaj prostor je kreiran s ciljem da građanima, aktivistima, novinarima i organizacijama civilnog društva obezbijedi gotove tehničke i metodološke alate za primjenu **građanske forenzike** u svakodnevnom nadzoru rada javnih institucija.

🔗 **Glavni portal projekta:** [gradjanskaforenzika.org](https://gradjanskaforenzika.org)
📖 **Radionički materijali i podrška:** [restartsrpska.org](https://restartsrpska.org)

---

## 🔍 Šta je Građanska forenzika?

Građanska forenzika je analitički metod provjere javnih odluka koji kombinuje kritičko čitanje administrativnih dokumenata, upotrebu digitalnih alata i pozivanje na važeći pravni okvir. Cilj nije polemička rasprava sa institucijama, već pretvaranje javnih tvrdnji u provjerljive činjenice kroz zakonite procedure pristupa informacijama i mehanizme institucionalne kontrole.

U savremenom okruženju administrativnog formalizma, vještačka inteligencija (AI) se u okviru ove metodologije koristi kao **analitičko ogledalo** i pomoćni instrument za prepoznavanje ponavljajućih birokratskih obrazaca, a ne kao konačni autoritet.

---

## 📂 Struktura repozitorijuma

Ovaj repozitorijum vjerno prati cjeline priručnika i organizovan je na sljedeći način:

* 📑 `01_uvod_i_metodologija/` — Osnovni pojmovi o AI pismenosti kao građanskoj vještini i vizuelni algoritam građanske forenzike.
* 🤖 `02_osnovni_prompt_paket/` — Gotovi, strukturisani "prompt skeletoni" (System, Context, Task, Style, Input) za terenski rad.
* ⚖️ `03_pandorina_kutija/` — Studije slučaja zasnovane na stvarnim upravnim aktima (analiza rješenja, povrede postupka i administrativni formalizam).
* 🛠️ `04_prakticni_vodic/` — Kontrolne liste, algoritmi poslušnosti u modernoj birokratiji i uputstva za postupanje pred Ombudsmanom i sudovima.

---

## 💡 Gotovi Prompt Skeletoni iz Priručnika

U nastavku su navedeni direktni, optimizovani promptovi koje možete kopirati i odmah iskoristiti u modelima kao što su ChatGPT, Claude ili Copilot.

### 1. Automatski AI prompt za analizu upravnog rješenja (Primjer br. 1)
Ovaj prompt služi da testira zakonitost, svrhu i istinitost rješenja organa, bez pretpostavki u njegovu korist.

```text
Uloga:
Ti si AI analitičar upravnog prava, javnog interesa i institucionalne odgovornosti. Nemaš zadatak da braniš organ, nego da testiraš zakonitost, svrhu i istinitost rješenja.

Ulaz:
U nastavku se nalazi tekst upravnog rješenja / odgovora organa.

Zadatak:
Izvrši strukturiranu analizu koristeći sljedeće korake:
1. IDENTIFIKACIJA ODLUKE (Organ, odgovorna osoba, zahvaćena prava građana)
2. ANALIZA JEZIKA (Pasivne konstrukcije i bezlične formulacije poput "utvrđeno je", "smatra se")
3. PROCEDURA vs. SVRHA (Da li se rješenje bavi svrhom zakona ili samo formom)
4. ČINJENICE (Utvrđene činjenice naspram ignorisanih ili prećutanih okolnosti)
5. ODGOVORNOST (Da li se pozivanje na nadležnost koristi za izbjegavanje odlučivanja)
6. JAVNI INTERES (Osnov za primjenu testa javnog interesa)
7. ROKOVI I ĆUTANJE (Zloupotreba rokova i institucionalno ćutanje)
8. DOGMATSKI INDIKATORI (Primjena AI-checkliste birokratske dogme)
9. PRAVNA RANJIVOST (Identifikacija tačaka ranjivih za žalbu / tužbu)
10. REZIME ZA GRAĐANE (Objašnjenje od maksimalno 10 rečenica, običnim jezikom)

Izlaz:
Strukturiran izvještaj sa jasnim naslovima, citatima iz teksta i konkretnim zaključcima. Bez uljepšavanja.

Tekst za analizu:
[ZALIJEPI TEKST UPRAVNOG RJEŠENJA]
```

### 2. Skraćena petominutna analiza (Primjer br. 2)
Brza provjera da li je upravni akt stvarno odlučivanje ili ritualna birokratska dogma.

```text
Uloga:
Ti si AI koji provjerava da li je upravno rješenje stvarno odlučivanje ili birokratska dogma prerušena u proceduru.

Zadatak:
Odgovori KRATKO i PRECIZNO na sljedeće tačke:
1. ODLUKA – Ko odlučuje i da li je odgovorna osoba imenovana (DA/NE)?
2. SUŠTINA – Da li se o pravu građanina stvarno odlučuje (DA/NE)?
3. JEZIK – Navedi 2-3 primjera bezličnog ili pasivnog jezika iz teksta.
4. PROCEDURA vs. SVRHA – SVRHA / FORMA?
5. ČINJENICE – Koje ključne činjenice su ignorisane ili prećutane?
6. JAVNI INTERES – DA / NE / FORMALNO?
7. CRVENI SIGNALI – Korišćenje fraza "nije nadležno", "rok je istekao", "u skladu sa propisima".
8. DOGMA TEST – Broj indikatora birokratske dogme (0–2 / 3–6 / 7+).
9. PRESUDA – Jedna rečenica: Da li je ovo odlučivanje ili ritual?

Tekst za analizu:
[ZALIJEPI TEKST UPRAVNOG RJEŠENJA]
```

---

## 🔒 Zaštita ličnih podataka (Važna napomena!)

U skladu sa preporukama iz Poglavlja 1.4 priručnika, prilikom korišćenja ovih promptova na komercijalnim AI platformama:
1. **Uklonite osjetljive podatke:** Prije unosa dokumenata obavezno uklonite JMBG, tačnu adresu stanovanja i brojevi ličnih dokumenata.
2. **Koristite oznaku `(anonimizovano)`:** Zamjena ličnih podataka ne mijenja pravni ili činjenični smisao dokumenta, a štiti privatnost lica.
3. **Fokusirajte se na postupanje organa:** AI analiza testira zakonitost i proceduru javnih akata, za šta identitet pojedinca nije neophodan.

---

## 🤝 Otvorena saradnja (Open Source Civics)

Ovaj projekat je potpuno otvoren! Pozivamo vas da date svoj doprinos ukoliko ste:
* **Građanski aktivista ili novinar** koji je testirao ove prompte na novim studijama slučaja.
* **Pravnik** koji želi da dopuni strukturu promptova za specifične upravne oblasti.
* **AI entuzijasta** koji želi pomoći u automatizaciji anonimizacije dokumenata za građansku forenziku.

Slobodno otvorite **Pull Request** sa novim prompt šablonima ili pokrenite diskusiju u sekciji **Issues**.

---

## 📜 Licenca i Citiranje

Tekstualni materijali, promptovi i primjeri u ovom repozitorijumu dostupni su besplatno pod međunarodnom licencom **Creative Commons Autorstvo-Nekomercijalno 4.0 (CC BY-NC 4.0)**.

**Preporučeni akademski format citiranja priručnika:**
> Šamara, V. (2026). *Vještačka inteligencija i birokratija: Terenski priručnik za građansku forenziku*. Digitalno otvoreno izdanje.
