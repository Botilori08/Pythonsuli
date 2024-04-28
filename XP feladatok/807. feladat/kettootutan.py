class Dolgozok:
    def __init__(self,sor):
        vagas = sor.split(";")
        self.azonosito = vagas[0]
        self.nev = vagas[1]
        self.anyjaneve = vagas[2]
        self.telepules = vagas[3]
        self.cim = vagas[4]
        self.netto = vagas[5]
        self.juttatas = vagas[6]
        self.belepes = vagas[7]
        self.szuletes = vagas[8]
        self.szulhely = vagas[9]



f = open("dolgozok.txt",encoding="utf8")
sorLista = []
for egySor in f:
    sorLista.append(Dolgozok(egySor.strip()))
f.close()
print()
