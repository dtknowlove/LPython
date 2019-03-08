import math
# print(abs(-22))

# for x in range(1,11):
# 	print(x)
# help(abs)

def tabs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('参数类型错误，仅限整型、浮点型！')
	if x>=0:
		return x
	else:
		return -x
print(tabs(1))

print(math.sin(1))

def move(x,y,step,angle=0):
	rx=x+step*math.cos(angle)
	ry=y-step*math.sin(angle)
	return rx,ry
x,y=move(100,100,60,math.pi/6)
k=move(100,100,60,math.pi/6)
print(x,y,k)


def quadratic(a,b,c):
	der=b*b-4*a*c
	x1=(-b+math.sqrt(der))/(2*a)
	x2=(-b-math.sqrt(der))/(2*a)
	return x1,x2
print(quadratic(-1,3,1))

def Power(x,m=2):
	s=1
	while m>0:
		s*=x
		m-=1
	return s
print(Power(2,10))

def AddEnd(l=None):
	if l==None:
		l=[]
	l.append('End')
	return l
print(AddEnd([1,2,3]))
print(AddEnd())

def CalcNumsPower(*number):
	s=0
	for n in number:
		s+=Power(n)
	return s
# print(CalcNumsPower((1,2,3,4)))
# print(CalcNumsPower([1,2,3,4]))
print(CalcNumsPower(1,2,3))
print(CalcNumsPower())

kk=[1,2,3,4,5]
print(CalcNumsPower(*kk))


