# Linked list is an abstract data type
# Successive elements are connected with pointers
# last element is connected to null 
# can be grow or shrink during program execution
# can be made as long as req until all memory is exhuasted
# does not waste memory but still some memory is used to store pointers
# head -> 4->15->7->40->NULL
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

class SinglyLinkedList:
    def __init__(self):
        self.head = Node() 
        self.length = 0
    # returns length of list
    def list_lenght(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        return count
    
    # insert at first position of linked list
    def insert_at_begining(self,data):
        new_node = Node()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1
    # insert in end position of linked list
    def insert_at_end(self,data):
        new_node = Node()
        new_node.set_data(data)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        if self.length == 0:
            self.head = new_node
        else:
            current.set_next(new_node) 
        self.length += 1
    # insert at any position of linked list
    def insert_at_position(self,position,data):
        if position < 0  or position > self.length:
            return None
        if position == 0:
            self.insert_at_begining(data)
        elif position == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            count = 1
            current = self.head
            while count < position - 1:
                count += 1
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            self.length += 1
    # deletes at first position
    def delete_at_begining(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.get_next()
            self.length -= 1
    # deleting last position data      
    def delete_at_end(self):
        if self.length == 0:
            print("List is empty")
        else:
            current = self.head
            previous = self.head
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            self.length -= 1
    # deleting any position data
    def delete_at_position(self,position):
        if position < 0  and position > self.length:
            return None
        if self.length == 0:
            print("The list is empty")
        elif position == 1:
            self.delete_at_begining()
        elif position == self.length:
            self.delete_at_end()
        else:
            current = self.head
            count = 1
            while count < position -1:
                count += 1
                current = current.get_next()
            current.set_next((current.get_next()).get_next())
            self.length -= 1
   
    # clear linked lists
    def clear(self):
        self.head = None
    # print list
    def print_list(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()
    # reversing the list
    def reverse_list(self):
        prev = None
        current = self.head
        while current != None:
            new = current.get_next()
            current.set_next(prev)
            prev = current
            current = new
        self.head = prev