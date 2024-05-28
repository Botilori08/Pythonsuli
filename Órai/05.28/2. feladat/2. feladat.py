from modul import *


darabszam = szam()
szamLista = []
while True:
    szamLista.append(keplet())
    if len(szamLista) == darabszam:
        break
print(szamLista)
