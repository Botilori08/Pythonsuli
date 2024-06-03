from collections import Counter
class Billboard:
    def __init__(self,sor):
        vagas = sor.split(";")
        self.helyezes = int(vagas[0])
        self.cim = vagas[1]
        self.eloado = vagas[2]
        self.elozo = vagas[3]
        self.legjobb = int(vagas[4])
        self.hetszam = int(vagas[5])

f = open("billboard.csv")
f.readline()
sorLista = []
for egySor in f:
    sorLista.append(Billboard(egySor))
f.close()

print("2.feladat:")
bekertHely = int(input("Kérek egy pozíciót: "))
for egyHely in sorLista:
    if egyHely.helyezes == bekertHely:
        print("\t A lista {}. helyén szereplő dal: {}: {}".format(bekertHely,egyHely.eloado,egyHely.cim))

print("4.feladat")
eloadok = []
for egyEloado in sorLista:
    eloadok.append(egyEloado.eloado)

print(eloadok)
