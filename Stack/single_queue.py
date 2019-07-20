class node:
    def __init__(self , value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.s1 = []
    
    def push(self, new_data):
#        new_node = node(new_data)
        if self.top is None:
            self.top = node(new_data)
            print('top value is: {}'.format(self.top.value))
        else:
            new_node = node(new_data)
            new_node.next = self.top
            self.top = new_node
            print(self.top.value)


    def print_list(self):
        self.s1 = []
        temp = self.top
        while(temp):
            self.s1.append(temp.value)
            temp = temp.next
        print(self.s1)

    def deque(self):
        if self.top is None:
            print('empty')
        else:
            a = self.s1.pop()
            print(a)
        print(self.s1)

    

if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(6)
    s.push(3)
    s.push(7)
    s.print_list()
    s.deque()
    s.print_list()