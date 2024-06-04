from medveModul import *

def haromMedve():
    medvek = []
    while len(medvek) < 3:
        medvek.append(medve())

    return medvek

lista = haromMedve()
def korVizsgalo(lista):
    for i in range(len(lista)):
        if lista[i][1] > 25:
            return "Öreg"
        else:
            return "Nem öreg"

        

print(korVizsgalo(lista))

#medve()
