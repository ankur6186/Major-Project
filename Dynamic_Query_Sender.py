import time
import sqlite3

f = open("Dynamic_Queries.txt", "r")
for line in f.readlines():
	try:
		conn = sqlite3.connect('Google_Meets.db')
		c = conn.cursor()
		c.execute(line)
		conn.commit()
		conn.close()
	except:
		time.sleep(5)