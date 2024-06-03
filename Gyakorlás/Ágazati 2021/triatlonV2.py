class Triatlon:
    def __init__(self,sor):
        vag = sor.split(";")
        self.nev = vag[0]
        self.nem = vag[1]
        self.szuletesNap = [2]
        self.uszasIdo = vag[3]
        self.uszasMp = int(self.uszasIdo.split(":")[0])*60*60 + int(self.uszasIdo.split(":")[1])*60 + int(self.uszasIdo.split(":")[2])
        self.kerekpar = vag[4]
        self.kerekparMp = int(self.kerekpar.split(":")[0])*60*60 + int(self.kerekpar.split(":")[1])*60 + int(self.kerekpar.split(":")[2])
        self.futas = vag[5]
        self.futasMp = int(self.futas.split(":")[0])*60*60 + int(self.futas.split(":")[1])*60 + int(self.futas.split(":")[2])
        self.rajtszam = int(vag[6])
    def idoValto(Mp):
        ora = Mp //3600
        if ora < 10:
            ora = "0{}".format(ora)
        perc = Mp % 3600 // 60
        if perc < 10:
            perc = "0{}".format(perc)
        masodperc = Mp % 3600 % 60
        if masodperc < 10:
            masodperc = "0{}".format(masodperc)
        
        return "{}:{}:{}".format(ora,perc,masodperc)

f=open("triatlon.txt",encoding="utf8")
f.readline()
triatlonLista = []
for egySor in f:
    triatlonLista.append(Triatlon(egySor))
f.close()
ferfiak = 0
for egyAdat in triatlonLista:
    if egyAdat.nem == "f":
        ferfiak += 1
print("2.feladat: A versenyen {} férfi induló volt".format(ferfiak))

idoMpLista=[]
for egyIdo in triatlonLista:
    egyIdo = egyIdo.uszasMp + egyIdo.kerekparMp+ egyIdo.futasMp
    idoMpLista.append(egyIdo)
idoMpLista.sort()
nyertes = idoMpLista[0]


nyertesneve = ""
rajtszam = 0
for egyElem in triatlonLista:
    if nyertes == egyElem.uszasMp + egyElem.kerekparMp + egyElem.futasMp:
        nyertesneve = egyElem.nev
        rajtszam += egyElem.rajtszam

print("3.feladat: A verseny női nyertese:")
print("\t neve: {}".format(nyertesneve))
print("\t rajtszáma: {}".format(rajtszam))
print("\t összideje: {}".format(Triatlon.idoValto(nyertes)))

f = open("osszidokV2.txt","w")
for egyElem in triatlonLista:
    f.write("{};{};{} \n".format(egyElem.nev,egyElem.rajtszam,Triatlon.idoValto(egyElem.uszasMp + egyElem.kerekparMp + egyElem.futasMp)))

