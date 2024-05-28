class Hegyek:
    def __init___(self,sor):
        vagas = sor.split(";")
        self.hegycsucsNev = vagas[0]
        self.hegysegNev = vagas[1]
        self.magassag = int(vagas[2])

hegyLista = [] 
f = open("hegyekMo.txt")
f.readline()
for egySor in f:
    hegyLista.append(Hegyek(egySor))
print("2.feladat")
print("\t A hegycsúcsok száma: {}".format(len(hegyLista)))
print("3.feladat")
magassagok = []
for egyMagassag in hegyLista:
    magassagok.append(egyMagassag.magassag)
print(magassagok)
