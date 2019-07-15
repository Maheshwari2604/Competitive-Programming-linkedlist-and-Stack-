class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self , new_node):
        new_node = node(new_node)
        new_node.next = self.head
        self.head = new_node
        print(self.head.data)

    def count_length(self):
        temp = self.head
        count = 0

        while(temp):
            temp = temp.next
            count += 1
        
        print('length of ll is: ' + str(count))
        return count


if __name__ == '__main__':
    llist = Linkedlist()
    print('hey push the values')
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)

    llist.count_length()
    
                