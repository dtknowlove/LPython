qdz={'name':'秦 小胖','age':27,'pay':11000,'job':'UIDesigner'}
dtknowlove={'name':'刘 壮士','age':27,'pay':12500,'job':"Unity Programer"}
people=[qdz,dtknowlove]
for persion in people:
	print(persion)

print(people[0]['name'])

for per in people:
	print(per['name'].split()[1])

pays=[per['pay'] for per in people]
print(pays)

pays=map((lambda x:x['pay']),people)
print(list(pays))

sumValue=sum([per['pay'] for per in people])
print(sumValue)

people.append(['Tom',54,25000,"Game Player"])
print(len(people))

print(people[-1][0])
