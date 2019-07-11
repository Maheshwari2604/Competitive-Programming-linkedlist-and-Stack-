class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None


	def append(self, new_data):
		new_node = node(new_data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next

		last.next = new_node



	def push(self, data):
		n_node = node(data)
		n_node.next = self.head
		self.head = new_node

	def insertafter(self, prev, new):
		if prev is None:
			print ('in linklist')

		new_node = node(new)

		new_node.next = prev.next

		prev.next = new_node
		

if __name__ == '__main__':
	list = linkedlist()
	
	list.append(2)

	list.push(3)

	list.push(4)

	list.insertafter(list.head.next, 5)
