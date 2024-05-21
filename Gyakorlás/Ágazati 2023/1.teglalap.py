sorok = 0
oszlopok = 0
while sorok == 0:
        try:
            sorok = int(input("Sorok száma: "))
        except:
              print("Nem megfelelő!")
while oszlopok == 0:
        try:
            oszlopok = int(input("Oszlopok száma: "))
        except:
              print("Nem megfelelő!") 

karakter = ""
while karakter == "":
      karakter = input("Kérek 1 karaktert: ")
      if len(karakter) > 1:
            try: