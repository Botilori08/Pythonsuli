print("1.feladat")
szo = "valami"
lista = []
szoLista = ['barack','alma','körte','szőlő','dinnye','ananász','eper']
while szo != "":
    szo = input("Kérek egy szót!: ")
    if szo != "":
        lista.append(szo)
if len(lista) > 0:
    print("A szavak száma: {}".format(len(lista)))
else:
    print("A szavak száma: {}".format(len(szoLista)))

print("A lista első fele: {}".format("_".join(lista[:len(lista)//2])))

