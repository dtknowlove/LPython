import pickle
dbfile=open('people-file','rb')
db=pickle.load(dbfile)
dbfile.close()

db['qdz']['pay'] *=1.1
db['dtknowlove']['name']='pickle pickle'

dbfile=open('people-file','wb')
pickle.dump(db,dbfile)
dbfile.close()