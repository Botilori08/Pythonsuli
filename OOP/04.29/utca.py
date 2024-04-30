class Telek:
    def __init__(self,sor):
        vag = sor.split(" ")
        self.oldal = int(vag[0])
        self.szelesseg = int(vag[1])
        self.szin = vag[2].strip()
        self.hazszam = 0

telkek = []

parosParatlan = [0,-1]
f = open("kerites.txt")
for egySor in f:
    telkek.append(Telek(egySor))
    parosParatlan[telkek[-1].oldal] += 2
    telkek[-1].hazszam = parosParatlan[telkek[-1].oldal]
f.close()

print("2.feladat:")
print("Az eladott telkek száma: {}".format(len(telkek)))
print("3. feladat")
if telkek[-1].oldal == 0:
    print("A páros oldalon adták el az utolsó telket")
else: 
    print("A páratlan oldalon adták el az utolsó telket")
print("Az utolsó telek házszáma:{}".format(telkek[-1].hazszam))




'''
oldalSzerint= [[],[]]
for egyTelek in telkek:
    if egyTelek.oldal == 0:
        oldalSzerint[0].append(egyTelek.oldal)
    else:
        oldalSzerint[1].append(egyTelek.oldal)


hazszinek = [[],[]]
for egyHaz in telkek:
        if egyHaz.oldal == 0:
            hazszinek[0].append(egyHaz.szin)
        else:
            hazszinek[1].append(egyHaz.szin)
print(hazszinek)
'''

oldalSzerint= [[],[]]
for egyTelek in telkek:
    oldalSzerint[egyTelek.oldal].append(egyTelek)

print("4.feladat")
for i in range(1,len(oldalSzerint[1])):
    if oldalSzerint[1][i].szin == oldalSzerint[1][i-1].szin and oldalSzerint[1][i].szin not in ["#",":"]:
        print("A szomszédossal egyezik a kerítés színe: {}".format(oldalSzerint[1][i].hazszam))
        break

print("5. feladat")

hazszam = int(input("Adjon meg egy házszámot! "))

for i, egyHaz in enumerate(telkek):
    if egyHaz.hazszam == hazszam:
        print("Kerítés színe/állapota: {}".format(egyHaz.szin))

        szinek="QWERTZUIOPASDFGHJKLYXCVBNM"
        szinek = szinek.replace(egyTelek.szin,"")
        if i >0:
            szinek = szinek.replace(telkek[i-1].szin,"")
        if i < len(telkek):
            szinek = szinek.replace(telkek[i+1].szin,"")

        print("Egy lehetséges festési szín {}".format(szinek[0]))
        break
else:
    print("Nincs ilyen házszám!")

#Hf utolsó feladat 

