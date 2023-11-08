import random

mgh = ["a", "á","e", "é", "i", "í","o", "ó","ö","ő","u","ú","ü","ű"]
msh = ["b", "c", "d","dz","dzs","f", "g", "gy","h","j","k","l","ly","m","n","ny","p", "q","r","s","sz","t","ty","v","w","x","y","z","zs"]

choose = []
valasztas = ["0", "1"]

while len(choose)< 5:
    i = random.choice(msh+mgh)
    if i not in choose:
        choose.append(i)
print(choose)
print("#"*80)
while len(choose)< 5:
    i = random.choice(valasztas)
    if i == "0":
        y = random.choice(mgh)
        choose.append(y)
        y = random.choice(msh)
        choose.append(y)
        y = random.choice(mgh)
        choose.append(y)
        y = random.choice(msh)
        choose.append(y)
        y = random.choice(mgh)
        choose.append(y)
    else:
        y = random.choice(msh)
        choose.append(y)
        y = random.choice(mgh)
        choose.append(y)
        y = random.choice(msh)
        choose.append(y)
        y = random.choice(mgh)
        choose.append(y)
        y = random.choice(msh)
        choose.append(y)
        
print(choose)
