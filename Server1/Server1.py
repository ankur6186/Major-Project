import socket
import pickle
s = socket.socket()
host = 'ankur-Inspiron-5567'
port = 8103
s.connect((host, port))
print("Connected")

while 1:
	recvd_data = s.recv(3000)
	try:
		record = pickle.loads(recvd_data)
		if record == "end":
			break
		print(record)
	except EOFError:
		print("nothing")