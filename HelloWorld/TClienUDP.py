import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr=('127.0.0.1',9998)
for data in [b'Michael',b'Tracy',b'Sarah']:
	s.sendto(data,addr)
	print("Received %s from server!"%s.recv(1024).decode('utf-8'))
s.close()