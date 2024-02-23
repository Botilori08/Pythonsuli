#Áramkör projekt
#2024.02.16.

import math
class jel:
	x = 0
	y = 0
	meret = 100
	
	szin = "black"

	def __init__(self, x, y, meret, canvas):
		self.x = x
		self.y = y
		self.meret = meret
		self.canvas = canvas
		self.r = self.meret * 0.06
		self.rajz()


	def rajz(self, vonalak = [], korok = []):
		self.canvas.create_rectangle(self.x, self.y, self.x + self.meret, self.y + self.meret, fill = "gray")

		for egyVonal in vonalak:
			self.canvas.create_line(egyVonal, width = self.meret * 0.03, fill = self.szin)	
			
		for egyKor in korok:
		    self.canvas.create_oval(egyKor, outline = self.szin, width= self.meret*0.03)

class elem(jel):
	def rajz(self):
		vonalak = [
			[
				self.x, self.y + self.meret * 0.5,
				self.x + self.meret * 0.45, self.y + self.meret * 0.5,
			],
			[
				self.x + self.meret * 0.45, self.y + self.meret * 0.2,
				self.x + self.meret * 0.45, self.y + self.meret * 0.8,
			],
			[
				self.x + self.meret * 0.55, self.y + self.meret * 0.4,
				self.x + self.meret * 0.55, self.y + self.meret * 0.6,
			],
			[
				self.x + self.meret * 0.55, self.y + self.meret * 0.5,
				self.x + self.meret * 1.00, self.y + self.meret * 0.5,
			],
		]
		jel.rajz(self, vonalak)
		
class kapcsolo(jel):
	def rajz(self):
		vonalak = [
			[
				self.x, self.y + self.meret * 0.5,
				self.x + self.meret * 0.333 - self.r, self.y + self.meret * 0.5,
			],
			[
				self.x + self.meret * 0.333 + self.r, self.y + self.meret * 0.5,
				self.x + self.meret * 0.666 - self.r, self.y + self.meret * 0.3,
			],
			[
				self.x + self.meret * 0.666 + self.r, self.y + self.meret * 0.5,
				self.x + self.meret * 1.00, self.y + self.meret * 0.5,
			],
		]
		
		korok= [
			[
				self.x+self.meret*0.333-self.r,	self.y+self.meret*0.5-self.r,
				self.x + self.meret*0.333 + self.r,	self.y+ self.meret*0.5 + self.r
			],
			[
				self.x+self.meret*0.666-self.r,	self.y+self.meret*0.5-self.r,
				self.x + self.meret*0.666 + self.r,	self.y+ self.meret*0.5 + self.r
			],
        ]
		
		jel.rajz(self, vonalak,korok)

class lampa(jel):
	def rajz(self):
		dx = self.r/math.sqrt(2)

		vonalak = [
			[
				self.x, 	self.y + self.meret * 0.5,
				self.x + self.meret * 0.5 - self.r,	 	self.y + self.meret * 0.5,
			],
			[
				self.x + self.meret * 0.5 - dx,		self.y + self.meret * 0.5-dx,
				self.x + self.meret * 0.5 + dx ,	 self.y + self.meret*0.5 + dx,
			],
			[
				self.x + self.meret * 0.5 - dx,		self.y + self.meret * 0.5 + dx,
				self.x + self.meret * 0.5 + dx ,	 self.y + self.meret*0.5 - dx,
			],
			[
				self.x + self.meret * 0.5 + self.r,	self.y + self.meret * 0.5,
				self.x + self.meret * 1.00 + dx , self.y + self.meret *0.5,
			],

		]
		
		korok= [
			[
				self.x+self.meret*0.333-self.r,	self.y+self.meret*0.5-self.r,
				self.x + self.meret*0.333 + self.r,	self.y+ self.meret*0.5 + self.r
			],
			[
				self.x+self.meret*0.666-self.r,	self.y+self.meret*0.5-self.r,
				self.x + self.meret*0.666 + self.r,	self.y+ self.meret*0.5 + self.r
			],
        ]
		jel.rajz(self,vonalak,korok)
from tkinter import *

win = Tk()
win.geometry("600x620+100+20")
win.title("Áramkör")
canvas = Canvas(win, bg="white")
print(canvas)


canvas.pack(fill=BOTH, expand= 1)


elem1 = elem(0,0,100,canvas)
#elem1.rajz()

elem2 = elem(200,100,50,canvas)
#elem2.rajz()

kapcsolo1 = kapcsolo(350, 150, 100, canvas)
lampa1 = lampa(0, 150, 100, canvas)

win.mainloop()