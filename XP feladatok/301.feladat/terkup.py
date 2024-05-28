from math import *
#V=1/3*r**2*pi*h

r = int(input("Mennyi legyen az alap sugara?: "))
h = int(input("Mennyi legyen a kúp magassága?: "))
V = (1/3)*r**2*pi*h
print("Az általad megadott adatokhoz tartozó körkúp térfogata: {} cm3".format(round(V,2)))
