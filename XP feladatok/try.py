szamok = []
bekert="alma"

while bekert!=" ":
    bekert= input("Írj be szamokat! ").split(",")
    if bekert != " ":
        szamok.append(bekert)
                      
print(szamok)

    