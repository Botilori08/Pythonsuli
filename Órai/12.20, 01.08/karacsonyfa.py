#Import the required libraries 

from tkinter import *
import math

def eltol(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok
    
#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("600x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti 


pontok=[0,0 ,100, 0 ,100 ,100 , 0, 100, 0,0]

#eltolás
for i in range(0,len(pontok),2):
    pontok[i]+=200
    pontok[i+1]+=100




canvas.create_line(pontok,width=5, fill="green")
pontok=eltol(pontok,100,0)
canvas.create_line(pontok,width=5, fill="green")

fenyo1=[200,0,0,400,190,400,190,500,210,500,210,400,400,400,200,0]
pontok=eltol(fenyo1,10,10)
canvas.create_line(fenyo1,width=5, fill="green")










win.mainloop()