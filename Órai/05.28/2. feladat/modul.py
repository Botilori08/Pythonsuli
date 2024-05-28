import math
def szam():
    elsoSzam = int(input("1.szam: "))
    masodikSzam = int(input("2.szam: "))
    harmadikSzam = int(input("3.szam: "))
    eredmeny = elsoSzam +masodikSzam+harmadikSzam
    return eredmeny

def keplet(x):
    keplet = (math.sqrt(42*x*3+12)+25*x)/(2*(13-26))*4*x/6
    return keplet
    
