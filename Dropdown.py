from tkinter import *

App=Tk()
menu_c= StringVar()
options=['Red','Blue','White','Yellow']
menu= OptionMenu(App,menu_c,'Red','Blue','White','Yellow')
menu.pack()
t= Toplevel() #adding more windows
t.title('output')
def show():
    msg=Label(App,text='      ', background=(menu_c.get()).lower())
    msg.pack()


B = Button(App, text='show', command=show)
B.pack()
App=mainloop()