from tkinter import *

food = ['Pizza', 'Hamburger', ' Hotdog']

def order():
    if(x.get() == 0):
        print("You've ordered a Pizza!")
    elif(x.get() == 1):
        print("You've ordered a Hamburger!")
    else:
        print("You've ordered a Hotdog!")

window = Tk()
window.geometry("640x640+1500+300")


pizzaImage = PhotoImage(file="pizza.png")
hamburgerImage = PhotoImage(file="hamburger.png")
hotdogImage = PhotoImage(file="hotdog.png")

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text = food[index],
                               variable= x,
                               value= index,
                               padx = 25,
                               font=("Impact", 25),
                               image=foodImages[index],
                               compound=LEFT,
                               indicatoron=0,
                               width=375,
                               command = order)
    radio_button.pack(anchor=W)


window.mainloop()