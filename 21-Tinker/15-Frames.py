from tkinter import *


window = Tk()
window.geometry("420x420+1500+300")

frame = Frame(window, bg="pink", bd=5, relief=RAISED)
frame.pack()

Button(frame, text = "W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(frame, text = "A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text = "S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text = "D", font=("Consolas", 25), width=3).pack(side=LEFT)




window.mainloop()