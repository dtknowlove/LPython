classmate=["a","b","c"]
line=0;
def clprint():
	print('==>>>>>%d:'%line,len(classmate))
def cprint():
	print('==>>>>>%d:'%line,classmate)
def ciprint(index):
	print('==>>>>>%d:'%line,classmate[index])

clprint()
cprint()
ciprint(0)
ciprint(-1)
classmate.append('e')
ciprint(-1)
classmate.insert(3,'d')
cprint()
classmate.pop()
cprint()

classmate=[]
cprint()
clprint()

t=(1,)
print(t)