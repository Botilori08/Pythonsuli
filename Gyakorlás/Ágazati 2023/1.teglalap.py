print("1.feladat")
sorok = int(input("Sorok száma: "))
oszlopok = int(input("Oszlopok száma: "))

karakter = ""
while karakter == "":
        karakter = input("Kérek 1 karaktert: ")
        if len(karakter) != 1:
            print("Nem megfelelő méret!")
            karakter = input("Kérek 1 karaktert: ")
        else:
            break
                
        
print((oszlopok*karakter+"\n")*sorok)


                