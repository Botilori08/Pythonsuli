import modul


darabszam = modul.szam()
print(darabszam)
szamLista = []
while len(szamLista) < darabszam:
    szamLista.append(modul.keplet(modul.szam()))
    if len(szamLista) == darabszam:
        break

print(szamLista)
