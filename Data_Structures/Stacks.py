#empty() – Returns whether the stack is empty – Time Complexity: O(1)
#size() – Returns the size of the stack – Time Complexity: O(1)
#top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
#push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
#pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

#  stack implementation using list

class stack_im:
    def __init__(self):
        self.list_element = []

    def empty(self):
        if self.list_element:
            print('stack not empty')
        else:
            print('Empty stack')

    def size(self):
        return len(list_element)

    def top(self):
        return list_element[-1]

    def push(self,data):
        self.list_element.append(data)

    def pop(self):
        self.list_element.pop(-1)

    def Print_stack(self):
        return print(self.list_element)



if __name__ == "__main__":
    stack = stack_im()

    stack.empty()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.Print_stack()
    stack.empty()
    stack.pop()
    stack.Print_stack()




