# Label = an area widget that holds text and/or an image within the window
from tkinter import *
from PIL import ImageTk, Image

window = Tk()

# get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# set the dimensions of the screen 
width=500
height=500

# calculate position x and y coordinates
x = (screen_width/1.5) - (width/2)
y = (screen_height/1.5) - (height/2)



# set the position of the window's top left corner
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
# window.geometry("640x640")
photo = PhotoImage(file = 'computer.png')
#photo = ImageTk.PhotoImage(Image.open("computer.jpg"))

label = Label(window, 
              text = "Hello World!",
              font = ('Times New Roman', 40, 'bold'),
              fg = '#00FF00',
              bg = "blue",
              bd = 10,
              padx = 20,
              pady = 50,
              image = photo,
              compound = LEFT)
label.pack()
#label.place(x = 100, y = 300)


window.mainloop()