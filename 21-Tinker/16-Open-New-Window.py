from tkinter import *

def create_window():
    new_window = Tk()       #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                            #Tk() = new independent window
    #old_window.destroy()   #close out of old window

old_window = Tk()
old_window.geometry("420x420+1500+300")

Button(old_window, text="Create New Window", font=("Times New Roman", 25), command=create_window).pack()


old_window.mainloop()