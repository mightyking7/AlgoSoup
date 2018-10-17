'''
Red black tree that stores a pointer to the
head of the red black tree.
'''

import Node
import Color


class RBTree:

    nil = Node()

    def __init__(self):

        self.head = Node()

        # set nil shared by all nodes in the tree

        nil.color = Color.BLACK
        nil.left = None
        nil.right = None
        nil.parent = None


    def insert(self, node):







