from tkinter import *
#can add image using photo = PhotoImage(file='img.png')
def display():
    if(x.get()==1):
        print("Agree")
    else:
        print("Disagree")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,text="I agree",variable=x,onvalue=1,offvalue=0,command=display,fg="#00FF11",bg='black',activebackground='black',activeforeground='#00FF11',padx=50,pady=50)
check_button.pack()


window.mainloop()