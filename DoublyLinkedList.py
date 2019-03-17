class Node1:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None  
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data = data
    def get_next(self):
        return self.next
    def set_next(self,nxt):
        self.next = nxt
    def has_next(self):
        return self.next != None
    def get_prev(self):
        return self.prev
    def set_prev(self,prev):
        self.prev = prev
    def has_prev(self):
        return self.prev != None
    def __str__(self):
        return "Node [Data = %s]" % (self.data,)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node1()
        self.tail = None
        self.length = 0
    # insert in the begining
    def insert_at_begining(self,data):
        new_node = Node1()
        new_node.set_data(data)
        if self.length == 0:
            self.head = self.tail = new_node
            self.length += 1
        else:
            new_node.set_prev(None)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
            self.length += 1
    # insert in the end       
    def insert_at_end(self,data):
        new_node = Node1()
        new_node.set_data(data)
        if self.length == 0:
            new_node.set_prev(None)
            self.head = self.tail = new_node
            self.length += 1
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            new_node.set_prev(current)
            current.set_next(new_node)
            self.tail = current.get_next()
            self.length += 1
    # insert at any position       
    def insert_at_position(self,position,data):
        if position < 0 or position > self.length:
            return None
        if position == 0:
            self.insert_at_begining(data)
        elif position == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node1()
            new_node.set_data(data)
            count = 1
            current = self.head
            while count < position-1:
                count += 1
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            new_node.set_prev(current)
            self.length += 1
    # delete in begining
    def delete_at_begining(self):
        if self.length == 0:
            return "List Is empty"
        elif self.length == 1:
            self.head = self.tail =  None
            
        else:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        self.length -= 1
    # delete in end    
    def delete_at_end(self):
        if self.length == 0:
            return "List Is empty"
        if self.length == 1:
            self.head = self.tail = None
            
        else:
            current = self.head
            previous = self.head
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            self.tail = previous
        self.length -= 1
    # delete at position
    def delete_at_position(self,position):
        if position < 0  or  position >self.length:
            print("List Index Error") 
        elif position == 1 :
            self.delete_at_begining()
        elif position == self.length:
            self.delete_at_end()
        else:
            current = self.head
            count = 1
            while count < position - 1:
                count += 1
                current = current.get_next()
            current.get_next().get_next().set_prev(current)
            current.set_next((current.get_next()).get_next())
            self.length -= 1
    # print list   
    def print_list(self):
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_next()