
import random
import math 
def homersekletek(cname):
    for i in range(24):
        i = random.randint(20,37)
        lista.append(i)
    print(cname + " mai hőmérséklet adatok óránként: ",lista)



lista=[]
Debrecen=[]
homersekletek("debreceni")

lista=[]
Sopron=[]
homersekletek("soproni")

lista=[]
Budapest=[]
homersekletek("budapesti")

lista=[]
Szeged=[]
homersekletek("soproni")

lista=[]
Kaposvár=[]
homersekletek("kaposvári")


