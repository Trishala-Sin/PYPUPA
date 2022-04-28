# BST Implementaion 


class bst_node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.root = data 
    
    def insertion(self,element):
        if element == self.root:
            return
        if element < self.root:
            if self.left :
                self.left.insertion(element)
            else:
                self.left = bst_node(element)
        if element > self.root:
            if self.right :
                self.right.insertion(element)
            else:
                self.right = bst_node(element)
    
    def search(self,element):
        if self.root == element:
            print(True) 
        if self.root < element:
            if self.right:
                self.right.search(element)
            else:
                print(False)
        if self.root > element:
            if self.left : 
                self.left.search(element)
            else:
                print(False)
            
        
    
Node = bst_node(2)
Node.insertion(3)

print(Node.left)
print(Node.right.root)
Node.search(3)
Node.search(5)
    