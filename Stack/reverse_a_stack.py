# Infixtoprefix(exp)
# {
#     create a stack named s

#     loop starting from 0 to len(exp):
#         if the exp[i] is operand:
#             append to postfix list
#         else if operator:
            
# }


class stack:
    def __init__(self):
        self.item = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2 , '^':3}
        self.postfix = []

    def push(self , i):
        self.item.insert(0,i)

    def isEmpty(self):
        return self.item == []

    def pop(self):
        self.item.pop()

    def peek(self):
        return self.item[0]

    def length(self):
        return len(self.item)

    def infixtopostfix(self , exp):
        tokenlist = exp.split()
        print(tokenlist)

        for i in tokenlist:
            #print(i)
            if i in "qwertyuiopasdfghjklzxcvbnm":
                self.postfix.append(i)
                print(self.postfix)
            elif i is '(':
                a = self.push(i)
                print(a)
            elif i is ')':
                toptoken = self.item.pop()
                while toptoken!='(':
                    b = self.postfix.append(i)
                    print('b is: ')
                    print(b)
                    toptoken = self.item.pop()
                    print(toptoken)

            else:
                while(not self.isEmpty() and (self.precedence[self.peek()] >= self.precedence[i])):
                    c = self.postfix.append(self.item.pop())
                    print('c is: ')
                    print(c)
                d = self.push(i)
                e = self.item
                print('d is: ' + str(d))
                print(self.item)
        
        while not self.isEmpty():
            self.postfix.append(self.item.pop())
        #return ''.join(self.postfix)
        print(''.join(self.postfix))
        print(self.item)    

if __name__ == "__main__":
    exp = ' a + b - c * g / h '
    s = stack()
    s.infixtopostfix(exp)

