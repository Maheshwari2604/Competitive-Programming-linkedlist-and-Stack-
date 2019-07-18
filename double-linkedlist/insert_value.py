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

    def insert_value(self , new_node):
        temp = node(new_node)
        x = temp.data
        print(x)
        temp1 = self.head
        y = temp1.data
        print(y)
        while(temp1):
            #print(temp1.data)
            while(temp1.data >= temp.data):
                temp1.data = temp.data
                print(temp1.data)
                temp.data = y
                temp1 = temp1.next
                
            temp1 = temp1.next

        

           
    def printlist(self):
        temp = self.head
        count = 0
        while(temp is not None):
            print(temp.data)
            count += 1
            temp = temp.next
        print('count is:')
        print(count)

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.printlist()
    llist.insert_value(1)