import transzformaciok
from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("1200x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti 

#fenyo2=[200,0,
#        0,100,
#        150,100,
#        0,200,
#        150,200,
#        0,300,
#        150,300,
#        150,400,
#        250,400,
#        250,300,
#        400,300,
#        250,200,
#        400,200,
#        250,100,
#        400,100,
#        200,0]


#fenyo2masolat = transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(fenyo2masolat,width=30, fill="darkgreen")
Lorant =[ [140,0,100,300,300,300,300,270,130,270,170,0,140,0], #L
                [400,270,470,200,400,130,330,200,400,270],#O ekezet
                [400,70,420,30,440,30,420,70,400,70], #O belső
                [400,300,500,200,400,100,300,200,400,300,], #O Külsö
                [520,100,520,300,550,300,550,230,590,300,620,300,580,230,620,230,620,100,520,100],#R külső
                [550,140,590,140,590,200,550,200,550,140],#R belső
                [660,300,710,100,770,100,820,300,790,300,770,250,710,250,690,300,660,300],#A külső
                [730,130,710,220,770,220,750,130,730,130],#A belső
                [730,70,740,30,760,30,750,70,730,70],#A ékezet
                [850,100,850,300,880,300,880,190,920,300,950,300,950,100,920,100,920,190,880,100,850,100],#N 
                [980,100,1080,100,1080,130,1045,130,1045,300,1015,300,1015,130,980,130,980,100]#T


        ]


hatter= "ffffff"
betuSzinek = ["blue",hatter,"blue"]


Lori2 = [Lorant]
#for e in Lori2:
#    e = transzformaciok.eltol(e,0,0)
#    e = transzformaciok.nagyit(e,1)
#    e= transzformaciok.forgat(e,45)

#    Lori2.append(e)
#print(Lori2)
#for e in Lori2:
#    canvas.create_line(e,width=5,fill="blue")

#Lori2 = transzformaciok.masol(Lorant)

#Lori2 = transzformaciok.forgat(Lori2,90)
#Lori2 = transzformaciok.nagyit(Lori2,1)   
#Lori2 = transzformaciok.eltol(Lori2,0,0)

#for e in Lori2: 
#    canvas.create_line(e,width=5,fill="red")


#canvas.create_line(nevO,width=5, fill="blue")
#canvas.create_line(nevL,width=5, fill="blue")
#canvas.create_line(nevR,width=5, fill="blue")
#canvas.create_line(nevRbelso,width=5, fill="blue")
#canvas.create_line(nevOBelso,width=5, fill="blue")
#canvas.create_line(nevOekezet,width=5, fill="blue")
#canvas.create_line(nevA,width=5, fill="blue")
#canvas.create_line(nevAbelso,width=5, fill="blue")
#canvas.create_line(nevAekezet,width=5, fill="blue")
#canvas.create_line(nevN,width=5, fill="blue")
#canvas.create_line(nevT,width=5, fill="blue")


#win.mainloop()

while True:
        canvas.delete("all")
        Lori2 = transzformaciok.forgat(Lori2,0.1)
        for i,e in enumerate(Lori2):
                d = canvas.create_line(Lori2,fill='blue', width="5")
        
        win.update_idletasks()
        win.update()
