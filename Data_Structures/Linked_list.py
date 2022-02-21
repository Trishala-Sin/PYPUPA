# This is to practice basic data structures: Linked list

# Single unit linked list consist of an element and pointer to the next element
# dynamic in nature no need to define fixed size.

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;


class LinkedList:
    def __int__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    list1 = LinkedList()
    list1.head = Node(1)
    second = Node(2)
    third = Node(3)
    list1.head.next = second
    second.next = third

    list1.printList()
