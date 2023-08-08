from tkinter import *
import time


WIDTH = 500
HEIGHT = 400
xVelocity = 2.5
yVelocity = 1.75


window = Tk()
window.geometry("+1500+300")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file="space.png")
background = canvas.create_image(0,0, image = background_photo, anchor = NW)

photo_image = PhotoImage(file="ufo.png")
my_image = canvas.create_image(0,0, image = photo_image, anchor = NW)


image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    # print(coordinates)
    if(coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if(coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()