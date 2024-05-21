szavak = []
sorszam = 1
elozo = ""

while szavak == []:
    if sorszam == 2:
        szo= input("Kérem az {}. szót! ".format(sorszam))
        elozo = szo
        szavak.append(szo)
        sorszam += 1
    else:
        elozo= input("Kérem az {}. szót! ".format(sorszam))
        print("számting")