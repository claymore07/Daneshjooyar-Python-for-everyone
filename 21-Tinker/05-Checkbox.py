from tkinter import *

def display():
    if(x.get() == 1):
        print("You agreed!")
    else:
        print("You didn't agree :(")

window = Tk()
window.geometry("940x320+1500+300")

x = IntVar() # BooleanVar, StringVar

python_photo = PhotoImage(file="python.png")

check_button = Checkbutton(window,
                           text = "I agree to something!",
                           variable=x,
                           command=display,
                           onvalue=1,
                           offvalue=0,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg = "black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,
                           pady=15,
                           image=python_photo,
                           compound=LEFT)

check_button.pack()

window.mainloop()