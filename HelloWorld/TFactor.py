age=20
if age>18:
	print('adult')
elif age>16:
	print('teenager')
else:
	print('kid')
	
li=[]
if li:
	print('true')
else:
	print('false')

names=['aa','bb','cc']
result=''
for name in names:
	result += name+" "
print(result)

print(list(range(6)))

sum=0;
for x in range(1,101):
	sum+=x
print(sum)

n=99
sumJ=0;
while n>0:
	sumJ+=n;
	n -=2;
print(sumJ)
	