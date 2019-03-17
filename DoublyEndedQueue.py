# Doubly ended Queue
class DoublyEndedQueue(object):
    def __init__(self):
        self.queue = []
    # return True if stack is empty
    def isEmpty(self):
        return self.queue  == 0
    # add in front of queue
    def addFront(self,data):
        self.queue.append(data)
    # add in rear of queue
    def addRear(self,data):
        self.queue.insert(0,data)
    # remove from front
    def removeFront(self):
        return self.queue.pop()
    # remove rear
    def removeRear(self):
        return self.queue.pop(0)