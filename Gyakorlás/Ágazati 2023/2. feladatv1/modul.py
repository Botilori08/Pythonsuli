def kor():
    lista = []
    x = int(input("X koordináta: "))
    lista.append(x)
    y = int(input("Y koordináta: "))
    lista.append(y)
    r = int(input("Sugár: "))
    lista.append(r)

    return lista

def viszony(lista1,lista2):
    pass




# r1: az első kör sugara
# r2: a második kör sugara
# d: a középpontok távolsága
# két kör érinti egymást, ha a sugaruk összege megegyezik a középpontjaik távolságával
# visszatérési értéke: logikai
def erint(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]==temp[2]
# két kör nem érinti és nem is metszi egymást, ha a sugaraik és távolságuk közül a két kisebb összege kisebb, mint a harmadik
# a körök lehetnek kívül, vagy belül is
# visszatérési értéke: logikai
def nemErint(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]<temp[2]
# két kör metszi egymást, ha a sugaraik és távolságuk közül a két kisebb összege nagyobb, mint a harmadik
# a körök lehetnek kívül, vagy belül is
# visszatérési értéke: logikai
def metsz(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]>temp[2]
# rendezi az adatokat, hogy megtudjuk melyik a leghosszabb
# visszatérési értéke: rendezett lista
def listaKeszit(r1,r2,d):
    temp=[r1,r2,d]
    temp.sort()
    return temp


