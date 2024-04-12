import radioClass as rc

f = open("veetel.txt")

sorszam = 0
tempSor=""
uzenetek = []
for egySor in f: 
    if sorszam %2==0:
        tempSor=egySor
    else:
        uzenetek.append(rc.Uzenet(tempSor,egySor)) #1.sor=tempSor,2.sor=egySor
    
    sorszam+=1

f.close()


print("2.feladat:")
print("Az első üzenet rögzítője:{}".format(uzenetek[0].amator))
print("Az utolsó üzenet rögzítője:{}".format(uzenetek[-1].amator))

print("\n3.feladat:")
for egyUzenet in uzenetek:
    if egyUzenet.farkasKereso():
        print("{}. nap, {}. rádióamatőr".format(egyUzenet.nap,egyUzenet.amator))

napok = []

while len(napok) < 11:
    tempNap = rc.Nap(len(napok)+1)
    for egyUzenet in uzenetek:
        if egyUzenet.nap == len(napok)+1:
            tempNap.hozzaAd(egyUzenet)
    napok.append(tempNap)



'''másik megoldás, számlálós ciklussal
napok=[]

for i in range(1,12):
    tempNap = rc.Nap(i)
    for egyUzenet in uzenetek:
        if egyUzenet.nap == i:
            tempNap.hozzaAd(egyUzenet)
'''
print("4. feladat")
for egyNap in napok:
    print("{}.nap {} rádióamatőr".format(egyNap.nap,egyNap.uzenetSzam()))
    # másképp: print(f"{egyNap.nap}.nap {egyNap.uzenetSzam()} rádióamatőr")


f = open("adaas.txt","w")
for uzenet in napok:
    f.write(uzenet.helyreAllit())
f.close()

print("7.feladat:")
napSzam = int(input("Adja meg a nap sorszámát:"))
amatorSzam = int(input("Adja meg a rádióamatőr sorszámát:"))


keresett = napok[napSzam-1].amatorSzama(amatorSzam) 

if not keresett:
    print("Nincs ilyen feljegyzés")
else:
    print("A megfigyelt egyedek szama: {}".format(keresett.kifejlett+keresett.kojok))
