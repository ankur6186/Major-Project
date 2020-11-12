from Trie2 import Trie_Mail

class Trie_Node_Meet:
	def __init__(self, char):
		self.char = char
		self.is_terminal = False
		self.counter = 0
		self.admin_email = None
		self.children = {}
		self.trie_mail = None

class Trie_Meet:
	def __init__(self):
		self.root = Trie_Node_Meet("#")

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

		meet_link = record[2]
		for char in meet_link:
			if char in node.children:
				node = node.children[char]
			else:
				new_node = Trie_Node_Meet(char)
				node.children[char] = new_node
				node = new_node
		if node.is_terminal == False:
			node.admin_email = record[1]
			node.is_terminal = True
		if node.trie_mail == None:
			node.trie_mail = Trie_Mail()
		isPresent = node.trie_mail.add_participant(record)
		if isPresent == True:
			node.counter += 1

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
		node.trie_mail.remove_participant(record)
		node.counter -= 1
		if node.counter == 0:
			self.remove_meet(meet_link)

	def dfs(self, node):
		if node.is_terminal == True:
			print("Meet->"+str(node.counter))
			node.trie_mail.dfs(node.trie_mail.root)
			print("")
		for child in node.children.values():
			self.dfs(child)
