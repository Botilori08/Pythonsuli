szamok = []
while szamok == [] or bekert > 0 : 
    bekert= int(input("Írj be számokat! "))
    szamok.append(bekert)
    if bekert ==0:
        break

print(szamok)

for i in szamok:
    i = int(i)

f = open("szamok.txt","w")
f.write(i)
f.close()