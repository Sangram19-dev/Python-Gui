from tkinter import  *

App=Tk()

choice = StringVar()
rb1 = Radiobutton(App, text='Option 1', variable=choice, value='RB1 selected')
rb2= Radiobutton(App, text='Option 2', variable=choice,value='RB2 selected')
rb1.deselect()
rb2.deselect()
rb1.pack()
rb2.pack()

def show():
    msg = Label(App, text=choice.get())
    msg.pack()

B=Button(App, text='show', command=show)
B.pack()

App.mainloop()