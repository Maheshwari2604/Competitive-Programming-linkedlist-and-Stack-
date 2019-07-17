import gc

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self , data):
        new_data = node(data)
        new_data.next = self.head

        if self.head is not None:
            self.head.prev = new_data
        
        self.head = new_node

    def deletenode(self , del):
        #base case
        if self.head is None or del is None:
            return

        # If node to be deleted is head node 
        if self.head == del:
            self.head = del.next

        # Change next only if node to be deleted is NOT 
        # the last node
        if del.next is not None:
            del.next.prev = del.prev

        if del.prev is not None:
            del.prev.next = del.next

        gc.collect()

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)