szavak = []
sorszam = 1
elozo = ""
lefutasok = 0
while len(szavak) < 20:
            szo = input("Kérem a(z) {}. szót! ".format(sorszam))
            sorszam += 1
            szavak.append(szo)
            if len(szo) > 6:
                    print("A karakterek száma téves!")
            if lefutasok != 0:
                if (szavak[-1])[-1] == szo[0]:
                        print("Nem illeszkedett!")
    
