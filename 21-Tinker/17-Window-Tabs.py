from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("420x420+1500+300")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True, fill=BOTH)

Label(tab1, text = "Hello, This from Tab#1", bg="yellow", width=50, height=25).pack()
Label(tab2, text="Goodbye, This is from Tab#2", bg="pink", width=50, height=25).pack()

window.mainloop()