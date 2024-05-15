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
Kvezeteknev = 0
for egynev in fembtLista:
    if egynev.vezeteknev[0] == "K":
        Kvezeteknev += 1
print("{} ember vezetékneve kezdődik K betűvel.".format(Kvezeteknev))
Kkeresztnev = 0
for egyNev in fembtLista:
    if egyNev.keresztnev[0] == "K":
        Kkeresztnev +=1
print("{} ember keresztneve kezdődik K betűvel".format(Kkeresztnev))

varosok = []
for egyVaros in fembtLista:
    varosok.append(egyVaros.telepules)
lakhelyek = list(dict.fromkeys(varosok))

print("Dolgozók lakhelyei:")
for egyLakhely in lakhelyek:
    print("\t" + egyLakhely)
