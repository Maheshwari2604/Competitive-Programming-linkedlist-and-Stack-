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
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                print(temp.data)
                temp = temp.next

            temp.next = new_node
        
        else:
            new_node.next = new_node


        self.head = new_node

    # def printt(self):
    #     temp = self.head
    #     while(temp):
    #         print(temp)
    #         temp = temp.next

        

    
            

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(6)
    llist.push(6)
    llist.printt()
    