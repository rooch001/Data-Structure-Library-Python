# Queue Data Structure Implemented by arrays
# Queue - FIFO - First In First Out
class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = -1
        self.size = 0
    # method insert value in queue (FIFO)
    def enQueue(self,data):
        if self.size == 0:
            self.queue.append(data)
            self.front = data
            self.size += 1
        else:
            self.queue.append(data)
            self.rear = data
            self.size += 1
    # method removes element from the first position of Queue (FIFO) and return the value
    def deQueue(self):
        if self.size <=0:
            return "Queue Underflow"
        self.front = self.queue[0]
        self.size -= 1
        return self.queue.pop(0)
    # method return Rear Element of Queue
    def queueRear(self):
        return self.rear
    # method return Front Element of Queue
    def queueFront(self):
        return self.front
    # method return Length of Queue
    def length(self):
        return self.size
    # special method used to print Queue elements (array)
    def __str__(self):
        return str(self.queue)
    