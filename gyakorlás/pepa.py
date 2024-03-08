pepalista =[]
f = open("pepa.txt")
while len(pepalista) < 10000 :
    pepalista.append("pepa")
    if len(pepalista) == 10000:
        break
    print(pepalista)
f.write(pepalista)