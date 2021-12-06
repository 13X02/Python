from tkinter import *
from tkinter import messagebox

def ok():
    answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    if(answer == 'yes'):
        print('I like pie too :)')
    else:
        print('Why do you not like pie? :(')


window= Tk()
button = Button(window,text="Submit",command=ok)
button.pack()
window.mainloop()