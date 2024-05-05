class Fembt:
    def __init__(self,sor):
        vagas = sor.split(":")
        self.vezeteknev = vagas[0].split(" ")[0]
        self.keresztnev = vagas[0].split(" ")[1]
        self.telepules = vagas[1]
        self.cim = vagas[2]
        self.szuletes = vagas[3]
        self.fizetes = int(vagas[4])

f = open("fembt.txt",encoding="utf8")
fembtLista = []
for egySor in f:
    fembtLista.append(Fembt(egySor))
f.close()
Kvezetnev = 0
for egynev in fembtLista:
    if egynev.vezeteknev[0] == "K":
        Kvezetnev += 1
print(Kvezetnev)
