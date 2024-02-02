elsoSzam = int(input("Írj be egy számot! "))
masodikSzam = int(input("Írj be mégegy számot! "))


if elsoSzam > masodikSzam:
    elsoeredmeny = elsoSzam / masodikSzam
    print(elsoeredmeny)

if masodikSzam > elsoSzam:
    masodikeredmeny = masodikSzam / elsoSzam
    eredmenyszoveg = "A masodik szám és az első szám hányadosa: {masodikeredmeny}"

    print(eredmenyszoveg.format(masodikeredmeny))