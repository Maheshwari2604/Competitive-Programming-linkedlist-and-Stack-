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
        self.item.append(i)

    def isEmpty(self):
        return self.item = []

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
            if i in "qwertyuiopasdfghjklzxcvbnm":
                self.postfix.append(i)
            elif i is '(':
                self.push(i)
            elif i is ')':
                toptoken = self.item.pop()
                while toptoken!='(':
                    self.postfix.append(i)
                    toptoken = self.item.pop()

    

if __name__ == "__main__":
    exp = 
    s = stack()
    s.infixtopostfix(exp)

