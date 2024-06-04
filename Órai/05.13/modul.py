def haromszog():
    lista = []
    while len(lista) < 3:
        try:
            szam = int(input("Kérem a(z) {} egész szamot!".format(len(lista)+1)))
            lista.append(szam)
        except:
            print("Ez nem egész szám!")
    return lista