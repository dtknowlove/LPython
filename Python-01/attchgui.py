from tkinter import *
from tkinter002 import MyGUI

mainwin=Tk()
Label(mainwin,text=__name__).pack()

popup=Toplevel()
Label(popup,text='Attch').pack(side=LEFT)
MyGUI(popup).pack(side=RIGHT)
mainwin.mainloop()