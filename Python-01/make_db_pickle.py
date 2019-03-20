from initdata import db
import pickle
dbfile=open('people-file','wb')
pickle.dump(db,dbfile)
dbfile.close()