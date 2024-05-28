def dupla():
    szam = 0
    while szam == 0:
        try:
            szam = int(input("Adj meg egy számot!: "))
        except:
            print("Ez nem egész szám!")
    return szam*2

print("Az általad megadott szám duplája: {}".format(dupla()))