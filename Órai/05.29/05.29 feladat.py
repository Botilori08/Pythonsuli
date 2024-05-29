import math
szam = 1
szamLista = []

while szam != 0:
    szam = int(input("Kérek egy számot: "))
    if szam != 0:
        szamLista.append(szam)
#print(szamLista)

pozitiv = 0
negativ = 0
for egySzam in szamLista:
    if egySzam < 0:
        negativ += egySzam
    else:
        pozitiv += egySzam
print("A pozitív számok összege: {}".format(pozitiv))
print("A negatív számok összege: {}".format(negativ))

if abs(negativ) > abs(pozitiv):
    print("A negatív számok összege távolabb van nullától!")
elif abs(pozitiv) > abs(negativ) :
    print("A pozitív számok összege távolabb van nullától!")
else:
    print("A pozitív és negatív számok nullától számított távolsága egyenlő!")

listaFele = szamLista[math.floor(:len(szamLista)/2)]

print(listaFele)
