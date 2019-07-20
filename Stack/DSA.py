class node:
    #constructor of node
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return 'node({})'.format(self.value)    

    __repr__ = __str__

class Stack:
    #stack constructor initialise top of statck and counter
    def __init__(self):
        self.top = None
        self.minimum =None
        self.count = 0

    # def __str__(self):
    #     temp = self.top
    #     out = []
    #     while temp:
    #         out.append(str(temp.value))
    #         temp = temp.next
    
    def push(self , new_data):
        if self.top is None:
            self.top = node(new_data)
            self.minimum = new_data
        

        #push mai self.minimum wo value hai jo push kii jaa rahi hai and temp wo jo create ho raha hai
        elif new_data < self.minimum:
            temp = (2 * new_data) - self.minimum
            new_node = node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = new_data
        
        else:
            new_node = node(new_data)
            new_node.next = self.top
            self.top = new_node
        print('number inserted: {}'.format(new_data))

    def pop(self):
        if self.top is None:
            print('stack is empty')
        else:
            removed_element = self.top.value
            self.top = self.top.next
            if removed_element < self.minimum:
                self.minimum = (2 * self.minimum) - removed_element
                print('self.minimum is: {}'.format(self.minimum))
                print("removed element is: {} ".format(removed_element))
            else:
                print('self.minimum is: {}'.format(self.minimum))
                print('removed_element is: {}'.format(removed_element))

    def getmin(self):
        if self.top is None:
            print('stack is empty')
        else:
            print("minimim value is: {}".format(self.minimum))

    def getpeek(self):
        if self.top is None:
            print('stack is empty')
        else:
            temp = self.top
            print(temp)

    def len(self):
        temp = self.top
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        print('count: {}'.format(count))


    def print_list(self):
        temp = self.top
        while(temp):
            print(temp)
            temp = temp.next
            
    def isempty(self):
        if self.top is None:
            print('stack is empty')
        else:
            print('not Empty')




if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(1)
    stack.push(5)
    stack.push(7)
    stack.print_list()
    stack.len()
    stack.isempty()
    stack.getmin()
    stack.pop()
    stack.getpeek()
