import sqlite3
import time
import socket
import pickle

# Connect to DB
conn = sqlite3.connect('Google_Meets.db')
c = conn.cursor()
query = "select ID, Mail, substr(Meet, 25), Location, Device, Timestamp, Latitude, longitude, Admin , JorL from Table1"
c.execute(query)
table = c.fetchall()
conn.close()

# Connect to Server1
s1 = socket.socket()
host = socket.gethostname()
port1 = 8103
s1.bind((host, port1))
s1.listen(1)
print("Waiting ....")
conn1, addr1 = s1.accept()
print(addr1, "has connected")

# Connect to Server2
s2 = socket.socket()
host = socket.gethostname()
port2 = 8203
s2.bind((host, port2))
s2.listen(1)
print("Waiting ....")
conn2, addr2 = s2.accept()
print(addr2, "has connected")

# Load Balancing
for record in table:
	data = pickle.dumps(record)
	print(record[2][0])
	if record[2][0] < 'n':
		conn1.send(data)
	else:
		conn2.send(data)
	sleep(0.1)

data = pickle.dumps("end")
conn1.send(data)
conn2.send(data)
s1.close
s2.close


# id_count = 1
# while 1:
# 	query = "select ID, Mail, substr(Meet, 25), Location, Device, Timestamp, Latitude, longitude, Admin , JorL from Table1 where ID is "+str(id_count)
# 	try:
# 		conn = sqlite3.connect('Google_Meets.db')
# 		c = conn.cursor()
# 		c.execute(query)
# 		l = c.fetchall()
# 		id_count += 1
# 		if l != []:
# 			print(l)
# 		conn.close()
# 	except:
# 		time.sleep()
