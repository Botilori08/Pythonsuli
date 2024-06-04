from modul import *


def haromharomszog():
    adatsor = []
    while len(adatsor) < 3:
        print("{}.adatsor".format(len(adatsor)+1))
        adatsor.append(haromszog())

    for i in range(len(adatsor)):
        print("a={}, b={}, c={}".format(adatsor[i][0],adatsor[i][1],adatsor[i][2]))
    return adatsor

def oldalvizsgalo(lista):
    print(lista.sort())
    for i in range(len(lista)):
        if lista[i][0] + lista[i][1] > lista[i][2]:
            return True
        elif lista[i][2] + lista[i][1] > lista[i][0]:
            return True
        

Adatok = haromharomszog()

print(oldalvizsgalo(Adatok))