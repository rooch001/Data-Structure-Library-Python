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

# Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = Node()
        self.lengths = 0
    # return length of list
    def length(self):
        count = 0
        if self.head.get_next() == None:
            return 0
        else:
            current = self.head
            count += 1
            current = current.get_next()
            while current != self.head:
                current = current.get_next()
                count += 1
            return count
    # insert in end position
    def insert_at_end(self,data):
        current = self.head 
        new_node = Node()
        new_node.set_data(data)
        if self.lengths == 0:
            self.head = new_node
            new_node.set_next(new_node)
            self.lengths += 1
        else:
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.head)
            self.lengths +=1
    # insert in front position     
    def insert_at_front(self,data):
        current = self.head
        new_node = Node()
        new_node.set_data(data)
        if self.lengths == 0:
            self.head = new_node
            new_node.set_next(new_node)
            self.lengths += 1
        else:
            new_node.set_next(self.head)
            current = current.get_next()
            while current.get_next() !=self.head:
                current = current.get_next()
            current.set_next(new_node)
            self.head = new_node
            self.lengths += 1
    # delete at end position       
    def delete_at_end(self):
        if self.lengths == 0:
            return "List is Empty"
        elif self.lengths == 1:
            self.head = None
            self.lengths -= 1
        else:
            current = self.head
            previous = self.head
            while current.get_next() != self.head:
                previous = current
                current = current.get_next()
            previous.set_next(self.head)
            self.lengths -= 1
    # delete from front
    def delete_at_front(self):
        if self.lengths == 0:
            return "List is Empty"
        elif self.lengths == 1:
            self.head = None
            self.lengths -= 1
        else:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()
            self.lengths -= 1
    # print list    
    def print_List(self):
        current = self.head
        if current == None:
            return "Empty List"
        print(current.get_data())
        while current.get_next() != self.head:
            current = current.get_next()
            print(current.get_data())
