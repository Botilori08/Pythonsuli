class Pontbt:
    def __init__(self,sor):
        vagas = sor.split(":")
        self.sorszam = vagas[0]
        self.nev = vagas[1]
        self.varos = vagas[2]
        self.utcaHazszam = vagas[3]
        self.osszeg = int(vagas[4])
        self.datum = vagas[5]

f = open("dolgozok.txt")
dolgozoLista = []
for egySor in f:
    dolgozoLista.append(Pontbt(egySor))
f.close()
osszegek = []
for egyElem in dolgozoLista:
    if egyElem.varos == "Szolnok":
        osszegek.append(egyElem.osszeg)
#print(osszegek)
osszeg = 0
for egyOsszeg in osszegek:
    osszeg+=egyOsszeg
print("A Szolnokiakhoz tartozó pézösszegek összege: {} Ft".format(osszeg))


