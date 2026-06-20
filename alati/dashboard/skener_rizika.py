import os

# Lista sistemskih indikatora birokratske opstrukcije i rizika
CRVENI_FLAGOVI = {
    "nije u nadležnosti": "Prebacivanje institucionalne odgovornosti",
    "rok je istekao": "Zloupotreba proceduralnih rokova",
    "utvrđeno je da nije": "Bezlični pasivni jezik bez odgovornog lica",
    "u skladu sa propisima": "Ritualni formalizam bez ulaženja u suštinu",
    "postupak je obustavljen": "Prekid građanskog nadzora"
}

def analiziraj_indeks_rizika(tekst):
    pronadjeni_rizici = []
    bodovi_rizika = 0
    
    for fraza, opis in CRVENI_FLAGOVI.items():
        if fraza in tekst.lower():
            pronadjeni_rizici.append(f"⚠️ {fraza.upper()} -> {opis}")
            bodovi_rizika += 2
            
    print("\n📊 PRELIMINARNI SKENER RIZIKA ZA DASHBOARD")
    print("-" * 40)
    if pronadjeni_rizici:
        for rizik in pronadjeni_rizici:
            print(rizik)
        print("-" * 40)
        print(f"🚨 UKUPNI INDEKS RIZIKA AKTA: {bodovi_rizika}/10")
    else:
        print("✅ Nisu detektovani primarni jezički indikatori opstrukcije.")
    print("-" * 40)

if __name__ == "__main__":
    test_tekst = input("Unesite dio teksta rješenja za brzu procjenu rizika dashboard-a: ")
    analiziraj_indeks_rizika(test_tekst)
