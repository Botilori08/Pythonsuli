sorok = 0
oszlopok = 0
while sorok == 0:
            sorok = int(input("Sorok száma: "))

while oszlopok == 0:
            oszlopok = int(input("Oszlopok száma: "))

karakter = ""
while karakter == "":
        karakter = input("Kérek 1 karaktert: ")
        if karakter != 1:
            print("Nem megfelelő méret!")
            karakter = input("Kérek 1 karaktert: ")
        else:
                break
                
        
print((oszlopok*karakter+"\n")*sorok)


                