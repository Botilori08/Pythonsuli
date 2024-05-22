def aSzamolo(szoveg):
    adarab = 0
    betuLista = []
    for e in szoveg:
            if e == 'a':
                adarab += 1
                return print("A megadott szóban {} darab 'a' betű van".format(adarab))
            else:
                return print("A megadott szóban nincs 'a' betű")

aSzamolo("alap")