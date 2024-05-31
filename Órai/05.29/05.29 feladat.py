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


listaFele = szamLista[:math.ceil(len(szamLista)/2)]
#print(listaFele)

pozitivdb = 0
negativdb = 0
for egyElem in listaFele:
    if egyElem > 0:
        pozitivdb += 1
    if egyElem < 0:
        negativdb += 1

if negativdb > pozitivdb:
    print("A negatív számokból több van a lista első felében.")
elif pozitivdb > negativdb:
    print("A pozitív számokból több van a lista első felében.")
else:
    print("A lista első felében a negatív és a pozitív számok darabszáma egyenlő.")

