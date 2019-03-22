class Person:
	def __init__(self, name,age,pay=0,job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay*=(1+percent)
		return self.pay
	def __str__(self):
		return '<%s => %s: %s、%s、%s>' % (self.__class__.__name__,self.name,self.age,self.pay,self.job)

if __name__ == '__main__':
	qdz=Person('秦 小胖',27,11000,'UIDesigner')
	dtknowlove=Person('刘 壮士',27,12500,'Unity Programer')
	print(qdz.name,dtknowlove.pay)
	print(qdz)

	print(qdz.lastName())
	print(dtknowlove.giveRaise(0.2))