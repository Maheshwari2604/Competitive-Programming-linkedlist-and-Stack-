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

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head

        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            print(slow_p)
            print(fast_p)
            
            if slow_p == fast_p:
                print('found')
                return
            
            else:
                print("not found")




if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(9)
    llist.push(3)
    llist.push(9    )
    llist.push(9)
    llist.detect_loop()
    