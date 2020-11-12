class Trie_Node_Mail:
	def __init__(self, char):
		self.char = char
		self.is_terminal = False
		self.counter = 0
		self.latitude = None
		self.longitude = None
		self.children = {}

class Trie_Mail:
	def __init__(self):
		self.root = Trie_Node_Mail("$")

	def add_participant(self, record):
		node = self.root
		mail = record[1]
		for char in mail:
			if char in node.children:
				node = node.children[char]
			else:
				new_node = Trie_Node_Mail(char)
				node.children[char] = new_node
				node = new_node
		isPresent = True
		if node.latitude == None:
			node.is_terminal = True
			node.counter += 1
			node.latitude = record[6]
			node.longitude = record[7]
			logging.debug("Participant: "+record[1]+" added to meet: "+record[2]+" for first time")
		else:
			lat = abs(node.latitude-record[6])
			lon = abs(node.longitude-record[7])
			distance = math.sqrt(lat**2+lon**2)
			r = 20
			if distance <= r:
				node.counter += 1
				logging.debug("Participant: "+record[1]+" added to meet: "+record[2]+" with another device")
			else:
				isPresent = False
				logging.debug("Participant: "+record[1]+" trying to connect to meet: "+record[2]+" from very far distance. Fraudulent Case Expected")
		return isPresent

	def remove_participant(self, record):
		node = self.root
		mail = record[1]
		for char in mail:
			if char in node.children:
				node = node.children[char]
		logging.debug("Participant: "+record[1]+" removed from the meet: "+record[2])
		node.counter -= 1

	def dfs(self, node):
		# print(node.char)
		if node.is_terminal == True:
			print("Mail->"+str(node.counter))
		for child in node.children.values():
			self.dfs(child)

