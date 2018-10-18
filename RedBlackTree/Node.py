'''
Node in a red black tree that stores a value.
It has color, a left, right, and parent pointer.
'''

NIL = 0

BLACK = 1

RED = 2

class Node:

    def __init__(self):

        self.parent = None

        self.left = None

        self.right = None

        self.value = -1

    def setLeft(self, node):

        self.left = node

    def setRight(self, node):

        self.right = node

    def setParent(self, node):

        self.parent = node


