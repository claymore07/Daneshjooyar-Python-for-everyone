from tkinter import *
from PIL  import ImageTk
import sqlite3
from numpy import random
import pyglet

# conda install -c conda-forge pyglet
# conda install -c anaconda pyinstaller
## conda remove pathlib

pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

# SET Colors
bg_color = "#3d6466"

# load custom fonts


def clear_widgets(frame):
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()

def fetch_db():
    # Connect to sqlite DB
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()

    # fetch all the table names
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    # choose random table idx
    idx = random.randint(0, len(all_tables) - 1)

    # fetch records from table
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()

    return table_name, table_records

def pre_process(table_name, table_records):

    # preprocess table name
    # AlmostCheeseDanishTurnovers101134 => Almost Cheese Danish Turnover
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    # preprocess table records
    ingredients = []

    for record in table_records:
        name = record[1]
        qty = record[2]
        unit = record[3]

        ingredients.append(f"{qty} {unit} of  {name}")

    return title, ingredients





def load_frame1():
    clear_widgets(frame2)

    # stack frame 1 above frame 2
    frame1.tkraise()
    # prevent widgets from modifying the frame
    frame1.pack_propagate(False)

    # create logo widget
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
    logo_widget = Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    # create label widget for instructions
    Label(frame1,
        text="Ready for your random recipe?",
        bg=bg_color,
        fg="white",
        font=("Shanti", 14)).pack()

    # create button widget
    Button(
        frame1,
        text="SHUFFLE RECIPE",
        font=("Ubuntu", 14),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=load_frame2).pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    
    # stack frame 2 above frame 1
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    # create logo widget
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")
    logo_widget = Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    # recipe title widget
    Label(frame2,
          text=title, 
          bg=bg_color,
          fg="white",
          font=("Ubuntu", 20)).pack(padx=20, pady=20)
    
    # recipe ingredients widgets
    for ing in ingredients:
        Label(frame2,
              text=ing,
              bg="#28393a",
              fg="white",
              font=("Shanti", 12)).pack(fill="both", padx=25)

    # 'back' button widget
    Button(
        frame2,
        text="BACK",
        font=("Ubuntu", 30),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=load_frame1).pack(pady=20)

# initialize app
root = Tk()
root.geometry("+1500+300")

# create a frame widgets
frame1 = Frame(root, width=500, height=600, bg=bg_color)
frame2 = Frame(root, bg=bg_color)

# place frame widgets in window
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()

# run app
root.mainloop()