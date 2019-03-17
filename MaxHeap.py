class MaxHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0
    # return parent
    def parent(self,index):
        return index//2
    # return left child
    def leftChild(self,index):
        return 2*index
    # return right child
    def rightChild(self,index):
        return 2*index + 1
    # return maximum
    def getMaximum(self):
        if self.size == 0:
            return -1
        return self.heapList[1]
    # returns minimum child
    def minChild(self,index):
        if self.heapList[2*index] < self.heapList[2*index + 1]:
            return 2*index
        else:
            return 2*index+1
    # percolating down to satisfy heap property 
    def percolateDown(self,i):
        left = 2*i
        right = 2*i+1
        largest = i
        if len(self.heapList) > left and self.heapList[largest] < self.heapList[left]:
            largest = left
        if len(self.heapList) > right and self.heapList[largest] < self.heapList[right]:
            largest = right
        if largest != i:
            self.heapList[i],self.heapList[largest] = self.heapList[largest],self.heapList[i]
            self.percolateDown(largest)
           
    # percolating up to satisfy heap property 
    def percolateUp(self,i):
        if i//2 <= 0:
            return
        elif self.heapList[i] > self.heapList[i//2]:
            self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            self.percolateUp(i//2)


    # delete max 
    def deleteMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.percolateDown(1)
        return retval
    # insert in heap
    def insert(self,element):
        self.heapList.append(element)
        self.size += 1
        self.percolateUp(self.size)
    # return Top element
    def peek(self):
        return self.heapList[1]
        
    
