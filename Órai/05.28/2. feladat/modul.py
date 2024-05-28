import math
def szam():
    elsoSzam = int(input("1.szam: "))
    masodikSzam = int(input("2.szam: "))
    harmadikSzam = int(input("3.szam: "))
    eredmeny = elsoSzam +masodikSzam+harmadikSzam
    return eredmeny

def keplet():
    keplet = (math.sqrt(42*szam()**3+12)+25*szam())/(2*(13-26))*4*szam()/6
    return keplet
    
