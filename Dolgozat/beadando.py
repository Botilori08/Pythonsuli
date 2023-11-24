import random

def szamok():
    x = 0
    y = 0 
    for k in szamlista:
        if k %2== 0:
            x = x + 1
        if k %2 != 0:
            y = y + 1
    print("Páratlan számok száma: ",y)
    print("Páros számok száma: ",x)
    
def paratlanOsszeadas():
    paratlan = []
    for d in szamlista:
        if d %2!= 0:
           paratlan.append(d)
           paratlanosszeg = sum(paratlan)
    print("Páratlan számok összege: ",paratlanosszeg)
    



szamlista = []
paratlan = []
for i in range(500):
    i = random.randint(10000,99999)
    szamlista.append(i)

print(szamlista)

print("#"*80)
szamok()
print("#"*80)
paratlanOsszeadas()


