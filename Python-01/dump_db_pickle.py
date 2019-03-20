import pickle
dbfile=open('people-file','rb')
db = pickle.load(dbfile)
for key in db:
	print(key,'=>\n',db[key])
print(db['qdz']['name'])