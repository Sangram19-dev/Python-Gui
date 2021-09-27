from tkinter import  *
from random import sample

App = Tk()
App.title("Checkbox in Element Picker")
App.geometry('350x250')
#grid system for placing our element properly
#row0  column0
#row1 column1

inp = Entry(App)#for asking input from user
inp.grid(row=0, column = 0, columnspan =2, padx = 20, pady = 5) #grid it in the project

no_choice=IntVar()
chk= Checkbutton(App, text='Double', variable=no_choice,onvalue=2,offvalue=1)
chk.deselect()
chk.grid(row=1,column=0,columnspan=2,padx=25,pady=5)

def pick(): #define function for show the input
    INP = (inp.get()).split(',')#get the user input
    #fit check box confition
    if no_choice.get()==2:
        chois='Choice:'+str(sample(INP,2))
    else:
        chois='Choice:' + str(sample(INP,1))
    #chois = 'Choice: ' = str(choice(INP))
    #Here we will change the output appreance with relief parameter, relief can be raise or flat
    msg = Label(App, text =chois, relief='raised', width=15,borderwidth=4) #store it in msg var
    msg.grid(row = 0,column=2 ,padx = 20, pady = 5, columnspan=2)
    if quit['state'] == DISABLED:
        quit['state'] = NORMAL



#cancel button will eneble when there will be some input or else disabled
B= Button(App,text="Show",command=pick ) #add button, when user click it get the result
B.grid(row=2,column=0 ,padx = 20, pady = 5)

quit = Button(App,text = 'Cancel',command = App.quit, state= DISABLED,borderwidth=5) #create a close button using quit function
quit.grid(row=2,column=1,padx = 20, pady = 5)
App.mainloop()#execution