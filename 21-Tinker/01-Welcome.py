from tkinter import *

window = Tk()
window.geometry("420x420")

window.title("Python For Everyone")

icon = PhotoImage(file = 'logo.png')
window.iconphoto(True, icon)
window.config(background = "#5cfcff")

window.mainloop()