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
        
        self.head = new_data

    def deletenode(self , dele):
        #base case
        if self.head is None or dele is None:
            return

        # If node to be deleted is head node 
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is NOT 
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev

        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()

    def printlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.printlist()
    llist.deletenode(llist.head)
    llist.printlist()