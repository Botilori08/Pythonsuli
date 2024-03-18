from NASAClass import *

adatok = []
f = open("NASAlog.txt")
for egySor in f:
    adatok.append(Nasa(egySor))

osszeg = 0
for egyAdat in adatok:
    osszeg += egyAdat.ByteMeret()

print(osszeg)

f.close()
print("5. feladat: Kérések száma: {}".format(len(adatok)))
print("6.feladat: Válaszok összes mérete: {}")