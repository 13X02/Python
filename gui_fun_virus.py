from tkinter import *
from tkinter import messagebox

def click():
    while(False):#turn this into true and execute to work
        messagebox.showwarning(title="Warning!!!",message="You cant close me")


window = Tk()

button = Button(window,command=click)
button.pack()

window.mainloop()
