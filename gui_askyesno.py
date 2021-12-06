from tkinter import *
from tkinter import messagebox

def ok():
    if messagebox.askyesno(title="Confirmation",message="Yes /No"):#there are some more messagebox items similar to this too lazy to try :)
        print("Yes")
    else:
        print("No")


window= Tk()
button = Button(window,text="Continue",command=ok)
button.pack()
window.mainloop()