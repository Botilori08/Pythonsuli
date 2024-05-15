lista = [3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]
letraMezo = [10,20,30,40]
indulo = 0
letraMezoszam = 0
mezokRalepett = []

print("2.feladat")
for egySzam in lista:
    indulo += egySzam
    mezokRalepett.append(indulo)
    if indulo in letraMezo:
        indulo = indulo-3
        letraMezoszam += 1

print(*mezokRalepett,sep=", ")

print("3.feladat")
print("A játék során {} alkalommal lépett létrára.".format(letraMezoszam))

print("4.feladat")
if mezokRalepett[-1] >= 45:
    print("A játékot befejezte.")
else:
    print("A játékot abbahagyta.")
