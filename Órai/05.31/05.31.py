
def bekero():
    global szam
    szam = 0
    while szam == 0:
        try:
            szam = int(input("Kérek egy számot!: "))
        except:
            print("Ez nem egész szám!")
    return szam


szamok = []
while True:
    Ujszam = bekero()
    if Ujszam >= 0:
        szamok.append(Ujszam)
    else:
        break

f = open("szamok.txt","w")
for egySzam in szamok:
    f.write(str(egySzam) + "\n")
f.close()
f = open("szamok.txt")
szamLista = []
for egySzam in f:
    szamLista.append(int(egySzam))
f.close()
osszeg = 0
for egyElem in szamLista:
    osszeg += egyElem


atlag = osszeg/len(szamLista)
atlagFeletti = 0
for egySzam in szamLista:
    if egySzam > atlag:
        egySzam += atlagFeletti
print(atlagFeletti)




