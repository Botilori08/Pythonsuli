def haromszog():
    lista = []
    while lista == []:
        try:
            szam1 = int(input("Kérem a(z) 1. egész szamot! "))
            lista.append(szam1)
        except:
            print("Ez nem egész szám!")
    while len(lista) < 2:
        try:
            szam2 = int(input("Kérem a(z) 2. egész szamot! "))
            lista.append(szam2)
        except:
            print("Ez nem egész szám!")

    while len(lista) < 3:
        try:
            szam3 = int(input("Kérem a(z) 3. egész szamot! "))
            lista.append(szam2)
        except:
            print("Ez nem egész szám!")

    return print(lista)

def haromHaromszog():
    adatsor1 = []
    adatsor2 = []
    adatsor3 = []
    if adatsor1 == []:
        haromszog()
        
    return adatsor1
