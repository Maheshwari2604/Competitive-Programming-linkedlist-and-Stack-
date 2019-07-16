class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self , new_node):
        new_node = node(new_node)
        print(new_node.data)
        new_node.next = self.head
        
        self.head = new_node

    def duplicacy(self):
        temp = self.head
        print(temp)

        if temp is None:
            return
        
        while(temp.next is not None):
            if temp.data == temp.next.data:
                print(temp.data)
                new = temp.next.next
                temp.next= None
                temp.next = new

            else:
                temp = temp.next

            

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(6)
    llist.push(6)
    llist.duplicacy()