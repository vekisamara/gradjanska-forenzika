# 🔍 Uputstvo za skriptu: Analiza PDF metapodataka (`forenzika_pdf.py`)

Ovaj alat vam omogućava da zavirite u skrivene slojeve digitalnih PDF dokumenata (rješenja, zapisnika, odluka) koje su izdale institucije i otkrijete ko je stvarni autor, kada je dokument kreiran i koji softver je korišćen.

## 🚀 Kako pokrenuti skriptu na Windows-u

1. Provjerite da li imate instaliran dodatak za čitanje PDF-a. Otvorite **Command Prompt (cmd)**, nalijepite komandu ispod i pritisnite **Enter**:
   ```cmd
   pip install pypdf
   ```
2. Ugasite Command Prompt i ponovo ga pokrenite.
3. Ukucajte riječ `python` i napravite razmak.
4. Prevucite fajl `forenzika_pdf.py` iz vašeg foldera direktno u prozor Command Promp-a i pritisnite **Enter**.
5. Kada vas skripta pita za putanju, **prevucite PDF dokument koji želite analizirati** u prozor i pritisnite **Enter**.

---

## 📊 Primjer forenzičkog izvještaja na terenu

Kada građanin unese PDF rješenje dobijeno od neke institucije, skripta u prozoru ispisuje jasan izvještaj:

```text
==================================================
🔍 FORENZIČKI IZVJEŠTAJ METAPODATAKA DOKUMENTA
==================================================
📁 Naziv fajla: Odbijanje_Zalbe_Gradjanina.pdf
📄 Broj stranica u dokumentu: 3
--------------------------------------------------
📌 Autor (Author/Korisnik računara): Milan_Pravna_Sluzba_Kompanije
📌 Kreator (Aplikacija): Microsoft® Word 2021
📌 Datum kreiranja: 2026-06-15 10:14:22
--------------------------------------------------
💡 Savjet za građansku forenziku:
Ukoliko se ime autora (Author) u sistemu razlikuje od imena službenika koji je potpisao papir, to je jasan digitalni trag da je nacrt rješenja pisala treća strana (npr. privatni investitor ili spoljni saradnik), što predstavlja osnov za sumnju u sukob interesa.
==================================================
```
