szavak = []
sorszam = 1
lefutasok = 0
while True:
     szo = input("Kérem a(z) {}. szót! ".format(sorszam))
     sorszam += 1
     
     if len(szo) != 6:
          print("A karakterek száma téves!")
          break
     elif lefutasok != 0:
          if szavak[-1][-1] == szo[0]:
               szavak.append(szo)
          else:
               print("Nem illeszkedett") 
               break
     else:
          lefutasok += 1
          szavak.append(szo)

lepesSzam = len(szavak)
print("Helyes lépések száma: {}".format(lepesSzam))
if lepesSzam in [0,1,2]:
     print("Szint: kezdő")
elif lepesSzam in [3,4,5]:
     print("Szint: közepes")
else:
     print("Szint: haladó")
