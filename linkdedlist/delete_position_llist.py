class node:
    def __init__(self , data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None


    def push(self , new_node):
        new_node = node(new_node)
        new_node.next  = self.head
        self.head = new_node

    def delete(self, position):
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next


    def printlist():
        temp = self.head
        while(temp):
            print(temp)
            temp = temp.next


if __name__ == '__main__':
    llist = linkedlist()
    llist.push(2)
    llist.push(4)
    #position is specified in parameters
    llist.delete(1)

    llist.printlist()