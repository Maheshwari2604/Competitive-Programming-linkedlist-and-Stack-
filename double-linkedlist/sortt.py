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

    def sortt(self):
        temp = self.head
        temp1 = self.head
        while(temp.data > temp1.next.data):
                x = temp.data
                print('here temp is')
                print(x)
                print(temp.data)
                temp.data = temp1.next.data
                print('here new temp1 of temp.data is')
                print(temp.data)
                temp1.next.data = x
                print('here temp1.next.data is')
                print(temp.next.data)
                temp1 = temp.next
            
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
    llist.sortt()
    llist.printlist()