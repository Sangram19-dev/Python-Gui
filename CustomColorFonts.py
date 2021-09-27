from tkinter import  *
from random import choice

App = Tk()
App.title("Grid System")
App.geometry('350x250')
App['background']= 'white'
#grid system for placing our element properly
#row0  column0
#row1 column1

inp = Entry(App,background= 'grey', foreground='black')#for asking input from user
inp.grid(row=0, column = 0, columnspan =2, padx = 20, pady = 5) #grid it in the project

def pick(): #define function for show the input
    INP = (inp.get()).split(',')#get the user input
    #chois = 'Choice: ' = str(choice(INP))
    msg = Label(App, text =choice(INP), font =('Courier',12), background = 'black', foreground='yellow') #store it in msg var
    msg.grid(row = 0,column=2 ,padx = 20, pady = 5)
    if quit['state'] == DISABLED:
        quit['state'] = NORMAL



#cancel button will eneble when there will be some input or else disabled
B= Button(App,text="Show",command=pick ) #add button, when user click it get the result
B.grid(row=1,column=0 ,padx = 20, pady = 5)

quit = Button(App,text = 'Cancel',command = App.quit, state= DISABLED, background='red', foreground='white') #create a close button using quit function
quit.grid(row=1,column=1,padx = 20, pady = 5)
App.mainloop()#execution