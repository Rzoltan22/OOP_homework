from abc import ABC, abstractmethod
from datetime import datetime


# Absztrakt osztály: Járat
class Jarat(ABC):
    def __init__(self, jaratszam, honnanhova, jegyar):
        self.jaratszam = jaratszam
        self.honnanhova = honnanhova
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

# Belföldi Járat
class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"

# Nemzetközi Járat
class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"

# JegyFoglalás
class JegyFoglalas:
    def __init__(self, utas_nev, jarat, honnanhova, datum):
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.honnanhova = honnanhova
        self.datum = datum
        self.ar = jarat.jegyar

# LégiTársaság
class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def foglalas(self, utas_nev, jaratszam, honnanhova, datum):
        if datum < datetime.now():
            return "Hibás dátum. Csak jövőbeli időpontokra lehet foglalni."
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                foglalas = JegyFoglalas(utas_nev, jarat, honnanhova, datum)
                self.foglalasok.append(foglalas)
                return f"Sikeres foglalás. Ár: {foglalas.ar} Ft"
        return "Nincs ilyen járat."

    def lemondas(self, utas_nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                return "Foglalás sikeresen lemondva."
        return "Nem található ilyen foglalás."

    def listaz_foglalasok(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        lista = []
        for f in self.foglalasok:
            lista.append(f"{f.utas_nev} - {f.jarat.jaratszam} ({f.jarat.honnanhova}) - {f.datum.strftime('%Y-%m-%d')} - {f.jarat.jarat_tipus()}")
        return "\n".join(lista)


def fo_menu(legitarsasag):
    while True:
        print("\n Repülőjegy Foglalás")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasz = input("Válassz egy műveletet: ")

        if valasz == "1":
            print("NemzetköziJarat LH100, Budapest-Stutgart 10000")
            print("NemzetköziJarat LH200, London-Budapest, 30000")
            print("NemzetköziJarat LH300, New York-Berlin, 60000")
            print("NemzetköziJarat LH400, Studgart-San Francisco, 80000")
            print("NemzetköziJarat LH500, Paris-Wienna, 20000")
            print("NemzetköziJarat LH600, Debrecen-Berlin, 15000")
            print("NemzetköziJarat LH700, Tokio-Honolulu, 100000")
            print("NemzetköziJarat LH800, Berlin-Warsó, 12000")
            print("BelföldiJarat LH900, Debrecen-Budapest, 5000")
            print("BelföldiJarat LH1000, Budapest-Debrecen, 5000")
            utas = input("Név: ")
            jarat = input("Járatszám: ")
            honnanhova = input("Honnan-Hova: ")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                datum_dt = datetime.strptime(datum, "%Y-%m-%d")
                print(legitarsasag.foglalas(utas, jarat, honnanhova, datum_dt))
            except ValueError:
                print("Hibás dátumformátum.")
        elif valasz == "2":
            utas = input("Név: ")
            jarat = input("Járatszám: ")
            print(legitarsasag.lemondas(utas, jarat))
        elif valasz == "3":
            print("\n Foglalások")
            print(legitarsasag.listaz_foglalasok())
        elif valasz == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")


# Rendszer inicializálása
lufthansa = Legitarsasag("Lufthansa")

# 10 járat
jarat1 = NemzetkoziJarat("LH100", "Budapest-Stutgart", 10000)
jarat2 = NemzetkoziJarat("LH200", "London-Budapest", 30000)
jarat3 = NemzetkoziJarat("LH300", "New York-Berlin", 60000)
jarat4 = NemzetkoziJarat("LH400", "Studgart-San Francisco", 80000)
jarat5 = NemzetkoziJarat("LH500", "Paris-Wienna", 20000)
jarat6 = NemzetkoziJarat("LH600", "Debrecen-Berlin", 25000)
jarat7 = NemzetkoziJarat("LH700", "Tokio-Honolulu", 100000)
jarat8 = NemzetkoziJarat("LH800", "Berlin-Warsó", 15000)
jarat9 = BelfoldiJarat("LH900", "Debrecen-Budapest", 5000)
jarat10 = BelfoldiJarat("LH1000", "Budapest-Debrecen", 5000)

lufthansa.hozzaad_jarat(jarat1)
lufthansa.hozzaad_jarat(jarat2)
lufthansa.hozzaad_jarat(jarat3)
lufthansa.hozzaad_jarat(jarat4)
lufthansa.hozzaad_jarat(jarat5)
lufthansa.hozzaad_jarat(jarat6)
lufthansa.hozzaad_jarat(jarat7)
lufthansa.hozzaad_jarat(jarat8)
lufthansa.hozzaad_jarat(jarat9)
lufthansa.hozzaad_jarat(jarat10)

# 6 foglalás (jövőbeli dátummal)
datum = datetime(2025, 6, 15)
lufthansa.foglalas("Kovács Anna", "LH100", "Budapest-Stutgart", datum)
lufthansa.foglalas("Nagy Péter", "LH200", "London-Budapest", datum)
lufthansa.foglalas("Szabó Éva", "LH300", "New York-Berlin", datum)
lufthansa.foglalas("Kiss Gábor", "LH400", "Studgart-San Francisco", datum)
lufthansa.foglalas("Varga Luca", "LH900", "Debrecen-Budapest", datum)
lufthansa.foglalas("Tóth Imre", "LH500", "Paris-Wienna", datum)

# Interfész indítása
fo_menu(lufthansa)
