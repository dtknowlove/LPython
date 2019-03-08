from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from_addr='dtknowlove@qq.com'#//input('From:')
password='herylhyhgknxbifd'#input('Password:')
to_addr='liuzhenhua@putao.com'#'2457089542@qq.com'#input('TO:')
smtp_server='smtp.qq.com'#input('SMTP server:')

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

content='<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p><p><img src="cid:0"></p></body></html>'
# content='hello,send by python...'
msg=MIMEMultipart()
msg.attach(MIMEText(content,'html','utf-8'))
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To'] = _format_addr("管理员<%s>"%to_addr)
msg['Subject']=Header("来自SMTP的问候...",'utf-8').encode()

with open('./file1.ico','rb') as f:
	mime=MIMEBase('image','ico',filename='file1.ico')
	mime.add_header('Content-Disposition', 'attachment', filename='file1.ico')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)


import smtplib
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.starttls()
server.login(from_addr,password)
# for x in range(1,10):
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
