import requests
url=b'http://www.baidu.com'
html=requests.get(url)
print(html.text)

tmp = html.content
print(tmp)

with open('baidu.html', 'wb') as f:
    f.write(tmp)