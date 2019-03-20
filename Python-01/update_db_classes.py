import shelve
db =shelve.open('class-shelve')

qdz=db['qdz']
qdz.giveRaise(0.2)
db['qdz']=qdz

dtknowlove=db['dtknowlove']
dtknowlove.giveRaise(0.3)
db['dtknowlove']=dtknowlove

db.close()