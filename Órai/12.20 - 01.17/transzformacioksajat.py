
import math

def eltol(pontok,x,y):
    if isinstance(pontok[0], list):
        for i in range(len(pontok)):
            pontok[i]=eltol(pontok[i],x,y)
    else:
        for i in range(0,len(pontok),2):
            pontok[i]+=x
            pontok[i+1]+=y
    return pontok
#nagyitas
def nagyit(pontok,x,y=-1):
    if isinstance(pontok[0], list):
            for i in range(len(pontok)):
                    pontok[i]=forgat(pontok[i],x,y)
    else: 
        if y==-1:
            print(y) 
            for i in range(len(pontok)):
                pontok[i]*=x
        else:
            for i in range(len(pontok)):
                if i %2==0:
                    pontok[i]*=x
                else:
                    pontok[i]*=y
        
    return pontok
	
#forgatas fuggveny
#x'= cos αx − sin αy
#y' = sin αx + cos αy
def forgatPont(x,y,szog):
    x2=math.cos(math.radians(szog))*x - math.sin(math.radians(szog))*y
    y2=math.sin(math.radians(szog))*x + math.cos(math.radians(szog))*y
	
    return x2,y2

def forgat(lista,szog,oX="",oY=""):
    if oX=="" and oY=="":
        oX,oY=kozepSzamol(lista)
    elif oX=="" or oY=="":
        return lista
    

    if isinstance(lista[0], list):
          for i in range(len(lista)):
                lista[i]=forgat(lista[i],szog,oX,oY)
    else: 
        lista=eltol(lista,-oX,-oY)
        
        for i in range(0,len(lista),2):
            lista[i],lista[i+1]=forgatPont(lista[i],lista[i+1],szog)
        
        lista=eltol(lista,-oX,-oY)
	
    return lista

def kozepSzamol(lista):
    if isinstance(lista[0], list):
            uj = []
            for i in range(len(lista)):
                x,y=kozepSzamol(lista[i])
                uj.append(x)
                uj.append(y)
        
            x,y=kozepSzamol(uj[i])
    else: 
        x = 0
        y = 0
        for i in range(len(lista)):
            if i%2==0:
                x +=lista[i]
            else:
                y +=lista[i]

            x=x/ len(lista)/2
            y=y/ len(lista)*2
        
    return x,y


if __name__ == '__name__':   
      print("rendesen elinditva")
#else:
#      print("Modulként betöltve") 



