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

           
    def printlist(self):
        temp = self.head
        count = 0
        while(temp is not None):
            print(temp.data)
            count += 1
            temp = temp.next
        print(count)

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.printlist()