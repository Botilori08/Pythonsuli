import math
class Kontener:
    def __init__(self,sor):
        vag = sor.split("#")
        self.nev = vag[0]
        self.telepules = vag[1]
        self.cim = vag[2]
        self.szuletes = vag[3]
        self.fizetes = int(vag[4])

f = open("kontenerkft.txt",encoding="utf8")
kontenerKft = []
for egySor in f:
    kontenerKft.append(Kontener(egySor))
f.close()

f = open("hatszol.txt","w",encoding="utf8")
hatszolFizetes = []
for egyAdat in kontenerKft:
    if egyAdat.telepules == "Hatvan" or egyAdat.telepules == "Szolnok":
        f.write(egyAdat.nev+"\n")
        hatszolFizetes.append(egyAdat.fizetes)
f.close()
osszFizetes = 0
for egyFizetes in hatszolFizetes:
    osszFizetes += egyFizetes

print("A hatvani és szolnoki dolgozók átlagbére {} Ft".format(math.floor(osszFizetes / len(hatszolFizetes))))
