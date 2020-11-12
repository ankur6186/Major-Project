import logging

LOG_FILENAME = "info.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,filemode='w')

class Trie_Node_Meet:
	def __init__(self, char):
		self.char = char
		self.is_terminal = False
		self.counter = 0
		self.admin_email = None
		self.children = {}
		# self.trie_email = Trie_Link()

class Trie_Meet:
	def __init__(self):
		self.root = Trie_Node_Meet("#");

	def search(self, meet_link):
		node = self.root
		for char in meet_link:
			if char in node.children:
				node = node.children[char]
			else:
				return False
		return node.is_terminal

	def add_participant(self, record):
		node = self.root

		# Check for No person to try a meet before the admin creates it.
		if record[8] == 0:

			if self.search(record[2]) == False:
				logging.debug("Attempt of Invalid Access Detected by participant: "+record[1]+" in the meet: "+record[2])
				return
			else:
				logging.debug("Meet participant: "+record[1]+" added to meet: "+record[2])
		else:
			logging.debug("Admin participant: "+record[1]+" created the meet link: "+record[2])
		meet_link = record[2]
		for char in meet_link:
			if char in node.children:
				node = node.children[char]
			else:
				new_node = Trie_Node_Meet(char)
				node.children[char] = new_node
				node = new_node
		node.is_terminal = True
		node.counter += 1
		node.admin_email = record[1]

	def remove_meet(self, meet_link, depth=0):
		node = self.root
		for char in meet_link:
			l = len(node.children)
			if l == 1:
				node.children[char] = None
				del node.children[char]
				break
			if char in node.children:
				node = node.childen[char]

	def remove_participant(self, record):
		node = self.root
		meet_link = record[2]
		for char in meet_link:
			if char in node.children:
				node = node.children[char]
		node.counter -= 1
		if node.counter == 0:
			self.remove_meet(meet_link)

	def dfs(self, node):
		print(node.char)
		for child in node.children.values():
			self.dfs(child)

