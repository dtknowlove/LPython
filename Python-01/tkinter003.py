from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
	showinfo(title='Replay',message='Hello %s!'%(name))

top=Tk()
top.title('Echo')
top.iconbitmap('icon.ico')

Label(top,text='Enter your name:').pack(side=TOP)
ent=Entry(top)
ent.pack(side=TOP)
btn=Button(top,text='Submit',command=lambda: reply(ent.get()))
btn.pack(side=LEFT)
top.mainloop()