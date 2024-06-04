def bekero():
    szoLista = []
    szo = ""
    while szo != "vége":
        szo = input("Kérek egy szót: ")
        if len(szo) <= 12:
            szoLista.append(szo)
        else:
            print("Túl hosszú!")
    szoLista.pop(-1)
    return szoLista

lista = bekero()

betuszam = 0
for egySzo in lista:
    betuszam += len(egySzo)

paratlanok = []
parosok = []
for egyElem in lista:
    if len(egyElem) %2 == 0:
        parosok.append(egyElem)
    else:
        paratlanok.append(egyElem)

if len(paratlanok) > len(parosok):
    print("Páratlan hosszúságú szóból van több!")
elif len(parosok) > len(paratlanok):
    print("Páros hosszúságú szavakból van több!")
else:
    print("A páros és páratlan hosszú szavak darabszáma egyenlő!")

lista.sort()
szoSzam = 0
for egySzo in lista:
    if len(egySzo) == 6:
        print("ABC rendben az első hatbetű szó: {}".format(egySzo))
        break
    else:
        szoSzam += 1
    
    if szoSzam == len(lista):
        print("Nincs hatbetűs szó!")

print("Megadott szavak betűinek száma: {}".format(betuszam))


