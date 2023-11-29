import random
import math 

def homersekletek(cname):
    for i in range(24):
        i = random.randint(20,37)
        lista.append(i)
    print(cname + " mai hőmérséklet adatok óránként: ",lista)

varosok=["Debrecen","Sopron","Budapest","Szeged","Kaposvár","Kilépés"]

for i,elem in enumerate(varosok):
    print("\t"+str(i+1)+":",elem,sep="")



varosId = "alma"
while varosId == "alma" or varosId not in range(len(varosok)+1):
    try:
        varosId = int(input("Válaszd ki a kívánt várost! "))
        if varosId not in range(len(varosok)+1):
            raise
    except:
        print("Válassz a listából!")

while varosId==1:
    try:
        lista=[]
        Debrecen=[]
        homersekletek("debreceni")
        if varosId in range(len(varosok)+1):
            break
    except:
        print("Válassz a listából!")

        
while varosId==2:
    try:
        lista=[]
        Sopron=[]
        homersekletek("soproni")
        if varosId in range(len(varosok)+1):
            break
    except:
        print("Válassz a listából!")

while varosId==3:
    try:
        lista=[]
        Budapest=[]
        homersekletek("budapesti")
        if varosId in range(len(varosok)+1):
            break
    except:
        print("Válassz a listából!")


while varosId==4:
    try:
        lista=[]
        Szeged=[]
        homersekletek("szegedi")
        if varosId in range(len(varosok)+1):
            break
    except:
        print("Válassz a listából!")

while varosId==5:
    try:
        lista=[]
        Kaposvár=[]
        homersekletek("kaposvári")
        if varosId in range(len(varosok)+1):
            break 
    except:
        print("Válassz a listából!")

if varosId==6:
    quit()
