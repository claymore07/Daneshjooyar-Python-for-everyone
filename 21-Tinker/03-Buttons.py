# buttons = you click it, then it does stuff
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(f"You have CLICKED the button {count} times")

window = Tk()
window.geometry("640x640+1500+300")

photo = PhotoImage(file='thumbsup.png')

button = Button(window, 
                text="Click Me!",
                command=click,
                font = ("Times New Roman", 30),
                fg="#00FF00",
                bg="black",
                activeforeground= "#00FF00",
                activebackground='black',
                state=ACTIVE,#DISABLED
                image=photo,
                compound=BOTTOM)

button.pack()

window.mainloop()