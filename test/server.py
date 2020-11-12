import socket
import pickle

s = socket.socket()
host = socket.gethostname()
port = 8091
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting ....")
conn, addr = s.accept()
print(addr, "has connected")
s1 = socket.socket()
host1 = socket.gethostname()
port1 = 8191
s1.bind((host1, port1))
s1.listen(1)
print(host1)
print("Waiting ....")
conn1, addr1 = s1.accept()
print(addr1, "has connected")

while 1:
	l = [1,2,3,4]
	data = pickle.dumps(l)
	conn.send(data)

	l1 = [1,2,3,4]
	data1 = pickle.dumps(l1)
	conn1.send(data1)
