qdz={'name':'秦 小胖','age':27,'pay':11000,'job':'UIDesigner'}
dtknowlove={'name':'刘 壮士','age':27,'pay':12500,'job':"Unity Programer"}
db={}
db['qdz']=qdz
db['dtknowlove']=dtknowlove

print(__name__)
if __name__ == '__main__':
	for key in db:
		print(key,'=>\n',db[key])
