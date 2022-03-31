
class stack_im:
    def __init__(self):
        self.li = []
    def empty(self):
        if self.li:
            print("stack not empty")
        else :
            print('stack is empty')
        
    def top(self):
        print(self.li[-1])
    
    def push(self,data):
        self.li.append(data)
        
    def pop(self):
        self.li.pop(-1)
        
    def printst(self):
        print(self.li)

if __name__ == '__main__':
    
    stack = stack_im()
    
    stack.empty()
    stack.push('abc')
    stack.push(1)
    stack.push(2)
    stack.printst()
    stack.top()
    stack.pop()
    stack.printst()
    


        

