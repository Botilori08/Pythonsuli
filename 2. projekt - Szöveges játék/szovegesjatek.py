#függvény definiálása
def menu(lista):
    for i,elem in enumerate(lista):
        print("{}: {}".format(i+1,elem))
        
    valasztas=0
    while (valasztas < 1 or valasztas > len(lista)) and valasztas!=69:
        try:
            valasztas= int(input("Válassz! "))
        except:
            pass
        
    return valasztas-1

lista = ["előre", "hátra", "jobbra", "balra" ]

#print("\n".join(lista))

#kiválasztott kiíratása

#valasz=menu(lista)
#print(valasz,lista[valasz])

tortenet=[
        [
            1,#szál ID
            "Reggel felébredtem. Mit tegyek?",#szoveg
            ["fogmosás", "reggeli", "öltözés"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            2,#szál ID
            "Elmegyek fogat mosni. Sikálom rendesen, ahogy kell!",#szoveg
            ["fogmosás", "reggeli", "öltözés"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            3,#szál ID
            "Kellene valamit enni! Anya csinált valamit? Nézzük meg!",#szoveg
            ["fogmosás", "reggeli", "öltözés"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            4,#szál ID
            "Kissé hűvös van, kellene valami ruha! \nFelveszek egy nadrágot, meg egy pólót.",#szoveg
            ["fogmosás", "reggeli", "öltözés", "66-os parancs"],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            66,#szál ID
            "Vége mindennek...",#szoveg
            [],#választási lehetőségek
            [] #hova ugorjon
        ]
    ]

szalId=1
while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #másként   
    temp=[e[0] for e in tortenet]
    szalIndex= temp.index(szalId)

    print(tortenet[szalIndex][1])
    if tortenet[szalIndex][2]==[]
        break
    
    menuPont=menu(tortenet[szalIndex][2])

    if menuPont == 68:
        break

    szalId=tortenet[szalIndex][3][menuPont]

print("The End")
