#LINKED LIST IMPLEMENTATION of Stack
class Node:
    def __init__(self):
        self.data = None
        self.next = None
    # set data field
    def set_data(self,data):
        self.data = data
    # get data
    def get_data(self):
        return self.data
    #set next field of node
    def set_next(self,nxt):
        self.next = nxt
    # get next field
    def get_next(self):
        return self.next
    # returns true if node points to another node
    def has_next(self):
        return self.next != None
class StackList:
    def __init__(self):
        self.head = None
        self.length = 0
    def push(self,data):
        new_node = Node()
        new_node.set_data(data)
        new_node.set_next(None)
        if self.head == None:
            self.head = new_node
            self.length += 1
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
            self.length += 1
    def pop(self):
        if self.head == None:
            print("Stack Underflow")
        elif self.head.get_next() == None:
            self.head = None
        else:
            current = self.head
            prev = self.head
            while current.get_next() != None:
                prev = current
                current = current.get_next()
            prev.set_next(None)
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def size(self):
        return self.length
    def peek(self):
        if self.head == None:
            print("Stack Underflow")
        elif self.head.get_next() == None:
            return self.head.get_data()
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            return current.get_data()
    def printStack(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()
    
