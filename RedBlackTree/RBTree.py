
from Node import *
import Colors

'''
Red black tree that stores nodes, performs rotations,
and stores a pointer to the root of the tree

Isaac Buitrago
'''
class RBTree:

    '''
        Purpose:
            Constructor for Graph
    '''
    def __init__(self):

        self.nil = None

        self.root = self.nil


    def insert(self, key):

        y = self.nil

        x = self.root

        # create the new node
        z = Node(key, Colors.RED)

        while x != self.nil:

            y = x

            if z.key < x.key:

                x = x.left

            elif z.key > x.key:

                x = x.right

        # set the parent of the new node
        z.parent = y

        # inserted into empty Tree
        if y == self.nil:

            self.root = z

        elif z.key < y.key:

            y.left = z

        else:
            y.right = z

        self.insertFixup(z)


    def insertFixup(self, node):

        # while the the parent is red, their may be an imbalance
        while node.parent.color == Colors.RED:

            # if on left branch of grandparent
            if node.parent == node.parent.parent.left:

                y = node.parent.parent.right

                # case 1, recolor parent and uncle
                if y != self.nil and y.color == Colors.RED:

                    y.color = node.parent.color = Colors.BLACK

                    node.parent.parent.color = Colors.RED

                    node = node.parent.parent

                #case 2, perform left rotation
                elif node == node.parent.right:

                    node = node.parent

                    self.leftRotate(node)

                # case 3, perform right rotation and recolor nodes
                node.parent.color = Colors.BLACK

                node.parent.parent.color = Colors.RED

                self.rightRotate(node.parent.parent)

            # on the right branch of grandparent
            else:

                y = node.parent.parent.left

                # case 1, recolor parent and uncle
                if y != self.nil and y.color == Colors.RED:

                    y.color = node.parent.color = Colors.BLACK

                    node.parent.parent.color = Colors.RED

                    node = node.parent.parent

                # case 2, perform left rotation
                elif node == node.parent.left:

                    node = node.parent

                    self.rightRotate(node)

                # case 3, perform right rotation and recolor nodes
                node.parent.color = Colors.BLACK

                node.parent.parent.color = Colors.RED

                self.leftRotate(node.parent.parent)

        self.root.color = Colors.BLACK











