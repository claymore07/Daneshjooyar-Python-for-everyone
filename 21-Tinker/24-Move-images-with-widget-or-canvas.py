#------------move widgets on window-------------
# from tkinter import *

# def move_up(event):
#     label.place(x = label.winfo_x(), y = label.winfo_y() - 10)
# def move_down(event):
#     label.place(x = label.winfo_x(), y = label.winfo_y() + 10)
# def move_left(event):
#     label.place(x = label.winfo_x() - 10, y = label.winfo_y())
# def move_right(event):
#     label.place(x = label.winfo_x() + 10, y = label.winfo_y())


# window = Tk()
# window.geometry("+1500+300")

# window.bind("<w>", move_up)
# window.bind("<a>", move_left)
# window.bind("<s>", move_down)
# window.bind("<d>", move_right)
# window.bind("<Up>", move_up)
# window.bind("<Left>", move_left)
# window.bind("<Down>", move_down)
# window.bind("<Right>", move_right)


# my_image = PhotoImage(file="racecar.png")
# label = Label(window, image=my_image)
# label.place(x = 0, y = 0)


# window.mainloop()

#-------------move images on canvas-------------

from tkinter import *

def move_up(event):
    canvas.move(my_image, 0, -10)
def move_down(event):
    canvas.move(my_image, 0, 10)
def move_left(event):
    canvas.move(my_image, -10, 0)
def move_right(event):
    canvas.move(my_image, 10, 0)


window = Tk()
window.geometry("+1500+300")


window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)


canvas = Canvas(window, width=500, height=500)
canvas.pack()


photoimage = PhotoImage(file="racecar.png")

my_image = canvas.create_image(0,0, image = photoimage, anchor = NW)



window.mainloop()