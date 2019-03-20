import shelve
from person import Person
from manager import Manager

qdz=Person('秦 小胖',27,11000,'UIDesigner')
dtknowlove=Person('刘 壮士',27,12500,'Unity Programer')
tom=Manager('Tom Done',50,50000)

db=shelve.open('class-shelve')
db['qdz']=qdz
db['dtknowlove']=dtknowlove
db['tom']=tom;
db.close()