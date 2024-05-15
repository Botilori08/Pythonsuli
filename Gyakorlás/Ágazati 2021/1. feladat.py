print("1. feladat:")
bekertSzoveg = input("Kérek egy szöveget: ")
bekertSzam = 0
while bekertSzam == 0:
    try:
        bekertSzam = int(input("Kérek egy számot: "))
    except:
        print("Ez nem egész szám!")

if bekertSzam > len(bekertSzoveg):
    print("Sajnos nincs ilyen betű.")
else:
    betuk = 4*bekertSzoveg[bekertSzam]
    print(betuk)