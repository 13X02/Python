from tkinter import *
from tkinter import messagebox

def error():
    messagebox.showerror(title="ERROR",message="An Error Occured")



window= Tk()
button = Button(window,text="Submit",command=error)
button.pack()
window.mainloop()