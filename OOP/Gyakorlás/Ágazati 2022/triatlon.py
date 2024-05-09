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
    perc = mp%(60*60)//60
    masodperc = mp % 3600 % 60
    return "{:02}:{:02}:{:02}".format(ora,perc,masodperc)
 

f = open("triatlon.txt",encoding="utf8")
f.readline()
triatlonLista = []
for egySor in f:
    triatlonLista.append(Triatlon(egySor))
f.close()
print("2.feladat: A versenyen {} induló volt".format(len(triatlonLista)))

idok = []
for egyIdo in triatlonLista:
    idok.append(egyIdo.uszasIdoMp+egyIdo.kerekparIdoMp+egyIdo.futasIdoMp)

idok.sort()
print("3.feladat: A verseny nyertese:")
print("neve: {}")
print("rajtszáma: {}")
print("összideje: {}".format(Visszavalto(idok[0])))