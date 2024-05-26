def haromszog(lista):
    lista = []
    while len(lista)<3:
        try:
            bekert = int(input("Kérem a(z) {}. egész szamot! ".format(len(lista)+1)))
            lista.append(bekert)
            if len(lista) == 3:
                break
        except:
            print("Ez nem egész szám!")

    return lista

def haromHaromszog():
    adatsor = []
    adatsor1 = []
    adatsor2 = []
    adatsor3 = []
    adatsorSzama = 0
    while len(adatsor) < 3:
        print("{}.adatsor".format(adatsorSzama +1))
        adatsor.append(haromszog(adatsor1))
        print("{}.adatsor".format(adatsorSzama +2))
        adatsor.append(haromszog(adatsor2))
        print("{}.adatsor".format(adatsorSzama +3))
        adatsor.append(haromszog(adatsor3))
        if len(adatsor) == 3 :
            break
    print("\t a={}, b={}, c={}".format(adatsor[0][0],adatsor[0][1],adatsor[0][2]))
    print("\t a={}, b={}, c={}".format(adatsor[1][0],adatsor[1][1],adatsor[1][2]))
    print("\t a={}, b={}, c={}".format(adatsor[2][0],adatsor[2][1],adatsor[2][2]))

    return adatsor

def oldalvizsgalo(lista):
    lista.sort()
    for i in range(len(lista)):
        if lista[i][0] + lista[i][1] > lista[i][-1] and lista[i][0] + lista[i][1] > lista[i][-1]:
        

