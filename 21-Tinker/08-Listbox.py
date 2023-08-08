from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered:")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
    

window = Tk()
window.geometry("+1500+300")


listbox = Listbox(window,
                  bg='#f7ffde',
                  font = ('Constantia', 35),
                  width=12,
                  selectmode=MULTIPLE)

listbox.pack()
listbox.insert(1, 'Pizza')
listbox.insert(2, 'Pasta')
listbox.insert(3, 'Garlic Bread')
listbox.insert(4, 'Soup')
listbox.insert(5, 'Salad')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submit_button = Button(frame, text = "submit", command=submit)
submit_button.pack(side=LEFT)

add_button = Button(frame, text = "add", command=add)
add_button.pack(side=LEFT)

delete_button = Button(frame, text = "delete", command=delete)
delete_button.pack(side=LEFT)


window.mainloop()