class Keszthely:
    def __init__(self,sor):
        vagas = sor.split(";")
        self.nev = vagas[0]
        self.szuletesEv = int(vagas[1])
        self.rajtszam = vagas[2]
        self.nemKod = vagas[3]
        self.kategoria = vagas[4]
        #idők 
        self.uszasIdoMp = int(vagas[5].split(":")[0])*60*60 + int(vagas[5].split(":")[1])*60 + int(vagas[5].split(":")[2])
        self.elsoDepoMp = int(vagas[6].split(":")[0])*60*60 + int(vagas[6].split(":")[1])*60 + int(vagas[6].split(":")[2])
        self.kerekparIdo = int(vagas[7].split(":")[0])*60*60 + int(vagas[7].split(":")[1])*60 + int(vagas[7].split(":")[2])
        self.masodikDepo = int(vagas[8].split(":")[0])*60*60 + int(vagas[8].split(":")[1])*60 + int(vagas[8].split(":")[2])
        self.futasIdo = int(vagas[9].split(":")[0])*60*60 + int(vagas[9].split(":")[1])*60 + int(vagas[9].split(":")[2])

def eletkor(ev):
    return 2024 - ev

def idoVisszavaltas(ido):
    ora = ido//(60*60)
    perc = ido%(60*60)//60
    masodperc = ido % 3600 % 60
    return "{:02}:{:02}:{:02}".format(ora,perc,masodperc)

f = open("Eredmenyek.txt")
eredmenyLista = []
for egySor in f:
    eredmenyLista.append(Keszthely(egySor))
print("2.feladat: A versenyt {} versenyző fejezte be".format(len(eredmenyLista)))
elitJuniorszam = 0
for egyElem in eredmenyLista:
    if egyElem.kategoria == "elit junior":
        elitJuniorszam += 1
print('3.feladat: Versenyzők száma az "elit junior" kategóriában: {} fő'.format(elitJuniorszam))
evek = []
for egyEv in eredmenyLista:
    evek.append(eletkor(egyEv.szuletesEv))
eletkorok = 0
for Ev in evek:
    eletkorok += Ev
print("4. feladat: Átlagéletkor: {}".format(round(eletkorok/len(evek),2)))

bekeres = input("5.feladat: Kérek egy kategóriát: ")
for egyEv in eredmenyLista:
    if bekeres == egyEv.kategoria:
        print("Rajtszám(ok):{}".format(egyEv.rajtszam))

print("6.feladat: A legjobb időt {} érte el.")
idok = []
for egyIdo in eredmenyLista:
    idok.append(egyIdo.uszasIdoMp + egyIdo.elsoDepoMp + egyIdo.kerekparIdo + egyIdo.masodikDepo + egyIdo.futasIdo)
idok.sort()

