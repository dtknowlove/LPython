from tkinter import *
from tkinter.messagebox import showinfo

class MyGUI(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self,parent)
		button=Button(self,text='click',command=self.replay)
		button.pack()
	def replay(self):
		showinfo(title='popup',message='Button clicked!')

if __name__ == '__main__':
	window=MyGUI()
	window.pack()
	window.mainloop()