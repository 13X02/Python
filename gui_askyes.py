from tkinter import *
from tkinter import messagebox

def ok():
    if messagebox.askokcancel(title="Confirmation",message="Do You want to contiue"):
        print("You want to contiue")
    else:
        print("You dont want to continue")


window= Tk()
button = Button(window,text="Continue",command=ok)
button.pack()
window.mainloop()