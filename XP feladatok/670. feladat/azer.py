szoLista = []
szoveg = input("Kérek egy mondatot!: ")

szoLista.append(szoveg.split())
for egySzo in szoLista:
    print("".join(egySzo).strip())


