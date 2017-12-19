import re,requests

def Dowload(url,pattern,picDir):
	html=requests.get(url).text
	pic_url=re.findall(pattern,html,re.S)

	print("===========>>>>>>>Start Download...")
	i = 0
	for each in pic_url:
		print(each)
		try:
			pic=requests.get(each,timeout=10)
		except requests.exceptions.ConnectionError:
			print('[错误：图片无法下载]')
			continue
		fileName=picDir+'/pictures_'+str(i)+'.jpg'	
		fp=open(fileName,'wb')
		fp.write(pic.content)
		fp.close()
		i += 1
	print("===========>>>>>>>End")