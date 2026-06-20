# 🪟 Uputstvo za pokretanje skripte na Windows sistemu

Ova skripta vam omogućava da potpuno lokalno, na svom računaru, očistite osjetljive lične podatke (JMBG, adresu, telefon, e-mail) iz rješenja i zapisnika prije nego što ih pošaljete na analizu vještačkoj inteligenciji. 

Vaši podaci nigdje ne odlaze sa računara — proces je 100% privatan i bezbjedan.

---

## 🛠️ Korak 1: Instalacija Pythona (Samo prvi put)

Da bi skripta radila na Windowsu, potrebno je da imate instaliran programski jezik Python:

1. Idite na zvanični sajt i preuzmite instalaciju: [python.org/downloads](https://python.org) (kliknite na žuto dugme **Download Python**).
2. Pokrenite preuzeti instalacioni fajl.
3. ⚠️ **VAŽNO:** Na samom dnu instalacionog prozora obavezno označite kućicu **"Add python.exe to PATH"** prije nego što kliknete na *Install Now*.
4. Sačekajte da se instalacija završi i zatvorite prozor.

---

## 📦 Korak 2: Instalacija dodatka za Word (.docx) dokumente

Skripta podržava i obradu Word dokumenata, za šta joj je potreban jedan mali dodatak:

1. Kliknite na Windows *Start* meni, ukucajte **cmd** i otvorite **Command Prompt**.
2. Nalijepite sljedeću komandu i pritisnite **Enter**:
   ```cmd
   pip install python-docx
   ```
3. Kada se ispiše poruka da je instalacija uspješna, možete zatvoriti prozor.

---

## 🚀 Korak 3: Preuzimanje i pokretanje skripte

1. Preuzmite fajl `anonimizacija.py` iz ovog foldera na svoj računar.
2. Otvorite **Command Prompt** (cmd) ponovo.
3. Ukucajte `python` i napravite razmak, a zatim **prevucite mišem** fajl `anonimizacija.py` iz vašeg foldera direktno u taj crni prozor (sistem će sam ispisati putanju). Pritisnite **Enter**.
4. Skripta će vas pitati da unesete putanju do vašeg dokumenta (`.txt` ili `.docx`).
5. Jednostavno **prevucite dokument koji želite očistiti** u prozor i pritisnite **Enter**.

💡 *Novi, bezbjedni dokument sa oznakom `_anonimizovano` biće kreiran u istom folderu gdje se nalazio i vaš originalni dokument!*
