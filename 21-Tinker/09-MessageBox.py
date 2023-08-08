from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("+1500+300")

def click():
    messagebox.showinfo(title="This is an info message box", message="You are person")
    # messagebox.showwarning(title='WARNING!', message="You have a VIRUS!!")
    # messagebox.showerror(title="ERROR!", message="Something went wrong:(")

    # if messagebox.askokcancel(title="Ask ok cancel", message="Do you want to do the thing?"):
    #     print('You did a thing!')
    # else:
    #     print("You canceled a thing !(")

    # if messagebox.askretrycancel(title="Ask ok cancel", message="Do you want to do the thing?"):
    #     print('You did a thing!')
    # else:
    #     print("You canceled a thing !(")

    # answer = messagebox.askquestion(title="Ask question", message="Do you like pie?")
    # if answer == 'yes':
    #     print('You did a thing!')
    # else:
    #     print("You canceled a thing !(")

    # answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question')
    # if answer == True:
    #     print("You like to code :)")
    # elif answer == False:
    #     print("Then why are you watching a video on coding?")
    # else:
    #     print("You have dodged the question!")

button = Button(window,
                text='Click Me!',
                command=click,
                font=("Times New Roman", 30),
                fg="#00FF00",
                bg="black",
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE, #DISABLED
                compound='bottom')
button.pack()

window.mainloop()