szamok = []
while szamok == [] or bekert > 0 : 
    bekert= int(input("Írj be számokat! "))
    szamok.append(bekert)
    if bekert ==0:
        break

print(szamok)

ujszamok = str(szamok)

f = open("szamok.txt","w")
f.write(ujszamok)
f.close()