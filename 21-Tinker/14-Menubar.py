from tkinter import *

def openFile():
    print("Open file has been selected")

def saveFile():
    print("Save file has been selected")

def quit():
    print("Quit has been selected")

window = Tk()
window.geometry("420x420+1500+300")

openImage = PhotoImage(file='file.png')
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu = menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open", command=openFile, image=openImage, compound=LEFT)
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Edit")
editMenu.add_command(label="Cut")
editMenu.add_command(label="Paste")

window.mainloop()