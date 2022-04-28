# This is to practice basic data structures: Linked list

# Single unit linked list consist of an element and pointer to the next element
# dynamic in nature no need to define fixed size.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,'-->',end =' ')
            temp = temp.next
    def append(self , new_element):
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = new_element
        else:
            self.head = new_element
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        curr_pos = self.head 
        pos = 0
        if self.head:
            while curr_pos.next:
                pos +=1 
                if self.head.next == position :
                    return pos 
        return None

        



if __name__ == '__main__':
    
    #list1.head = Node(1)
    no1 = Node(1)
    no2 = Node(2)
    no3 = Node(3)
    l1 = LinkedList()
    l1.append(no1)
    l1.append(no2)
    l1.append(no3)
    l1.get_position(3)
    l1.printList()
