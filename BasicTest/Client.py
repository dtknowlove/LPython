import socket

class UrlData(object):
	def __init__(self, bundleID,url):
		super(UrlData, self).__init__()
		self.bundleID = bundleID
		self.url = url
	def ToString(self):
		print('BundleID:%s Url:%s'%(self.bundleID,self.url))

def GetUrlData(str):
	res = str.split(b'|')	
	urlData=UrlData(res[0],res[1])
	return urlData

def ReceiveData(sock):
	while True:
		d = sock.recv(BYTELEN)		
		if len(d)<0:
			break 
		buffer = []
		buffer.append(d)
		data = b''.join(buffer)
		length=int(data[:2])
		urlData=GetUrlData(data[3:])
		urlData.ToString()

IP='127.0.0.1'
PORT=13000
BYTELEN=128

address=(IP,PORT)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect
s.connect(address)
print('connect to server')

#receive
ReceiveData(s)

s.close()
print('close')


