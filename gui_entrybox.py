from tkinter import *

def submit():
    name=entry.get() 
    print("Hey ",name ," How are you?")
    entry.config(DISABLED)#for disabling further input upon entering

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


window = Tk()

entry =Entry(window,bg="black",fg="red")#add show = "*/any symbol" for passwordss
entry.insert(0,"Enter your name")#for default text
entry.pack(side=LEFT)

submit_button = Button(window,text ="Enter",command=submit,font=("Arial", 20),bg='black',fg="red")
submit_button.pack(side=RIGHT)

delete_button = Button(window,text ="Delete",command=delete,font=("Arial", 20))
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text ="Backspace",command=backspace,font=("Arial", 20))
backspace_button.pack(side=RIGHT)

window.mainloop()