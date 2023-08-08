#grid() = geometry manager that organizes widgets in a table-like structure in a parent widget
# column width is determined based on the width of the largest widget on the rows
from tkinter import *


window = Tk()
window.geometry("+1500+300")

titleLabel = Label(window, text="Enter Your Info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name: ", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last Name: ", bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=1, column=1)

emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window, text="Submit", padx=5).grid(row=4, column=0, columnspan=2)

window.mainloop()