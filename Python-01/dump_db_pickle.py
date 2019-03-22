import pickle
dbfile=open('people-file','rb')
db = pickle.load(dbfile)
dbfile.close()
for key in db:
	print(key,'=>\n',db[key])
print(db['qdz']['name'])