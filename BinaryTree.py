#BINARY TREE
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
    def set_data(self,data):
        self.data = data
    def set_right(self,value):
        self.right = value
    def set_left(self,value):
        self.left = value
    def get_data(self):
        return self.data
    def get_right(self):
        return self.right
    def get_left(self):
        return self.left
    def get_parent(self):
        return self.parent
    def set_parent(self,value):
        self.parent = value
              
class BinaryTree:
    def __init__(self):
        self.root = None
        self.maxEle = 0
    # insert value in binary tree
    def insert(self,data):
        if self.root == None:
            self.root = Node()
            self.root.set_data(data)
        else:
            self._insert(self.root,data)
    def _insert(self,current,value):
        if value < current.get_data():
            if current.get_left() == None:
                current.set_left(Node()) 
                current.get_left().set_data(value)
                current.get_left().set_parent(current) 
            else:
                self._insert(current.get_left(),value)
        elif value >= current.get_data():
            if current.get_right() == None:
                current.set_right(Node())
                current.get_right().set_data(value)
                current.get_right().set_parent(current)
            else:
                self._insert(current.get_right(),value)
    # preorder traversal 
    def printPreorder(self):
        self._printPreorder(self.root)
    def _printPreorder(self,current):
        if current == None:
            return
        print(current.get_data())
        self._printPreorder(current.get_left())
        self._printPreorder(current.get_right())
    # inorder traversal
    def printInorder(self):
        self._printInorder(self.root)
    def _printInorder(self,current):
        if current == None:
            return 
        self._printInorder(current.get_left())
        print(current.get_data())
        self._printInorder(current.get_right())
    # post order traversal
    def printPostorder(self):
        self._printPreorder(self.root)
    def _printPostorder(self,current):
        if current == None:
            return 
        self._printPostorder(current.get_left())
        self._printPostorder(current.get_right())
        print(current.get_data())  
    # returns max element
    def maxElement(self):
        return self._maxElement(self.root)
    def _maxElement(self,current):
        if not current:
            return self.maxEle
        if current.get_data() > self.maxEle:
            self.maxEle = current.get_data()
        self._maxElement(current.get_left())
        self._maxElement(current.get_right())
        return self.maxEle
        