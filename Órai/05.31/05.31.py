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
Ujszam = bekero()
while Ujszam >= 0:
    szamok.append(Ujszam)
    if szam < 0:
        break


    

print(szamok)
