from tkinter import *
from tkinter.messagebox import showinfo
def replay():
	showinfo(title='popup',message='Button pressed!')
window=Tk()
label=Label(window,text='Spam')
label.pack()
button=Button(window,text='click',command=replay)
button.pack()
window.mainloop()