from tkinter import  *
from random import randint

App = Tk()
App.title("Random Generator")
App.geometry('350x350') #increase decrese size of the window

#Display = Label(App, text= "Application Window") #add text
#Display.pack()
#adding buttons in app
def show_msg():
    msg = Label(App, text = randint(1,100) )
    msg.pack()
a= Button(App, text="Generate", command = show_msg )
a.pack()
App.mainloop()#execution