class Dolgozok:
    def __init__(self,sor):
        vag = sor.split(":")
        self.szam = int(vag[0])
        self.nev = vag[1]
        self.varos = vag[2]
        self.utca = vag[3]
        self.hazszam = int(vag[3].split(" ")[2])
        self.osszeg = int(vag[4])
        self.szuletesiDatum = vag[5]

f = open("dolgozok.txt")
dolgozoLista = []
for egySor in f:
    dolgozoLista.append(Dolgozok(egySor))
f.close()
#print(dolgozoLista)
osszegLista = []
for egyElem in dolgozoLista:
    osszegLista.append(egyElem.osszeg)
Osszeg = 0
for egyOsszeg in osszegLista:
    Osszeg += egyOsszeg
print("A pénzösszegek összege: {} Ft".format(Osszeg))
print(egyElem.hazszam)





