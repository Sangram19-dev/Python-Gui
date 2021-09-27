from tkinter import  *
from random import choice

App = Tk()
App.title("User Input")
App.geometry('350x350')

inp = Entry(App)#for asking input from user
inp.pack() #pack it in the project

def show(): #define function for show the input
    INP = inp.get() #get the user input
    msg = Label(App, text =INP) #store it in msg var
    msg.pack()

B= Button(App,text="Show",command=show ) #add button, when user click it get the result
B.pack()

App.mainloop()#execution