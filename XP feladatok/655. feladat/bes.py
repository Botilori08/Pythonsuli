bSzam = 0
szoveg = ""
while szoveg == "":
    szoveg = input("Írj be egy szöveget! ")
    for egyBetu in szoveg:
        if egyBetu == "b" or egyBetu == "B":
            bSzam += 1

if bSzam > 0:
    print("A megadott szövegben {}db 'b' betű van".format(bSzam))
else:
    print("A megadott szövegben nincs 'b' betű")