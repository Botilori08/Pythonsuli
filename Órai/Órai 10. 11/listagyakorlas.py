

lista=[]

bekeres="menjébe"


while bekeres!="":
    bekeres=input("Írj be valamit!" )
    if bekeres!="":
        lista.append(bekeres)
    
print(lista)
utolso=lista[-3:]
utolso.sort()

lista.sort()
for e in lista:
    print(e)
    

for e in lista[:-3]:
    print(e)
    
for e in utolso:
    print(e)
