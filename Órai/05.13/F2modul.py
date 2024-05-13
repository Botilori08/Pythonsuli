def haromszog(lista):
    while lista == []:
        try:
            elsoSzam = int(input("Kérem a(z) 1. egész szamot! "))
            lista.append(elsoSzam)
        except:
            print("Ez nem egész szám!")
    while len(lista) < 2:
        try:
            masodikSzam = int(input("Kérem a(z) 2. egész szamot! "))
            lista.append(masodikSzam)
        except:
            print("Ez nem egész szám!")
    while len(lista) < 3:
        try:
            harmadikSzam = int(input("Kérem a(z) 3. egész szamot! "))
            lista.append(harmadikSzam)
        except:
            print("Ez nem egész szám!")

    return lista

def haromHaromszog():
    adatsor1 = []
    adatsor2 = []
    adatsor3 = []
    print("1.adatsor")
    while adatsor1 == []:
        haromszog(adatsor1)
        if len(adatsor1) < 4:
            break
    print("2.adatsor")
    while adatsor2 == []:
        haromszog(adatsor2)
        if len(adatsor2) < 4:
            break
    print("3.adatsor")
    while adatsor3 == []:
        haromszog(adatsor3)
        if len(adatsor3) < 4:
            break
    return print(adatsor1), print(adatsor2),print(adatsor3)
