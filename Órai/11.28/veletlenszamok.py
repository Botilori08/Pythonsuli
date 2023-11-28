import random 
import math 

def veletlen(mettol, meddig,lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol

    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam
    


print(veletlen(10,20))
print("#"*80)
#Adjunk hozzá egy listához 100 random számot 
szamok= []
for i in range(100):
        szamok.append(veletlen(10,20))

print(szamok)

#készítsünk egy olyan listát, ami véletlenszerű darabszámú listát tartalmaz
#Ezek a listák tartalmazzanak 10,20 darabszámú emberi testmagasságot 

print("#"*80)
lista=[]
random1=veletlen(10,21)
for k in range(random1):
	random2=veletlen(10,21)
	magassaglista=[]
	for _ in range (random2):
		magassaglista.append(veletlen(160,201))
	lista.append(magassaglista)

print(lista)


