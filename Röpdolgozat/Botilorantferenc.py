
adatok = []

f= open("helsinki.txt")
for sor in f:
    adatok.append(sor.strip().split("\n"))
f.close()

print(adatok)

for elem in range(len(adatok)):
        adatok[elem][0] = int(adatok[elem][0])
        