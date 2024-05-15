import math
class Dolgozo:
    def __init__(self,sor):
        vag = sor.split(";")
        self.azonosito = int(vag[0])
        self.nev = vag[1]
        self.anyjaneve = vag[2]
        self.telepules = vag[3]
        self.cim = vag[4]
        self.fizetes = int(vag[5])
        self.jutalom = int(vag[6])
        self.belepes = vag[7]
        self.szuletes = vag[8]
        self.szulhely = vag[9]

f = open("dolgozok.txt",encoding="utf8" )
lista= []
for egySor in f:
    lista.append(Dolgozo(egySor))
f.close()

jutalmak = 0
for elem in lista:
    jutalmak += elem.jutalom
print("A jutalmak összege {} Ft".format(jutalmak))

fizetesek = []
osszFizetes = 0
for egyFizetes in lista:
    fizetesek.append(egyFizetes.fizetes)
for egyErtek in fizetesek:
    osszFizetes += egyErtek
print("A fizetések átlaga: {} Ft".format(math.floor(osszFizetes / len(fizetesek))))

lakhelyVizsgalat = False
for egylakhely in lista:
    if egylakhely.telepules == "Recsk":
        lakhelyVizsgalat = True
    else:
        lakhelyVizsgalat = False

    if lakhelyVizsgalat == True:
        print("Van recski dolgozó.")

tataiakSzama = 0
for egyLakos in lista:
    if egyLakos.telepules == "Tata":
        tataiakSzama += 1
print("{} db tatai dolgozó van".format(tataiakSzama))


