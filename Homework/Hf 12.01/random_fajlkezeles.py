import random 
import math


randomszam= math.floor(random.random()*1)*500+1000



print(randomszam)

f = open("Random.txt","a")
f.write(randomszam)
f.close()
f = open("Random.txt", "r")
print(f.read())
