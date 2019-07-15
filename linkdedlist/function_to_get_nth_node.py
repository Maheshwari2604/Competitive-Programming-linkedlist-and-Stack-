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

    def function_to_get_nth_node(self , key):
        temp = self.head
        count = 0
        while(temp):
            if temp.data == key:
                count += 1
                print("yeah done")
                print(count)
                break
            else:
                count += 1
                print('not found')
                temp = temp.next

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.function_to_get_nth_node(2)