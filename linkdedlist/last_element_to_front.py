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
        
    def movetofront(self):
        temp = self.head
        print(temp.data)
        while(temp):
            temp = temp.next

        print(temp)
        last_no = temp
        print(last_no)


    
            

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(6)
    llist.push(6)
    llist.movetofront()
    