l = [
# (1, 'ivoibs@gmail.com', 'wjw-gkvb-wdi', 'Raipur', 'Laptop', '2020-10-08 12:34:21', 21.25, 81.629997, 1, 0), 
# (2, 'rahul@gmail.com', 'wjw-gkvb-wdi', 'Mumbai', 'Laptop', '2020-10-08 12:34:21', 19.07609, 72.8774, 0, 0), 
# (3, 'ajay@gmail.com', 'wjw-gkvb-wdi', 'Lucknow', 'Android', '2020-10-08 12:34:21', 26.85, 80.949997, 0, 0), 
# (4, 'anmol@gmail.com', 'wjw-gkvb-wdi', 'Delhi', 'Laptop', '2020-10-08 12:34:21', 28.610001, 77.230003, 0, 0), 
# (5, 'barkha@gmail.com', 'wjw-gkvb-wdi', 'Ratnagiri', 'Android', '2020-10-08 12:34:21', 16.994444, 73.300003, 0, 0), 
# (6, 'ben@gmail.com', 'wjw-gkvb-wdi', 'Ratnagiri', 'Android', '2020-10-08 12:34:21', 16.994444, 73.300003, 0, 0), 
# (7, 'ram@gmail.com', 'wjw-gkvb-wdi', 'Gotak, Karnataka', 'iOS', '2020-10-08 12:34:21', 16.1667, 74.833298, 0, 0), 
# (8, 'ajay@gmail.com', 'wjw-gkvb-wdi', 'Lucknow', 'Android', '2020-10-08 12:34:21', 26.85, 80.949997, 0, 1), 
# (9, 'raj@gmail.com', 'wjw-gkvb-wdi', 'Mumbai', 'Laptop', '2020-10-08 12:34:22', 19.07609, 72.8774, 0, 0), 
# (10, 'raj@gmail.com', 'wjw-gkvb-wdi', 'Mumbai', 'Laptop', '2020-10-08 12:34:22', 19.07609, 72.8774, 0, 1), 
# (11, 'rakesh@gmail.com', 'wjw-gkvb-wdi', 'Raipur', 'Android', '2020-10-08 12:34:22', 21.25, 81.629997, 0, 0), 
# (12, 'riya@gmail.com', 'wjw-gkvb-wdi', 'Belgaum, Karnataka', 'Laptop', '2020-10-08 12:34:22', 15.852792, 74.498703, 0, 0), 
# (13, 'ben@gmail.com', 'wjw-gkvb-wdi', 'Ratnagiri', 'Android', '2020-10-08 12:34:22', 16.994444, 73.300003, 0, 1), 
# (14, 'ranjan@gmail.com', 'wjw-gkvb-wdi', 'Barh, Bihar', 'iOS', '2020-10-08 12:34:22', 25.477585, 85.709091, 0, 0), 
# (15, 'nikita@gmail.com', 'wjw-gkvb-wdi', 'Roorkee, Uttarakhand', 'iOS', '2020-10-08 12:34:22', 29.854263, 77.888, 0, 0), 
# (16, 'abha@gmail.com', 'wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', '2020-10-08 12:34:22', 12.971599, 77.594566, 0, 0), 
# (17, 'shreyansh@gmail.com', 'wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', '2020-10-08 12:34:22', 12.971599, 77.594566, 0, 0), 
# (18, 'tushar@gmail.com', 'wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', '2020-10-08 12:34:22', 12.971599, 77.594566, 0, 0), 
# (19, 'abha@gmail.com', 'wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', '2020-10-08 12:34:23', 12.971599, 77.594566, 0, 1), 
# (20, 'soha@gmail.com', 'wjw-gkvb-wdi', 'Almora, Uttarakhand', 'Laptop', '2020-10-08 12:34:24', 29.594189, 79.653893, 0, 0), 
# (21, 'sohail@gmail.com', 'wjw-gkve-abc', 'Kharagpur, West Bengal', 'Android', '2020-10-08 15:13:18', 22.34601, 87.231972, 1, 0), 
# (22, 'shivani@gmail.com', 'wjw-gkve-abc', 'Fatehpur, Rajasthan', 'Android', '2020-10-08 15:13:18', 27.99502, 74.961792, 0, 0), 
# (23, 'shivam@gmail.com', 'wjw-gkve-abc', 'Siliguri, West Bengal', 'iOS', '2020-10-08 15:13:18', 26.732311, 88.410286, 0, 0), 
# (24, 'shivani@gmail.com', 'wjw-gkve-abc', 'Fatehpur, Rajasthan', 'Android', '2020-10-08 15:13:18', 27.99502, 74.961792, 0, 1), 
# (25, 'swaraj@gmail.com', 'wjw-gkve-abc', 'Mangaluru, Karnataka', 'Android', '2020-10-08 15:13:18', 12.915605, 74.855965, 0, 0), 
(26, 'sitara@gmail.com', 'wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', '2020-10-08 15:13:18', 23.9468, 88.049713, 1, 0), 
(27, 'sitara@gmail.com', 'wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', '2020-10-08 15:13:18', 23.9468, 88.049713, 0, 1) 
# (28, 'archana@gmail.com', 'wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', '2020-10-08 15:13:18', 23.9468, 88.049713, 0, 0), 
# (29, 'rakshatha@gmail.com', 'wjw-gkve-abc', 'Mangaluru, Karnataka', 'Android', '2020-10-08 15:13:19', 12.915605, 74.855965, 0, 0), 
# (30, 'shabana@gmail.com', 'wjw-gkve-abc', 'Vijaypur, Jammu and Kashmir', 'iOS', '2020-10-08 15:13:19', 32.564522, 75.023148, 0, 0), 
# (31, 'archana@gmail.com', 'wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', '2020-10-08 15:13:19', 23.9468, 88.049713, 0, 1), 
# (32, 'rihanna@gmail.com', 'wjw-gkve-abc', 'Rahon, Punjab', 'Android', '2020-10-08 15:13:19', 31.052128, 76.1175, 0, 0), 
# (33, 'gurpreet@gmail.com', 'wjw-gkve-abc', 'Rahon, Punjab', 'Laptop', '2020-10-08 15:13:19', 31.052128, 76.1175, 0, 0), 
# (34, 'bheem@gmail.com', 'wjw-gkve-abc', 'Mangaluru, Karnataka', 'Android', '2020-10-08 15:13:19', 12.915605, 74.855965, 0, 0), 
# (35, 'anisha@gmail.com', 'wjw-gkve-abc', 'Shimoga, Karnataka', 'iOS', '2020-10-08 15:13:19', 13.92993, 75.5681, 0, 0), 
# (36, 'devansh@gmail.com', 'wjw-gkve-abc', 'Shimoga, Karnataka', 'iOS', '2020-10-08 15:13:19', 13.92993, 75.5681, 0, 0), 
# (37, 'rihanna@gmail.com', 'wjw-gkve-abc', 'Rahon, Punjab', 'Android', '2020-10-08 15:13:19', 31.052128, 76.1175, 0, 1), 
# (38, 'blare@gmail.com', 'wjw-gkve-abc', 'Moga, Punjab', 'iOS', '2020-10-08 15:13:19', 30.81646, 75.171707, 0, 0), 
# (39, 'alice@gmail.com', 'wjw-gkve-abc', 'Batala, Punjab', 'Laptop', '2020-10-08 15:13:19', 31.823462, 75.205063, 0, 0), 
# (40, 'blare@gmail.com', 'wjw-gkve-abc', 'Moga, Punjab', 'iOS', '2020-10-08 15:13:19', 30.81646, 75.171707, 0, 1)
]

trie_meet = Trie_Meet()
for i in range(len(l)):
	if l[i][9] == 0:
		trie_meet.add_participant(l[i])
	else:
		trie_meet.remove_participant(l[i])
	trie_meet.dfs(trie_meet.root)
