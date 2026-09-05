# GFO MEDIA — P/A/D Layer Prompt v0.3

**Status:** EXPERIMENTAL  
**Methodology:** `metodologija/media-analysis/18_populist_personalization_authoritarian_dogma_layer_v0_3.md`

## Canonical operational prompt

Analiziraj dostavljeni sadržaj koristeći **GFO MEDIA — Populist Personalization, Authoritarian Narrative & Political Dogma Layer v0.3**.

Ovaj prompt je pomoćni eksperimentalni prompt. Ne zamjenjuje niti mijenja canonical GFO MEDIA promptove 10–13 i njihove scoring sisteme.

Ne klasifikuj političara, stranku, instituciju ili medij kao populističke ili autoritarne. Analiziraj isključivo strukturu konkretnog sadržaja i dokumentovani longitudinalni obrazac kada je dostupan.

Prvo rekonstruiši **stvarni institucionalni i uzročni lanac** iz dostupnih dokaza. Zatim odvojeno rekonstruiši **narativni lanac** koji sadržaj predstavlja publici.

Ocijeni odvojeno:

- P1–P9 **Populist Personalization**;
- A1–A8 **Authoritarian Narrative**;
- D1–D6 **Political Dogma / Epistemic Authority**.

Za svaki indikator navedi:

- intenzitet 0–4;
- konkretan dokaz;
- evidence confidence: HIGH / MEDIUM / LOW.

Posebno testiraj:

- Political Credit Capture;
- Origin Displacement;
- Citizen Agency Appropriation;
- Institutional Complexity Suppression;
- Obstacle Construction;
- Moral Monopoly;
- Institutional Delegitimization;
- Threat Amplification;
- Leader-as-Protector;
- Leader Indispensability;
- Position Reversal without Error Recognition;
- Evidence Subordination;
- Retrospective Consistency Reconstruction.

Za svaki prelazak `EVENT → INTERPRETATION → ATTRIBUTED CAUSE → POLITICAL CONSEQUENCE` utvrdi postoji li dokazni most. Nedostatak dokaza označi kao `EVIDENCE GAP`, ne kao dokaz neistinitosti. Tvrdnju koja zavisi samo od samog političkog aktera označi kao `SOURCE-DEPENDENT ATTRIBUTION`.

Ne pripisuj namjeru, manipulaciju, koordinaciju, korupciju ili nezakonitost bez nezavisnog dokaza. Temporalna povezanost političkog zaokreta i političke koristi nije dokaz motiva.

### A-GATE

A ne može biti iznad LOW ako nijedan od A2, A3, A4, A5 ili A8 nema intenzitet najmanje 2.

Ako je A2=4 zbog eksplicitne egzistencijalne/fizičke prijetnje kolektivu, postavi `EXISTENTIAL_THREAT_FRAME = TRUE`.

### Contradiction Persistence Test

Ako postoje T1 i T2 koji mogu biti kontradiktorni, utvrdi:

1. šta je tačno tvrđeno/odlučeno u T1;
2. šta je tačno tvrđeno/odlučeno u T2;
3. jesu li kompatibilni;
4. šta se između njih promijenilo — činjenice, zakon, dokaz, nadležnost ili okolnosti;
5. da li je promjena javno objašnjena;
6. da li je priznata prethodna greška/nepotpunost ili promjena politike;
7. da li postoji podržano alternativno objašnjenje;
8. da li komunikacija implicitno zahtijeva da se oba nespojiva stava prihvate kao ispravna u trenutku kada ih politički autoritet zastupa.

Vrati jedan status:

`NO MATERIAL CONTRADICTION` / `EXPLAINED REVERSAL` / `PARTIALLY EXPLAINED REVERSAL` / `UNEXPLAINED MATERIAL REVERSAL` / `INSUFFICIENT EVIDENCE`.

Obavezno testiraj alternativna objašnjenja prije D3/D4/D6: nova činjenica ili dokaz, promjena zakona, obavezujuća odluka, promjena nadležnosti, pregovarački kompromis, eksplicitno taktička promjena, bezbjednosni kontekst, ispravka greške ili nepotpun raniji javni zapis.

Ne sabiraj P, A i D u jedinstveni score.

Ako je dostupna serija sadržaja, primijeni Longitudinal Mode i provjeri P→A, A→P i A↔D konvergenciju.

## Obavezni izlaz

1. Observed claim
2. Documented / Reality Chain
3. Narrative Chain
4. Missing links / evidence gaps
5. Alternative explanations
6. P1–P9 tabela
7. A1–A8 tabela
8. A-GATE i Existential Threat Flag
9. D1–D6 tabela
10. Contradiction Persistence Test
11. Convergence assessment
12. Classification: P / A / D odvojeno
13. Why not stronger label
14. Šta je dokazano / šta je interpretacija / šta ostaje otvoreno
15. Tri dokumenta ili podatka koji bi najviše mogli promijeniti ocjenu
