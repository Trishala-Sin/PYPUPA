# linked list 

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self,header=None):
        self.header = header
        
    def display(self):
        temp = self.header
        while temp!= None:
            print(str(temp.data) +"-->",end=' ')
            temp = temp.next
            
    def insert(self,new_ele):
        temp = self.header 
        if self.header:
            while temp.next:
                temp = temp.next                
            temp.next = new_ele
        else:
            self.header = new_ele        

            
    def delete(self,val):
        temp = self.header
        if temp.data == val:
            temp = temp.next
            return
        while temp != None:
            if temp.data == val:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return
                
          
                
                
            
        
            

if __name__ == '__main__':
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    LI = Linked_list()
    LI.insert(node1)
    LI.insert(node2)
    LI.insert(node3)
    
    
    #print(node1.next.data)
    LI.display()
    LI.delete(2)
    LI.display()
    
        
        