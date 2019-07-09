#node
class node:
	
	def __init__(self, data):
		self.data = data
		print(self.data)
		self.next = None

#linkedlist
class linkedList:
	def __init__(self):
		self.head = None

	def printvalue():
		temp = self.head
		while(temp):
			v = temp.data
			print(v)
			temp.next
			
		
	
if __name__ == '__main__':
	list = linkedList()
	
	list.head = node(1)
	print('hey here a value is: ')
	print(list.head.data)
	secand = node(2)
	print(secand)
	third = node(3)
	print(third)

	list.head.next = secand;
	print(list.head.next)
	secand.next = third;
	print(secand.next)
	
	print('Done')






#Output:
'''
1
hey here a value is: 
1
2
<__main__.node instance at 0x7fb9559a37a0>
3
<__main__.node instance at 0x7fb9559a37e8>
<__main__.node instance at 0x7fb9559a37a0>
<__main__.node instance at 0x7fb9559a37e8>
Done
'''

