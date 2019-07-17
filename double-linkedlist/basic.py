
# Node of a doubly linked list  
class node:
    def __init__(self, data):
        self.data = data
        self.next = next
        self.prev = prev

class linkedlist:
    def __init__(self):
        self.head = None

# Adding a node at the front of the list 
    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def inserafter(self, prev_node , new_node):
        if prev_node is None: 
            print("This node doesn't exist in DLL") 
            return
  
        new_node = node(new_data) 
  
        new_node.next = prev_node.next
  
        prev_node.next = new_node 
  
        new_node.prev = prev_node 
  
        if new_node.next is not None: 
            new_node.next.prev = new_node 

# Add a node at the end of the DLL 
    def append(self , new_data):
        new_node = node(new_data)
        temp = self.head
        new_node.next = None

        if self.head is None:
            self.head = new_node
            new.node.prev = None
            return

        while(last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last


if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.inserafter(3 , 6)
    llist.append(8)
    
