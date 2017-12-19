import re,os
from package_filehelper import FileHelper,NetworkHelper


keywords=input('输入要关键字:')
pages=10
url='https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&ct=201326592&ic=0&lm=-1&width=&height=&v=flip'%keywords

for i in range(pages):	
	pic_dir=os.getcwd()+'/../Cache/picture/p%d'%i
	FileHelper.GetPathIfNoCreateDir(pic_dir)
	resUrl = re.sub("ic=\d","ic=%d"%i,url)
	print(resUrl)
	NetworkHelper.Dowload(resUrl,'"objURL":"(.*?)"',pic_dir)


