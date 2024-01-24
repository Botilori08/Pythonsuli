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

nevL = [140,0,
        100,300,
        300,300,
        300,270,
        130,270,
        170,0,
        140,0]

nevO = [[400,300,
        500,200,
        400,100,
        300,200,
        400,300,
],
[400,270,
            470,200,
            400,130,
            330,200,
            400,270],
[400,70,
              420,30,
              440,30,
              420,70,
              400,70

              ]
]
nevR =[540,100,
         540,300,
         570,300,
         570,230,
         610,300,
         640,300,
         600,230,
         640,230,
         640,100,
         540,100]
nevRbelso = [570,140,
            610,140,
            610,200,
            570,200,
            570,140
            ]

Lori2 = []
#for e in nevO:
#    e = transzformaciok.eltol(e,0,0)
#    e = transzformaciok.nagyit(e,1)
#    e= transzformaciok.forgat(e,45)


#    Lori2.append(e)

#print(Lori2)
    

for e in Lori2:
    canvas.create_line(e,width=5,fill="blue")

Lori2 = transzformaciok.eltol(Lori2,100,100)
Lori2 = transzformaciok.nagyit(Lori2,1)
Lori2= transzformaciok.forgat(Lori2,45)   

canvas.create_line(nevL,width=5, fill="blue")
canvas.create_line(nevR,width=5, fill="blue")
canvas.create_line(nevRbelso,width=5, fill="blue")
#canvas.create_line(nevOBelso,width=10, fill="blue")
#canvas.create_line(nevOekezet,width=10, fill="blue")

win.mainloop()