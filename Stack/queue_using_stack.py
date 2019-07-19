class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self , x):
        #move all elements from S1 to S2
        print('inital: '+ str(self.s1))
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            print(self.s2)
            print(self.s1.pop())

        #append all elements
        self.s1.append(x)
        print('s1 is: ' + str(self.s1))
    
        #push back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            print('self.s1 is : ')
            print(self.s1)
            self.s2.pop() 

    def dequeue(self):
        if len(self.s1) == 0:
            print('Empty')
        else:
            x = self.s1[-1]
            print(self.s1.pop())
            return x


    def print_queue(self):
        #print(self.s1)
        print('s1 is: ')
        print(self.s1)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(7)
    q.enqueue(5)
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.dequeue()