from tkinter import *

App=Tk()

sld_v =IntVar()
#orient for orientation(by defouly vertical but we  can make it horizontal)
sld = Scale(App, from_=0, to=100, variable=sld_v, orient=HORIZONTAL)
sld.pack()
def show():
    msg = Label(App, text=sld_v.get())
    msg.pack()

B = Button(App,text='show', command=show)
B.pack()
App=mainloop()