from person import Person
class Manager(Person):
	#overwrite
	def giveRaise(self, percent,bonus=0.1):
		self.pay*=(1+percent+bonus)
		return self.pay
if __name__ == '__main__':
	tom=Manager('Tom Done',50,50000)
	print(tom.lastName())
	print(tom.giveRaise(0.2))
