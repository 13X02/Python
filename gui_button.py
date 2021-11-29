from tkinter import *
from tkinter import font
#can add image with photoimage function i didnt add since somehow image is not supported since my chip is m1
count = 0
def click():
    global count 
    count += 1
    print("clicked ",count," times")

window = Tk()

button = Button(window,text ="Sample Button",command =click,font=("Arial",50),fg="black",bg="white",activebackground="green",activeforeground="red")
button.pack()
window.mainloop()
