from NASAClass import *

adatok = []
f = open("NASAlog.txt")
for egySor in f:
    adatok.append(Nasa(egySor))

print(len(adatok))
f.close()