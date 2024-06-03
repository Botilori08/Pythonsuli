from medveModul import *

def haromMedve():
    medvek = []
    while len(medvek) < 3:
        medvek.append(medve())
    
    return medvek


def korVizsgalo():
    lista = haromMedve()
    for egylista in lista:
        print(egylista)

print(korVizsgalo())

#medve()
