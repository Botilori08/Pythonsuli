
adatok=[]

f = open("helsinki.txt")
for sor in f:
    adatok.append(sor.strip().split(" "))

for i in range(len(adatok)):
    adatok[i][0] = int(adatok[i][0])
    adatok[i][1] = int(adatok[i][1])
f.close()

print(adatok)
