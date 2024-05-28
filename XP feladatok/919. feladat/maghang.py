

def mghSzamlalo():
    maganHangzok = ["a","á","A","Á","e","é","E","É","i","í","I","Í","o","ó","O","Ó","ö","ő","Ö","Ő","u","ú","U","Ú","ü","ű","Ü","Ű"]
    szo = input("Kérek egy szöveget!: ")
    mghSzam = 0
    for egyBetu in szo:
        for egyKarakter in maganHangzok:
            if egyBetu == egyKarakter:
                mghSzam += 1  
    if mghSzam == 0   :
        return "A megadott szövegben nincs magánhangzó!"
    else:
        return "A megadott szövegben {} db magánhangzó van".format(mghSzam)
    
print(mghSzamlalo())
