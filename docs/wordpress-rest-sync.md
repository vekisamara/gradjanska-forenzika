# WordPress REST API sinhronizacija

Ovaj repozitorij može automatski kreirati ili ažurirati WordPress postove iz Markdown datoteka u folderu `blog/`.

## Tok rada

1. Članak se kreira ili izmijeni u `blog/*.md`.
2. Izmjena se pošalje na granu `main`.
3. GitHub Actions pokreće `.github/workflows/sync-wordpress.yml`.
4. Skripta `scripts/sync_wordpress.py` čita YAML front matter i Markdown.
5. WordPress post se pronalazi prema `slug` vrijednosti.
6. Post se kreira ili ažurira, a kategorije i tagovi se automatski usklađuju.

Sinhronizacija je jednosmjerna: **GitHub → WordPress**. Skripta ne briše WordPress postove.

## 1. Provjera REST API-ja

Otvorite u pregledniku:

```text
https://VAŠ-SAJT/wp-json/
```

Za trenutnu instalaciju vjerovatna adresa je:

```text
https://analize.gradjanskaforenzika.org/wp/wp-json/
```

Ako dobijete JSON odgovor, REST API je dostupan. Ako dobijete 403, HTML grešku ili preusmjerenje, provjerite sigurnosni plugin, hosting firewall, Cloudflare pravila i WordPress permalink postavke.

## 2. Poseban WordPress korisnik

Preporučeno je napraviti poseban WordPress korisnički nalog za automatizaciju, na primjer:

```text
github-publisher
```

Uloga:

- **Editor** ako treba kreirati i objavljivati postove te upravljati kategorijama i tagovima;
- **Author** nije dovoljan za sve operacije kategorizacije na svim instalacijama;
- **Administrator** nije potreban.

## 3. Application Password

U WordPress administraciji:

1. Otvorite **Users → Profile** za korisnika automatizacije.
2. Pronađite odjeljak **Application Passwords**.
3. Unesite naziv, na primjer `GitHub gradjanska-forenzika`.
4. Kreirajte lozinku.
5. Kopirajte prikazanu lozinku odmah; WordPress je neće ponovo prikazati.

Application Password nije glavna lozinka korisnika. Može se zasebno opozvati bez promjene prijave u WordPress.

## 4. GitHub Actions Secrets

U repozitoriju `vekisamara/gradjanska-forenzika` otvorite:

**Settings → Secrets and variables → Actions → New repository secret**

Dodajte:

| Secret | Vrijednost |
|---|---|
| `WP_SITE_URL` | Osnovni URL WordPress instalacije, npr. `https://analize.gradjanskaforenzika.org/wp` |
| `WP_USERNAME` | WordPress korisničko ime automatizacije |
| `WP_APPLICATION_PASSWORD` | Application Password generisan u WordPressu |

Ne dodavati navodnike. Application Password može biti unesen sa ili bez razmaka; skripta uklanja razmake.

## 5. Prvi test

Otvorite karticu **Actions** u GitHub repozitoriju, izaberite **Sync blog to WordPress** i kliknite **Run workflow**.

Ručni test sinhronizuje sve `.md` datoteke iz foldera `blog/`. Kasniji push u `main` sinhronizuje izmijenjene članke.

Post sa istim `slug` poljem biće ažuriran, a ne dupliciran.

## Front matter format

```yaml
---
title: "Naslov članka"
slug: "naslov-clanka"
date: 2026-08-07
language: sr-Latn
status: draft
excerpt: "Kratak opis članka."
categories:
  - Građanska forenzika
  - EU standardi, lokalna praksa
tags:
  - transparentnost
  - javna uprava
---
```

Podržani statusi:

- `draft`
- `published` ili `publish`
- `private`
- `pending`
- `future`

Za sigurniji urednički tok koristite `status: draft`. Promijenite na `published` tek nakon provjere.

## Sigurnosne napomene

- Koristiti isključivo HTTPS.
- Ne upisivati korisničko ime ili Application Password u Markdown, Python ili workflow datoteke.
- Za automatizaciju koristiti poseban WordPress nalog sa najmanjim dovoljnim ovlaštenjima.
- Opozvati Application Password kada se više ne koristi ili ako postoji sumnja da je kompromitovan.
- GitHub treba ostati primarni izvor teksta; ručne izmjene u WordPressu mogu biti prepisane sljedećom sinhronizacijom.

## Najčešće greške

### `401 rest_cannot_create`

Korisnik nema potrebna ovlaštenja ili Application Password nije ispravan.

### `403 forbidden`

Sigurnosni plugin, hosting firewall ili proxy blokira REST API ili Basic Authentication zaglavlje.

### `404 No route was found`

Provjeriti `WP_SITE_URL`. Mora pokazivati na direktorij u kojem je WordPress instaliran.

### Post je objavljen umjesto nacrta

Status u Markdown front matteru određuje WordPress status. Koristite:

```yaml
status: draft
```

### Dupli postovi

Svaki članak mora imati stabilan i jedinstven `slug`. Ne mijenjati slug nakon prve sinhronizacije bez namjerne migracije.
