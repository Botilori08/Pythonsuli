def medve():
    lista = []
    kor = 1
    tomeg = 1
    nev = input("A medve neve: ")
    lista.append(nev)
    while len(lista) < 3:
        try:
            kor = int(input("A medve kora: "))
            lista.append(kor)
            tomeg = int(input("A medve tomege: "))
            lista.append(tomeg)
        except:
            print("Nem megfelelő adat!")
    return lista


