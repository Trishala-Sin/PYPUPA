class node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data  = data
    def search(self,value_search):
        if  self.data == value_search:
            print( True)
        if self.left:    
            if self.data >    value_search:
                return(self.left.search(value_search))
        if self.right:        
            if self.data <    value_search:
                return(self.right.search(value_search))
root = node(2)
root.left = node(1)
root.right = node(3)
print(root.right.data)
print(root.search(3))