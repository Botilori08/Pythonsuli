print("1.feladat")

elsoSzo = input("Kérem az első szöveget: ")
masodikSzo = input("Kérem a második szöveget: ")

szam = 0
while szam == 0:
    try:
        szam = int(input("Kérek egy egész számot: "))
    except:
        print("Ez nem egész szám!")

if elsoSzo > masodikSzo:
    print("Az első hosszabb!")
    print(szam*(elsoSzo+"\n"))
elif masodikSzo > elsoSzo:
    print("A második hosszabb!")
    print(szam*(masodikSzo+"\n"))
else:
    print("Egyenlő hosszúak!")
    print(szam*(elsoSzo+"\n"))

