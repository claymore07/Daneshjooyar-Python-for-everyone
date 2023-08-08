from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

window = Tk()
window.geometry("420x420+1500+300")

button = Button(text='Click Me', command=click)
button.pack()

window.mainloop()