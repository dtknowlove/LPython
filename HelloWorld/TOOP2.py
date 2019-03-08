class Employee():
	'员工基类'
	EmployeeCount=0
	def __init__(self, name,salary):
		super(Employee, self).__init__()
		self.name = name
		self.salary = salary
		Employee.EmployeeCount+=1
	def DisplayCount(self):
		print("Total employee count is:%d"%Employee.EmployeeCount)
	def ToString(self):
		print("Name:%s Salary:%d"%(self.name,self.salary))

e1=Employee("Jack",2000)
e2=Employee("Mike",3000)

e1.ToString()
e2.ToString()
e1.DisplayCount()
print(Employee.__doc__)
		