class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None

    def push(self , new_node):
        new_node = node(new_node)
        new_node.next = self.head
        self.head = new_node

    def middle_element(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            #print(temp.data)
            temp = temp.next

            
        middle = count/2 + 1
        print(count)
        print(middle)
        print(type(middle))

        count = 1
        temp = self.head
        print('here the value is')
        print(count)
        print(middle)
        print('above initial values')
        while(temp):
            if (count == middle):
                print(temp.data)
                break
            else:
                temp = temp.next
                count += 1
                #print(temp.data)
                print('error')

        # middle = count/2 + 1
        # print(count)
        # print(middle)
        # print(type(middle))


        

if __name__ == "__main__":
    llist = linkedlist()
    llist.push(2)
    llist.push(33)
    llist.push(411)
    llist.push(522)
    llist.push(623)
    llist.push(35589)
    llist.push(642)
    llist.push(9)
    llist.push(512)
    llist.push(33)
    llist.push(334)
    llist.middle_element()   