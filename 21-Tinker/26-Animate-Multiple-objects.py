from tkinter import *
import time


class Ball:

    def __init__(self, canvas, x,y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,  diameter, diameter, fill = color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
    
    def move(self):
        coordinates = self.canvas.coords(self.image)

        if(coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0):
            self.xVelocity = -self.xVelocity
        
        if(coordinates[3] >= (self.canvas.winfo_width()) or coordinates[1] < 0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)



window = Tk()
window.geometry("+1500+300")

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0,0, 100, 1,1, "white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()