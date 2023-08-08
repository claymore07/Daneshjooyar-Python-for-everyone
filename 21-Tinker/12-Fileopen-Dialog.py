from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(title="Open file okay?",
                                          initialdir="C:\\Users\\babak\\Python For Everyone\\21-Tinker-01",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()
window.geometry("420x420+1500+300")

button = Button(text='Open', command=openFile)
button.pack()


window.mainloop()