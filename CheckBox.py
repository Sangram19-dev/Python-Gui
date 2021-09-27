from tkinter import  *
from random import choice

App = Tk()
App.title("CheckBox")
App.geometry('350x250')

check = StringVar()#Store integer values
#create checkbox
chk = Checkbutton(App, text='Checkbox', variable=check, onvalue='yes', offvalue='Nope')
chk.deselect()
chk.pack()

def show():
    msg=Label(App, text=check.get())
    msg.pack()

B = Button(App, text='show', command=show )
B.pack()
App.mainloop()#execution