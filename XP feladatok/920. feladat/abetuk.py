def aSzamolo():
    adarab = 0
    szoveg = input("Kérek egy szót!: ")
    betuLista = []
    for e in szoveg:
        if e == 'a':
                adarab += 1
    if adarab == 0:
        print("A megadott szóban nincs 'a' betű")
    else:
        print("A megadott szóban {} db 'a' betű van".format(adarab))


aSzamolo()