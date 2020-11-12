import sqlite3
import logging
import math

from Trie1 import Trie_Meet

LOG_FILENAME = "debug.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,filemode='w')

def main():
	conn = sqlite3.connect('Google_Meets.db')
	c = conn.cursor()
	query = "select ID, Mail, substr(Meet, 25), Location, Device, Timestamp, Latitude, longitude, Admin , JorL from Table1"
	c.execute(query)
	table = c.fetchall()
	conn.close()

	trie_meet = Trie_Meet()
	for record in table:
		if record[9] == 0:
			trie_meet.add_participant(record)
		else:
			trie_meet.remove_participant(record)
	trie_meet.dfs(trie_meet.root)

if __name__ == '__main__':
	main()