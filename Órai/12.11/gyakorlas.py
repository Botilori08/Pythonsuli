adatok = []

f = open("cb.txt")
for sor in f: 
    adatok.append(sor.strip().split(";"))

for e in range(len(adatok)):
    adatok[e][0] = int(adatok[e][0])
    adatok[e][1] = int(adatok[e][1])
    adatok[e][2] = int(adatok[e][2])

print(adatok)
f.close()