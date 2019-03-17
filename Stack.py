# Stack Data Structure Implemented by arrays
# Stack - Last In First Out
class Stack:
    def __init__(self):
        self.array = []
    # method push insert element in the end of array
    def push(self,element):
        self.array.append(element)
    # method pop delets element from the first position of the array and return the element
    def pop(self):
        return self.array.pop()
    # method returns top element of stack
    def peek(self):
        return self.array[-1]
    # method return the size of stack
    def size(self):
        return len(self.array)
    # method checks whether the stack is empty or not ; returns bool (True|False)
    def isEmpty(self):
        return len(self.array) <= 0