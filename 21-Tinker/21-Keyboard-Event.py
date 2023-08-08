from tkinter import *

def do_something(event):
    # print("You pressed")
    label.config(text = event.keysym)


window = Tk()
window.geometry("+1500+300")

window.bind("<Key>", do_something) #w, a, s, d, Up, Down, Right, enter = Return

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()