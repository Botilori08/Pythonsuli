

class szorzotabla:
    def __init__(self,szam):
             self.tablasor = [szam*i for i in range(1,11)]

tablalista = []
for sorszam in range(1,11):
        tablalista.append(szorzotabla(sorszam).tablasor)

print(tablalista)

    
    
