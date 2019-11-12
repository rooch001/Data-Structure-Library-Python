# Data-Structure-Library-Python
# Stack
```Python
class Stack(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  isEmpty(self)
 |      # method checks whether the stack is empty or not ; returns bool (True|False)
 |
 |  peek(self)
 |      # method returns top element of stack
 |
 |  pop(self)
 |      # method pop delets element from the first position of the array and return the element
 |
 |  push(self, element)
 |
 |  returnStack(self)
 |      # method return stack (self.array class variable: type:[List])
 |
 |  size(self)
 |      # method return the size of stack
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
 # Queue
 ```Python
 class Queue(builtins.object)
 |  # Queue Data Structure Implemented by arrays
 |  # Queue - FIFO - First In First Out
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __str__(self)
 |      Return str(self).
 |
 |  deQueue(self)
 |      # method removes element from the first position of Queue (FIFO) and return the value
 |
 |  enQueue(self, data)
 |
 |  length(self)
 |      # method return Length of Queue
 |
 |  queueFront(self)
 |      # method return Front Element of Queue
 |
 |  queueRear(self)
 |      # method return Rear Element of Queue
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

 ```
 # Stack using LinkedList: StackList
 ```Python 
 class StackList(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  isEmpty(self)
 |      # check whether stack is empty (returns Bool)
 |
 |  peek(self)
 |      # returns top element of stack
 |
 |  pop(self)
 |      # pop element from stack
 |
 |  printStack(self)
 |      # print Stack
 |
 |  push(self, data)
 |      # Push element into stack
 |
 |  size(self)
 |      # returns size of list
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

 ```
 # Singly Linked List
 ```Python
 class Node(builtins.object)
 |  # Linked list is an abstract data type
 |  # Successive elements are connected with pointers
 |  # last element is connected to null
 |  # can be grow or shrink during program execution
 |  # can be made as long as req until all memory is exhuasted
 |  # does not waste memory but still some memory is used to store pointers
 |  # head -> 4->15->7->40->NULL
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  get_data(self)
 |      # get data
 |
 |  get_next(self)
 |      # get next field
 |
 |  has_next(self)
 |      # returns true if node points to another node
 |
 |  set_data(self, data)
 |      # set data field
 |
 |  set_next(self, nxt)
 |      #set next field of node
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

Help on class SinglyLinkedList in module __main__:

class SinglyLinkedList(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  clear(self)
 |      # clear linked lists
 |
 |  delete_at_begining(self)
 |      # deletes at first position
 |
 |  delete_at_end(self)
 |      # deleting last position data
 |
 |  delete_at_position(self, position)
 |      # deleting any position data
 |
 |  insert_at_begining(self, data)
 |      # insert at first position of linked list
 |
 |  insert_at_end(self, data)
 |      # insert in end position of linked list
 |
 |  insert_at_position(self, position, data)
 |      # insert at any position of linked list
 |
 |  list_lenght(self)
 |      # returns length of list
 |
 |  print_list(self)
 |      # print list
 |
 |  reverse_list(self)
 |      # reversing the list
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
 # MinHeap
 ```Python
 class MinHeap(builtins.object)
 |  # same as max heap , only difference is the top element in the heap will be the minimum value
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  deleteMin(self)
 |
 |  getMinimum(self)
 |
 |  insert(self, element)
 |
 |  leftChild(self, index)
 |
 |  maxChild(self, index)
 |
 |  parent(self, index)
 |
 |  peek(self)
 |
 |  percolateDown(self, i)
 |
 |  percolateUp(self, i)
 |
 |  rightChild(self, index)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

 ```
 # MaxHeap
 ```Python
 class MaxHeap(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  deleteMax(self)
 |      # delete max
 |
 |  getMaximum(self)
 |      # return maximum
 |
 |  insert(self, element)
 |      # insert in heap
 |
 |  leftChild(self, index)
 |      # return left child
 |
 |  minChild(self, index)
 |      # returns minimum child
 |
 |  parent(self, index)
 |      # return parent
 |
 |  peek(self)
 |      # return Top element
 |
 |  percolateDown(self, i)
 |      # percolating down to satisfy heap property
 |
 |  percolateUp(self, i)
 |      # percolating up to satisfy heap property
 |
 |  rightChild(self, index)
 |      # return right child
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
 # Heapify, Heapsort, buildHeap function
 ```Python
 buildHeap(array)
    #build heap from an array

Help on function heapSort in module __main__:

heapSort(arr)
    # heap sort
 ```
 # Doubly Linked List
 ```Python
 class DoublyLinkedList(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  delete_at_begining(self)
 |      # delete in begining
 |
 |  delete_at_end(self)
 |      # delete in end
 |
 |  delete_at_position(self, position)
 |      # delete at position
 |
 |  insert_at_begining(self, data)
 |      # insert in the begining
 |
 |  insert_at_end(self, data)
 |      # insert in the end
 |
 |  insert_at_position(self, position, data)
 |      # insert at any position
 |
 |  print_list(self)
 |      # print list
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

 ```
 # Doubly Ended Queue:
 ```Python
 class DoublyEndedQueue(builtins.object)
 |  # Doubly ended Queue
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  addFront(self, data)
 |      # add in front of queue
 |
 |  addRear(self, data)
 |      # add in rear of queue
 |
 |  isEmpty(self)
 |      # return True if stack is empty
 |
 |  removeFront(self)
 |      # remove from front
 |
 |  removeRear(self)
 |      # remove rear
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)


 ```
 
 # Circular Linked List
 ```Python
 class CircularLinkedList(builtins.object)
 |  # Circular Linked List
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  delete_at_end(self)
 |      # delete at end position
 |
 |  delete_at_front(self)
 |      # delete from front
 |
 |  insert_at_end(self, data)
 |      # insert in end position
 |
 |  insert_at_front(self, data)
 |      # insert in front position
 |
 |  length(self)
 |      # return length of list
 |
 |  print_List(self)
 |      # print list
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 ```
 # Binary Tree
 ```Python
 class BinaryTree(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  insert(self, data)
 |      # insert value in binary tree
 |
 |  maxElement(self)
 |      # returns max element
 |
 |  printInorder(self)
 |      # inorder traversal
 |
 |  printPostorder(self)
 |      # post order traversal
 |
 |  printPreorder(self)
 |      # preorder traversal
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

 ```
