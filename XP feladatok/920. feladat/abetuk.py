def aSzamolo(szoveg):
    adarab = 0
    betuLista = []
    for e in szoveg:
        if e == 'a':
            adarab += 1
    if adarab == 0:
        print("A megadott szóban nincs 'a' betű")
    else:
        print("A megadott szóban {} db 'a' betű van".format(adarab))

aSzamolo("alap")