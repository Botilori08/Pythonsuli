# Mértékegység átváltó
# Boti Lóránt 2023.10.06
# Projektfeladat

tipusok= ["Hosszúság","Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + Térfogat"]

print("#"*35)
#for elem in tipusok:
#    print(elem)

for i,elem in enumerate(tipusok):
    print("\t"+str(i+1)+":",elem,sep="")

print("\t0: Kilépés")

tipusId="alma"
while tipusId=="alma" or tipusId not in range(len(tipusok)+1): 
    try:
        tipusId=int(input("Válassz! ")) 
    except:
        print("Válassz a listából!")
