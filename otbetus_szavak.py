import random

mgh = ["a", "á","e", "é", "i", "í","o", "ó","ö","ő","u","ú","ü","ű"]
msh = ["b", "c", "d","dz","dzs","f", "g", "gy","h","j","k","l","ly","m","n","ny","p", "q","r","s","sz","t","ty","v","w","x","y","z","zs"]

choose = []

while len(choose)<= 4:
    i = random.choice(msh)
    if i not in choose:
        choose.append(i)
    print(choose)
    
