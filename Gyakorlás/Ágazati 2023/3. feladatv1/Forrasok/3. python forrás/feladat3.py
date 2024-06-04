class Billboard:
    def __init__(self,sor):
        vagas = sor.split(";")
        self.helyezes = int(vagas[0])
        self.cim = vagas[1]
        self.eloado = vagas[2]
        self.elozo = vagas[3]
        self.legjobb = int(vagas[4])
        self.hetszam = int(vagas[5])

    def ujVizsgalat(elozohet,het):
        ujak = 0
        if elozohet== "-" and het == 1:
            ujak+=1
        return ujak
            


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


print("3. feladat:")
belepokszama = 0
for egyElem in sorLista:
    belepokszama += Billboard.ujVizsgalat(egyElem.elozo,egyElem.hetszam)
print("\t A héten {} új belépő volt.".format(belepokszama))
    

print("4.feladat")
eloadok = []
listaSok = {}
for egyEloado in sorLista:
    eloadok.append(egyEloado.eloado)
for egyElem in eloadok:
    if egyElem in listaSok:
        listaSok[egyElem]+=1
    else:
        listaSok[egyElem] = 1

legtobbnev = list(listaSok)[0]
print("\t A legtöbbet szereplő előadó(k): {}".format(legtobbnev))

f = open("eloadok.txt","w")
eloadok = list(listaSok)
for egyEloado in eloadok:
        f.write("{}\n".format(egyEloado))







