f = open("laktatkft.txt",encoding="utf8")
sorok = []
for egySor in f:
    sorok.append(egySor.strip().split(";"))

dolgozok = 0
budapestiBerek = []
for i in range(len(sorok)):
    szuletesEv = int(sorok[i][3].split("-")[0])
    sorok[i][4] = int(sorok[i][4])
    if 2024- szuletesEv > 30:
        dolgozok += 1
    if sorok[i][1] == 'Budapest':
        budapestiBerek.append(sorok[i][4])
print("30 évesnél idősebb dolgozók száma: {} fő".format(dolgozok))
osszBer = 0
for egyBer in budapestiBerek:
    osszBer += egyBer

print("A budapesti dologozók átlagbére: {} Ft".format(round(osszBer/len(budapestiBerek))))
