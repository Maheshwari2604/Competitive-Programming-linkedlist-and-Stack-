class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = node(new_data)
		new_node.next = self.head
		self.head = new_node

	def deletenode(self, key):
		temp = self.head
		
		if(temp is not None):
			if(temp.data == key):
				self.head = temp.next
				temp = None
				return
		
		while(temp is not None);
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return

		prev.next = temp.next

		temp = None

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
		

if __name__ == '__main__':
	l = linkedlist()
	l.push(1)
	l.push(2)
	l.push(3)
	l.push(4)
	l.deletenode(1)
	l.printlist()
		
