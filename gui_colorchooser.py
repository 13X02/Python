from tkinter import *
from tkinter import colorchooser
def click():
    color = colorchooser.askcolor()
    color_code = color[1]
    window.config(bg=color_code)

window =Tk()

window.geometry("720x480")
button = Button(window,command=click,text="Change Background")
button.pack()

window.mainloop()