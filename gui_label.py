from tkinter import *
from PIL import ImageTk, Image

window = Tk()

photo = ImageTk.PhotoImage(Image.open("person.jpeg"))

label = Label(window,
              text="Sample label",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
#label.place(x=0,y=0)

window.mainloop()