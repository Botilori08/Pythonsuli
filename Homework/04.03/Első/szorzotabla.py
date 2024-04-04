
class Szorzasok:
    def __init__(self,sor):
        vagas = sor.split(",")
        self.elso = int(vagas[0])
        self.masodik = int(vagas[1])
        self.harmadik = int(vagas[3])
        self.negyedik = int(vagas[4])
        self.otodik = int(vagas[5])
        self.hatodik = int(vagas[6])
        self.hetedik = int(vagas[7])
        self.nyolcadik = int(vagas[8])
        self.kilencedik = int(vagas[9])
        self.tizedik= int(vagas[10])


        

szamok = []
f = open("szamparok.txt")
for egySor in f:
    szamok.append(Szorzasok(egySor.strip()))
#print(szamok)

f.close() 


for egyszam in szamok:
    print("{} x {} = {}".format(egyszam.elso,egyszam.elso,egyszam.elso*egyszam.elso))
    print("{} x {} = {}".format(egyszam.masodik,egyszam.masodik,egyszam.masodik*egyszam.masodik))
    print("{} x {} = {}".format(egyszam.harmadik,egyszam.harmadik,egyszam.harmadik*egyszam.harmadik))
    print("{} x {} = {}".format(egyszam.negyedik,egyszam.negyedik,egyszam.negyedik*egyszam.negyedik))
    print("{} x {} = {}".format(egyszam.otodik,egyszam.otodik,egyszam.otodik*egyszam.otodik))
    print("{} x {} = {}".format(egyszam.hatodik,egyszam.hatodik,egyszam.hatodik*egyszam.hatodik))
    print("{} x {} = {}".format(egyszam.hetedik,egyszam.hetedik,egyszam.hetedik*egyszam.hetedik))
    print("{} x {} = {}".format(egyszam.nyolcadik,egyszam.nyolcadik,egyszam.nyolcadik*egyszam.nyolcadik))
    print("{} x {} = {}".format(egyszam.kilencedik,egyszam.kilencedik,egyszam.kilencedik*egyszam.kilencedik))
    print("{} x {} = {}".format(egyszam.tizedik,egyszam.tizedik,egyszam.tizedik*egyszam.tizedik))





