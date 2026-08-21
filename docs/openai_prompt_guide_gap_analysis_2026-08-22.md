# OpenAI Prompt Guide → GFO Prompt Library: gap analiza

**Datum:** 22. avgust 2026.  
**Status:** interna metodološka analiza  
**Referenca:** OpenAI Cookbook, *ChatGPT Enterprise: Practical prompt engineering for everyday work*

## Sažetak

Postojeća GFO Prompt Library je dokazno strožija od opšteg OpenAI vodiča: već ima zajedničko forenzičko jezgro, dokaznu matricu, razdvajanje činjenice od tvrdnje izvora i tumačenja, red-team prolaz, kontrolu pouzdanosti i pravilo da odsustvo dokaza nije dokaz odsustva.

Najveći jaz nije u dokaznoj disciplini nego u upravljanju promptovima kao kontrolisanim analitičkim instrumentima. OpenAI vodič eksplicitnije insistira na scoping-u, jednom primarnom rezultatu, acceptance criteria i malim evaluacionim setovima. Ove elemente treba centralizovati u GFO.

## ZADRŽATI

### 1. Zajedničko forenzičko jezgro

Zadržati obavezno nasljeđivanje zajedničkih pravila za sve promptove. Ovo je jače i sigurnije od ponavljanja zaštitnih instrukcija u svakom promptu.

### 2. Dokazna matrica i T-ID sistem

Zadržati T1…Tn, klasifikaciju ČINJENICA / TVRDNJA IZVORA / TUMAČENJE / PRETPOSTAVKA / NEPOZNATO i standardne statuse tvrdnji.

### 3. Lanac obrazloženja

Zadržati test:

> pitanje → činjenica → dokaz → pravilo → obrazloženje → zaključak

To je ključna GFO nadogradnja nad generičkim prompt engineering pravilima.

### 4. Red-team drugi prolaz

Zadržati nezavisni kontrolni prompt koji pokušava suziti ili osporiti prvi nalaz.

### 5. Kvantitativni modul

Zadržati poseban modul za brojke, poređenja, indikatore, kauzalnost i statističke tvrdnje umjesto opterećivanja svih promptova istim pravilima.

## IZMIJENITI

### 1. Jedan prompt — jedan primarni rezultat

Neki stariji GFO promptovi kombinuju ekstrakciju, pravnu analizu, formalizam, FOI strategiju, žalbu i rezime u jednom pozivu. To daje širok rezultat, ali povećava rizik plitke obrade pojedinih dijelova.

Pravilo: svaki prompt definiše jedan primarni rezultat; sekundarni izlazi ostaju samo ako direktno podržavaju taj rezultat.

### 2. Standardizovati strukturu

Umjesto različitih struktura po starijim promptovima, novi i revidirani promptovi treba da koriste:

> Context → Task → Evidence rules → Analytical tests → Output schema → Uncertainty → Self-check / Acceptance criteria

### 3. Persona kao funkcionalna uloga, ne retorički stav

Formulacije tipa „oštar analitičar“ ili „ne pretpostavljaj u korist organa“ treba koristiti oprezno. Bolje je zadati funkciju: nezavisni analitički alat koji aktivno traži protivdokaze, ali ne polazi od unaprijed zadatog zaključka.

### 4. Jasnije označiti neizvjesnost

Svaki ključni zaključak treba imati kvalitativni nivo pouzdanosti i odgovor na pitanje: „Šta bi moglo promijeniti ovaj zaključak?“

### 5. Razdvojiti prompt QA od case QA

Kontrola kvaliteta konkretnog nalaza i validacija samog prompta nisu ista stvar. Potrebna su dva odvojena procesa.

## DODATI

### 1. Acceptance criteria

Svaki složeni prompt mora imati eksplicitnu završnu provjeru tačnosti, potpunosti, dokazne discipline, kalibracije, formata i ljudske provjere.

### 2. Standardni šablon prompta

Dodati jedinstveni obrazac koji nove module prisiljava da definišu kontekst, jedan zadatak, dokazna pravila, testove, izlaz i kriterijume prihvatanja.

### 3. Prompt evaluation / benchmark

Za svaku novu ili materijalno izmijenjenu verziju složenog prompta koristiti najmanje 5 testova, preporučeno 8–10, uključujući pozitivne, negativne, granične i nepotpune slučajeve.

### 4. Kritične greške

Bez obzira na ukupnu ocjenu, prompt automatski pada ako izmisli izvor ili činjenicu, pogrešno predstavi nepotvrđenu tvrdnju kao činjenicu, zanemari odlučan protivdokaz ili iz odsustva dokumenta zaključi da dokument ne postoji.

### 5. Regresioni set

Svaka stvarna greška koja zahtijeva izmjenu prompta postaje trajni regresioni test. Time Prompt Library uči iz stvarnih predmeta bez pretvaranja pojedinačnih iskustava u neprovjereno pravilo.

### 6. Status prompta

Uvesti status: `STABILAN`, `U VALIDACIJI`, `POVUČEN`.

## IMPLEMENTIRANO 22.08.2026.

- dodat `metodologija/13_standard_kvaliteta_promptova.md` — GF-PROMPT-QS 1.0;
- dodat `metodologija/14_validacija_promptova.md` — GF-PROMPT-EVAL 1.0;
- dodat `promptovi/_sablon_prompta.md` — GF-PROMPT-TEMPLATE 1.0;
- `promptovi/00_forenzicko_jezgro.md` podignut na GF-PROMPT-CORE 1.2;
- `metodologija/07_ai_protokol_i_promptovi.md` podignut na GF-MET-AI 1.1;
- `metodologija/09_kontrola_kvaliteta_i_ponovljivost.md` podignut na GF-MET-QA 1.1.

## Sljedeća faza

Ne treba odmah mehanički prepisivati sve postojeće promptove. Prioritet je migracija po riziku:

1. pravni i upravni promptovi;
2. promptovi koji proizvode javne tvrdnje;
3. KAIT i GFO odlučivanje;
4. kvantitativni i PR-to-Payment moduli;
5. generativni promptovi za FOI, urgencije i podneske.

Svaki prompt se pri prvoj materijalnoj izmjeni prevodi na novi sedmobločni standard i testira prema GF-PROMPT-EVAL 1.0.
