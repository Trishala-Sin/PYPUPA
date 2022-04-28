# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class bst():
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None


    def insert_val(self,data):
        if data == self.root:
            return 
        if data < self.root:
            if self.left:
                self.left.insert_val(data)
            else:

                self.left=bst(data)
               
        else:
            print(self.right)
            if self.right:
                self.right.insert_val(data)
            else:
                self.right=bst(data)
  
    def in_order_traversal(self,element):

            
        # First print the data of node
      
            if self.left:
                self.left.in_order_traversal(element)
            element.append(self.root)
        # Finally recur on right child
            if self.right:
                self.right.in_order_traversal(element)
            return(element)
    def search(self,val):
        if val==self.root:
            print( True)
        if val<self.root:    
            if self.left:
                self.left.search(val)
            else:
                print( False)        

        if val>self.root:
            if self.right:
                self.right.search(val)
            else:
                print( False)  
   
    def minimum_value(self):
        if self.left:
            return self.left.minimum_value()
        else:
            return self.root    

    
    
    def delete(self,val):
        if val<self.root:
            if self.left:
                 self.left = self.left.delete(val)
            else:
                return None     
        elif val>self.root:    
            if self.right:
                self.right = self.right.delete(val)
            else:
                return None    
        else:
            if self.left is None and self.right is None:
                  return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                  return self.right    
                
            else:
                minvalue = self.right.minimum_value()  
                self.root=minvalue
                self.right = self.right.delete(val)


        return self      





                
if __name__ == '__main__':
    list_val = [1, 4, 3, 2, 5 ]
    obj = bst(list_val[0])
    for i in range(1,len(list_val)):
        obj.insert_val(list_val[i])
    print(obj.in_order_traversal([]))
    obj.search(10)
    obj.delete(1)
    print(obj.in_order_traversal([]))
