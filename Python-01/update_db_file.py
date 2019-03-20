from make_db_file import loadDbase,storeDbase
db=loadDbase()
db['qdz']['pay']*=1.1
db['dtknowlove']['name']="kick kick"
storeDbase(db)