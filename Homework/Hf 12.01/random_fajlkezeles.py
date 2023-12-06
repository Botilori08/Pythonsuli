import random 
import math


randomszam= []
for i in range(500):
    i = random.randrange(1000,100001)
    randomszam.append(i)

#print(randomszam)
szoveg= str(randomszam)
print(szoveg)


f = open("Random.txt","a")
f.write(szoveg)
f.close()

