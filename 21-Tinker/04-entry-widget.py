# entry widget = textbox that accepts a single line of users input
from tkinter import *


def submit():
    username = entry.get()
    print(f"Hello {username}")

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1 , END)

window = Tk()
window.geometry("940x320+1500+300")

# Entry Widget
entry = Entry(window,
              font=("Arial", 40),
              fg = "#00FF00",
              bg = "black")

#entry.config(show = "*")
#entry.insert(0, 'SpongeBob')

entry.pack(side = LEFT)

# Submit Button
submit_button = Button(window, 
                       text = 'submit',
                       font=('Times New Roman', 20),
                       command= submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window, 
                       text = 'delete',
                       font=('Times New Roman', 20),
                       command=delete)

delete_button.pack(side = RIGHT)

backspace_button = Button(window, 
                       text = 'backspace',
                       font=('Times New Roman', 20),
                       command=backspace)

backspace_button.pack(side = RIGHT)



window.mainloop()