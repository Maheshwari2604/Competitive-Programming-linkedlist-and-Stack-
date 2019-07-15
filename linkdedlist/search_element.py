class node:
    def __init__(self , data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self , data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def search_element(self , key):
        temp = self.head
        while(temp):
            if temp.data == key:
                print('yes found')
                break
            else:
                print('not found')
                temp = temp.next

        

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    #search element present or not
    llist.search_element(2)
