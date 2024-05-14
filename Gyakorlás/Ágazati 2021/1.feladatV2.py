print("1.feladat")
elsoBekert = input("Kérem az első szöveget: ")
masodikBekert = input("Kérem a második szöveget: ")
szam = 0
while szam == 0:
    try:
        szam = int(input("Kérek egy egész számot:"))
    except:
        print("Ez nem egész szám!")

if len(elsoBekert) > len(masodikBekert):
    print("Az első szám nagyobb!")
    print((elsoBekert+"\n")*szam)
elif len(elsoBekert) == len(masodikBekert):
    print("A két szám egyenlő!")
    print((elsoBekert+"\n")*szam)
else:
    print("A második szám nagyobb!")
    print((masodikBekert+"\n")*szam)

