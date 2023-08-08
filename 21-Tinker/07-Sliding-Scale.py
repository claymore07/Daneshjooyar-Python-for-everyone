from tkinter import *

def submit():
    print(f"The Temperature is {scale.get()} degrees C")


window = Tk()
window.geometry("640x640+1500+300")

flameImage = PhotoImage(file='flame.png')
flameLabel = Label(image=flameImage)
flameLabel.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,
              font = ('Consolas', 20),
              tickinterval = 10,
              showvalue=0,
              troughcolor= '#69EAFF',
              fg='#FF1C00',
              bg='#111111')

scale.pack()


snowflakeImage = PhotoImage(file='snowflake.png')
snowflakeLabel = Label(image=snowflakeImage)
snowflakeLabel.pack()

button = Button(window, text='Submit', command=submit)


button.pack()

window.mainloop()