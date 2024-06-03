lista = []
szo = "alma"
while szo != "":
    szo = input("Kérek egy szót: ")
    if szo != "":
        lista.append(szo)

print("A szavak száma: {}".format(len(lista)))

listaFele = lista[:len(lista)//2]

print("A lista első fele: {}".format("_".join(listaFele)))
