from functools import reduce

DIGITS={'0':0 , '1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(c):
		return DIGITS[c]
	return reduce(fn,map(char2num,s))
print(str2int("129999"))


def normalize(name):
	return name[0].upper()+name[1:].lower()

names=["maliYa",'aaMiiKKK',"ELeeE"]

print(list(map(normalize,names)))

def str2float(s):
	li=s.split('.')
	def fn2point(n):
		a=1
		for num in range(1,len(n)+1):
			a=a*10
		return str2int(n)/a
	return str2int(li[0])+fn2point(li[1])

print(str2float('123.456'))