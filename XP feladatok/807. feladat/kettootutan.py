class Dolgozok:
    def __init__(self,sor):
        vagas = sor.strip().split(";")
        for i in range(len(vagas)):
            vagas[i] = vagas[i].strip('""')
        self.azonosito = int(vagas[0])
        self.nev = vagas[1]
        self.anyjaneve = vagas[2]
        self.telepules = vagas[3]
        self.cim = vagas[4]
        self.netto = int(vagas[5])
        self.juttatas = vagas[6]
        self.belepes = int(vagas[7].split("-")[0])
        self.szuletes = vagas[8]
        self.szulhely = vagas[9]



f = open("dolgozok.txt",encoding="utf8")
f.readline()
sorLista = []
for egySor in f:
    sorLista.append(Dolgozok(egySor))
f.close()
#print(sorLista)
dolgozoLista = []
berLista = []
for egyDolgozo in sorLista:
    if egyDolgozo.belepes > 2005:
        dolgozoLista.append(egyDolgozo.nev)
        berLista.append(egyDolgozo.netto)

#print(dolgozoLista)
#print(berLista)
print("2005 után érkezett dolgozók és nettó bérük:")
for i,egyMunkas in enumerate(dolgozoLista):
    print("{}: {}Ft".format(egyMunkas,berLista[i]))
