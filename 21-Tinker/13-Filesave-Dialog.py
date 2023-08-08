from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\babak\\Python For Everyone\\21-Tinker-01",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


window = Tk()
window.geometry("420x420+1500+300")

button = Button(window, text = 'Save', command=save_file)
button.pack()

text = Text(window,
            bg = "light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            fg = 'purple',
            padx=20,
            pady=20)
text.pack()


window.mainloop()