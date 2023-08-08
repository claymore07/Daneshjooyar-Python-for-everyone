from tkinter import *

def submit():
    input = text.get("2.0", END)
    print(input)

window = Tk()
window.geometry("420x420+1500+300")

text = Text(window,
            bg = "light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            fg = 'purple',
            padx=20,
            pady=20)

text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()