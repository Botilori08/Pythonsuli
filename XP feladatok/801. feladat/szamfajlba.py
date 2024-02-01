szamok = []
while szamok == [] or bekert > 0 : 
    bekert= int(input("Írj be egy számot! "))
    szamok.append(bekert)
    if bekert ==0:
        break

print(szamok)

ujszamok = str(szamok)

f = open("adat.txt","w")
f.write(ujszamok)
f.close()