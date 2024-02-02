bekertszam = int(input("Írj be egy számot! "))



if bekertszam %2 == 0:
    print("A szám osztható 2-vel")
else:
    print("A szám nem osztható kettővel! ")

if bekertszam %3 == 0:
    print("A szám osztható 3-mal")
else: 
    print("A szám nem oszható hárommal")

if bekertszam %3 !=0 and bekertszam %2 != 0:
    print("A szám sem 2-vel sem 3-mal nem osztható")

if bekertszam %3 ==0 and bekertszam %2 == 0: 
    print("A szám 2-vel is, és hárommal is osztható")
