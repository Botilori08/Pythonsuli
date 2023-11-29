import random

#12 fő, 8-12 jegy/fő, jegy 1-5

jegyek_szama=[]
for i in range(12):
    egyDiak = []
    for k in range(random.randrange(8,13)):
        jegy = random.randrange(1,6)
        egyDiak.append(jegy)
    jegyek_szama.append(egyDiak)
    print(egyDiak)
    atlag = sum(egyDiak)/jegy
    print(atlag)
    



