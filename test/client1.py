import socket
import pickle
s = socket.socket()
host = 'ankur-Inspiron-5567'
port = 8191
s.connect((host, port))
print("Connected")

while 1:
	recvd_data = s.recv(3000)
	l = pickle.loads(recvd_data)
	print(l)