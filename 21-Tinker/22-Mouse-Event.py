from tkinter import *

def do_something(event):
    print("Mouse Coordinates: " + str(event.x) + ", " + str(event.y))

window = Tk()
window.geometry("+1500+300")

window.bind("<Button-1>",do_something) #left mouse click
# window.bind("<Button-2>",do_something) #scroll wheel
# window.bind("<Button-3>",do_something) #right mouse click
# window.bind("<ButtonRelease>",do_something)#mousebutton release
# window.bind("<Enter>",do_something) #enter the window
# window.bind("<Leave>",do_something) #leave the window
# window.bind("<Motion>",do_something) #Where the mouse moved


window.mainloop()