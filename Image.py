from tkinter import *
from PIL import Image,ImageTk # pip install pillow
app=Tk()
#it will change the icon of the app
app.iconbitmap#(use the ico file,file location

img = Image.open((r'res\python.png'))#mention the path here where image is stored
lbl=Label(app,image=ImageTk.PhotoImage(img))
lbl.pack()
app.mainloop()