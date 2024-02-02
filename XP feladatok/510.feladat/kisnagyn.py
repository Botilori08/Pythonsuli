szamlista = []
while szamlista == [] or bekert > 0 : 
    bekert= int(input("Írj be egy számot! "))
    szamlista.append(bekert)
    if bekert ==0:
        break

szamok = []
for e in szamlista:
    szamok.append(e)
szamok.sort()
legkisebb = szamok[0]
legnagyobb = szamok[-1]
print("A legkisebb szám:",szamok[0])
print("A legnagyobb szám:",szamok[-1])