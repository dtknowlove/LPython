import re
import webbrowser
from lxml import etree

# text='<a herf = "www.baidu.com">....<a herf = "www.google.com">'
# urls=re.findall('<a herf = "(.*?)">',text,re.S)
# for each in urls:
# 	print(each)
# 	webbrowser.open("http://"+each,2,True)


# html = '''
# <html>
# <title>爬虫的lallal基本知识</title>
# <body>
# ……
# </body>
# </html>
# '''
# print(re.search('<title>(.*?)</title>',html,re.S).group(1))

# pages='http://tieba.baidu.com/p/4342201077?pn=1'
# for i in range(10):
# 	url=re.sub('pn=\d',"pn=%d"%i,pages)
# 	print(url)
# 	webbrowser.open_new(url)

html='''
<div id="test1">content1</div>
<div id="test2">content2</div>
<div id="test3">content3</div>
'''
selector=etree.XML('<a><b>Haegar</b></a>')#etree.HTML(html)
content = selector.xpath("hello('Dr. Falken')")#'//div[re:match(start-with(@id,"test"))]/text()')
print(content)
# for each in content:
#     print(each)