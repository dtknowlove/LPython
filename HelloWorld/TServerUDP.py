import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('127.0.0.1',9998)
s.bind(addr)

print('Bind UDP on 9998...')
while True:
	data,addr=s.recvfrom(1024)
	print('Received from %s:%s'%addr)
	s.sendto(b'Hello,%s!'%data,addr)