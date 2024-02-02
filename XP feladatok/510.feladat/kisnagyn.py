szamok = []
while szamok == [] or bekert > 0 : 
    bekert= int(input("Írj be egy számot! "))
    szamok.append(bekert)
    if bekert ==0:
        break

novekvolista = szamok.sort()


print(novekvolista[0],novekvolista[-1:])