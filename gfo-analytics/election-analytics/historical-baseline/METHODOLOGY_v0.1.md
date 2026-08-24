# Historical Baseline Methodology v0.1

## 1. Purpose

Historical Baseline proizvodi statistički profil biračkog mjesta iz više izbornih ciklusa. Profil služi kao referentna tačka za kasniju detekciju odstupanja.

Baseline ne zaključuje da je rezultat regularan, neregularan ili manipulisan.

## 2. Unit of analysis

Osnovna jedinica je:

`canonical_polling_station × historical_election`

Nakon mapiranja, više istorijskih zapisa može pripadati istom trenutnom/ciljnom biračkom mjestu.

## 3. Required separation

Tri vrste poređenja moraju ostati odvojene:

1. turnout/structural baseline;
2. candidate/party/bloc baseline;
3. later anomaly comparison.

Candidate ili bloc istorija ne smije se računati preko izbora koji nisu politički uporedivi bez eksplicitnog mappinga.

## 4. Minimum baseline features

Za svako ciljano biračko mjesto v0.1 računa, gdje su podaci dostupni:

- `historical_election_count`
- `registered_voters_mean`
- `registered_voters_std`
- `turnout_mean`
- `turnout_median`
- `turnout_std`
- `turnout_min`
- `turnout_max`
- `invalid_rate_mean`
- `invalid_rate_std`
- `valid_vote_rate_mean`
- `historical_turnout_range`

Za političke blokove, kada postoji `political_bloc_id`:

- broj uporedivih izbora;
- mean/median/std vote share;
- min/max share;
- posljednji istorijski share.

## 5. Statistical conventions

- procenti se računaju iz apsolutnih vrijednosti kada su dostupne;
- sample standard deviation koristi `n-1` i ostaje `null` kada postoji manje od 2 opažanja;
- `0` nije isto što i missing;
- nevažeći udio je `invalid_votes / total_votes` samo kada je `total_votes > 0`;
- turnout je `total_votes / registered_voters` samo kada je `registered_voters > 0`;
- source-provided percentage može se sačuvati, ali baseline koristi deterministički preračun iz apsolutnih vrijednosti gdje god je moguće.

## 6. Polling-station mapping

Istorijski kod BM nije dovoljan dokaz da je populacija biračkog mjesta ostala ista.

Dozvoljeni mapping statusi:

- `exact_verified`
- `exact_code_unverified`
- `renamed_verified`
- `boundary_changed`
- `split`
- `merged`
- `manual_verified`
- `uncertain`
- `unmapped`

Samo mapping koji je eksplicitno označen kao analitički upotrebljiv ulazi u baseline.

v0.1 automatski ne spaja `split`, `merged`, `boundary_changed` ili `uncertain` zapise.

## 7. Confidence

`mapping_confidence` je vrijednost 0–1.

Preporučeni pragovi:

- 1.00 — zvanično/ručno potvrđena identičnost;
- 0.95 — isti službeni kod i kompatibilni metapodaci;
- 0.80–0.94 — jaka vjerovatnoća, zahtijeva pregled;
- <0.80 — ne ulazi automatski u baseline.

Default prag baseline enginea: `0.95`.

## 8. Historical election eligibility

Svaki izbor mora imati zaseban eligibility profil:

- `turnout_eligible`
- `structural_eligible`
- `political_share_eligible`

Na primjer lokalni izbor može biti koristan za turnout, ali ne mora biti direktno uporediv sa predsjedničkom utrkom za candidate/bloc share.

## 9. Validation

Baseline mora flagovati najmanje:

- duplikate istog `election_id + polling_station_code + candidate`;
- različite station totals unutar istog election/BM zapisa;
- `total_votes > registered_voters`;
- `valid + invalid != total` kada su sva polja dostupna;
- zbir kandidatskih glasova != valid votes za uporedivu single-choice utrku;
- mapping ispod minimalnog confidence praga;
- manje od minimalnog broja istorijskih izbora.

## 10. No anomaly scoring

Baseline feature poput `turnout_std = 0.032` nije anomaly rezultat.

Kasniji engine može izračunati:

`current turnout vs historical distribution`

ali taj korak ne pripada Historical Baseline v0.1.

## 11. Reproducibility

Svaki baseline output mora sadržati:

- input dataset IDs/versions;
- mapping file hash/version;
- baseline engine version;
- konfiguraciju (`min_mapping_confidence`, minimal election count);
- timestamp obrade.

## 12. Core rule

**Historical similarity must be demonstrated, not assumed. A baseline is only as valid as the mapping that connects its historical observations.**
