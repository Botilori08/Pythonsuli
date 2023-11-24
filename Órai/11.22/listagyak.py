
def maxkeres(lista):
    legnagyobb=lista[0]
    maxIndex=0
    #elem indexének megkeresése
    #for i,elem in enumerate(lista):
    for i in range(len(lista)):
        if lista[i]>legnagyobb:
            legnagyobb=lista[i]
            maxIndex=i

    return(legnagyobb,maxIndex)


lista =[100,35,69,42,73,55,66,22,33,70,81]
legnagyobb,maxIndex = maxkeres(lista)
print(maxIndex,legnagyobb)
