# Civic Decision Engine — KAIT specifikacija v0.1

## Integracija

KAIT se implementira unutar GFO Analysis sloja i proširuje entitete Claim, Evidence, Edge, Gap i Finding. Ne uvodi paralelni engine. Report Builder smije koristiti samo high-impact KAIT nalaze koje je potvrdio recenzent.

## Podatkovni model

| Entitet | Ključna polja |
|---|---|
| Claim | claim_type, exact_text, paraphrase, speaker_actor_id, source_locator, certainty, scope, declared_purpose, operative_function |
| Warrant | source_ref, evidence_level, source_status, proposition_supported, relevance, limitations |
| Premise | text, explicit, source_ref, challenge_status |
| ClaimAnalysis | warrants, premises, counterevidence, alternative_explanations, adequacy_status, adequacy_reason, missing_evidence, review_status |
| TermRegister | term, meaning_in_document, normative_reference, usage_variants, material_effect |

## Programske validacije

| Pravilo | Kriterijum |
|---|---|
| Citation lock | High-impact tvrdnja bez lokatora ne može biti `confirmed`. |
| Source-status lock | R/N izvor ne može dati konačan citat niti sam zatvoriti high-impact nalaz. |
| Adequacy separation | `evidence_level` ne smije automatski popuniti `adequacy_status`. |
| Scope lock | Kategorična ili generalizovana tvrdnja zahtijeva eksplicitno obrazloženje adekvatnosti. |
| Alternative lock | Negativan high-impact nalaz zahtijeva neutralnu alternativu ili obrazloženo `nije primjenjivo`. |
| Counterevidence gate | Neobrađen D1/D2 protivdokaz blokira finalizaciju. |
| Causality lock | Temporal edge ne smije automatski postati uzročna veza. |
| Knowledge boundary | Razlikovati dokument u spisu, institucionalno dostupan i eksterni dokument. |
| Linkage orphan check | Prikazati tvrdnje bez warrant veze i dokaze bez analitičke veze. |
| Motive lock | Motiv, pogodovanje i koordinacija traže direktan izvor i ljudsku potvrdu. |

## Acceptance criteria

- **AC-K01:** 100% high-impact tvrdnji ima lokator ili oznaku „nije utvrđeno“.
- **AC-K02:** 100% R/N oznaka očuvano je kroz transformacije.
- **AC-K03:** nema automatskih statusa adekvatnosti izvedenih samo iz D nivoa.
- **AC-K04:** najmanje 95% ručno označenih protivdokaza pronađeno je u ATA-1 gold setu.
- **AC-K05:** nema temporal-only veza prikazanih kao uzročnost.
- **AC-K06:** svaki negativni high-impact nalaz ima alternativno objašnjenje ili test.
- **AC-K07:** najmanje 90% slaganja dva analitičara o vrsti tvrdnje i adekvatnosti nakon kalibracije.
- **AC-K08:** svaki javni high-impact nalaz ima `review_status: confirmed`.

## MVP prioritet

1. Claim/Warrant/Premise JSON objekti i četiri statusa adekvatnosti.
2. Ljudska potvrda te citation, source-status, causality i motive lock.
3. Claim Inspector, Argument Chain i Orphan Queue.
4. Izvoz claim matrice u JSON i dokumentni format.
5. Regresija na ATA-1 i najmanje dva dodatna predmeta.

Referentna šema: [`sheme/kait_claim_analysis_v0.1.schema.json`](sheme/kait_claim_analysis_v0.1.schema.json).

