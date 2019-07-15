class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node = node(new_node)
        new_node.next = self.head
        self.head = new_node

    def repition(self , data):
        temp = self.head
        count = 0
        while(temp):
            if(temp.data == data):
                count += 1
            else:
                print('error')
            temp = temp.next
        print(count)    


if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(9)
    llist.push(3)
    llist.push(9)
    llist.push(4)
    llist.push(5)
    llist.push(9)
    llist.repition(9)
    