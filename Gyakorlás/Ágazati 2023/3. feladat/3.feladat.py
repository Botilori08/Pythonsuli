class Hegyek:
    def __init__(self,sor):
        vagas = sor.split(";")
        self.hegycsucsNev = vagas[0]
        self.hegysegNev = vagas[1]
        self.magassag = int(vagas[2])
    def labatValto(ertek):
        atvaltott = ertek*3.280839895
        return atvaltott

hegyLista = [] 
f = open("hegyekMo.txt")
f.readline()
for egySor in f:
    hegyLista.append(Hegyek(egySor))
f.close()
print("2.feladat")
print("\t A hegycsúcsok száma: {}".format(len(hegyLista)))
print("3.feladat")
magassagok = []
Osszmagassag = 0
for egyMagassag in hegyLista:
    magassagok.append(egyMagassag.magassag)
    Osszmagassag += egyMagassag.magassag
print(" \t A hegycsúcsok átlagos magassága: {} m".format(round(Osszmagassag/len(magassagok),2)))
print("4. feladat")
magassagok.sort()
legkisebb = magassagok[0]
legkisebbneve = ""
for egyElem in hegyLista:
    if egyElem.magassag == legkisebb:
        legkisebbneve = egyElem.hegycsucsNev

print("\t A legalacsonyabb csúcs: {}".format(legkisebbneve))
f = open("matra.txt","w")
for egyElem in hegyLista:
    if egyElem.hegysegNev == "Mátra":
        f.write(str(round(Hegyek.labatValto(egyElem.magassag),1))+"\n")
f.close()
