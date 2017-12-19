# import re
# import webbrowser
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

# html='''
# <div id="test1">content1</div>
# <div id="test2">content2</div>
# <div id="test3">content3</div>
# '''

# selector = etree.HTML(html)
# print(etree.tostring(selector,pretty_print=True))
# content=selector.xpath('//div/text()')
# for each in content:
# 	print(each)

html1='''
<div id="class">Hello,
    <font color=red>my</font>
    world!
<div>
'''
selector=etree.HTML(html1)
# print(etree.tostring(selector,pretty_print=True))
tmp=selector.xpath('//div[@id="class"]')
for e in tmp:
	print(e.xpath('string(.)'))
# info = tmp.xpath('string(.)')
# content2 = info.replace('\n','')
# print(content2)

