from tkinter import *
from tkinter.messagebox import showinfo
from tkinter002 import MyGUI

class CustomGUI(MyGUI):
	def replay(self):
		showinfo(title='弹窗',message='我是一个弹窗')
if __name__ == '__main__':
	CustomGUI().pack()
	mainloop()