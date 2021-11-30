from tkinter import *

food =["Shawai", "Alfham","Mandi"]

window = Tk()

x =IntVar()
label = Label(window,
              text="Which food do you like",
              font=('Impact',60,'bold'),
              fg='orange',
              bd=10,
              bg="white",
              padx=20,
              pady=20,
              compound='top')
label.pack()

for index in range(len(food)):
    radiobutton=Radiobutton(window,variable =x,value=index,text=food[index],font=("Impact",50),compound='bottom',padx=20,fg="cyan",bg="white")
    radiobutton.pack()

window.mainloop()
