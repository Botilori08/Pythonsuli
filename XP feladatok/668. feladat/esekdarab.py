szoveg = ""
lista = []
esek = []
while szoveg == "":
    szoveg = input("Kérek egy szöveget!: ")
    lista = szoveg.split(" ")

    for egySzo in lista:
        if egySzo == "és" or egySzo == "És" :
            esek.append(egySzo)

if len(esek) > 0:
    print("A megadott szövegben {} db 'és' szó van".format(len(esek)))
else:
    print("A megadott szövegben nincs 'és' szó")