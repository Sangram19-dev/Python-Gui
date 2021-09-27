from tkinter import  *
from random import choice

App = Tk()
App.title("Element Picker From User Input")
App.geometry('350x350')

inp = Entry(App)#for asking input from user
inp.pack() #pack it in the project

def pick(): #define function for show the input
    INP = (inp.get()).split(',') #split user input by ,
    msg = Label(App, text =choice(INP)) #store it in msg var
    msg.pack()

B= Button(App,text="Choose",command=pick ) #add button, when user click it get the result
B.pack()

App.mainloop()#execution