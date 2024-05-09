class Triatlon:
    def __init__(self,sor):
        vag = sor.split(";")
        self.nev = vag[0]
        self.nem = vag[1]
        self.szuletes = vag[2]
        self.uszasIdo = vag[3].split(":")
        self.uszasIdoMp = int(self.uszasIdo[0])*60*60 + int(self.uszasIdo[1])*60 + int(self.uszasIdo[2])
        self.kerekparIdo = vag[4].split(":")
        self.kerekparIdoMp = int(self.kerekparIdo[0])*60*60 + int(self.kerekparIdo[1])*60 + int(self.kerekparIdo[2])
        self.futasIdo = vag[5].split(":")
        self.futasIdoMp = int(self.futasIdo[0])*60*60 + int(self.futasIdo[1])*60 + int(self.futasIdo[2])
        self.rajtszam = int(vag[6])

def Visszavalto(mp):
    ora = mp//(60*60)
    if ora < 10:
        ora = "0{}".format(mp//(60*60))
    perc = mp%(60*60)//60
    if perc < 10:
        perc= "0{}".format(mp%(60*60)//60)
    masodperc = mp % 3600 % 60
    if masodperc < 10:
        masodperc= "0{}".format(mp % 3600 % 60)
                                
    return "{}:{}:{}".format(ora,perc,masodperc)
 

f = open("triatlon.txt",encoding="utf8")
f.readline()
triatlonLista = []
for egySor in f:
    triatlonLista.append(Triatlon(egySor))
f.close()
print("2.feladat: A versenyen {} induló volt".format(len(triatlonLista)))

idok = []
for egyIdo in triatlonLista:
    idok.append(Visszavalto(egyIdo.uszasIdoMp+egyIdo.kerekparIdoMp+egyIdo.futasIdoMp))
idok.sort()
nyertes = ""
rajtszam = 0
for egyTime in triatlonLista:
    if Visszavalto(egyTime.uszasIdoMp+egyTime.kerekparIdoMp+egyTime.futasIdoMp) == idok[0]:
        nyertes = egyTime.nev
        rajtszam = egyTime.rajtszam

print("3.feladat: A verseny nyertese:")
print("neve: {}".format(nyertes))
print("rajtszáma: {}".format(rajtszam))
print("összideje: {}".format(idok[0]))

f = open("osszidok.txt","w")
for egyOsszeg in triatlonLista:
    f.write("{};{};{}".format(egyOsszeg.rajtszam,egyOsszeg.nev,Visszavalto(egyOsszeg.uszasIdoMp+egyOsszeg.kerekparIdoMp+egyOsszeg.futasIdoMp))+"\n")
f.close()