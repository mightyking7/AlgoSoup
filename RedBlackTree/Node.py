
'''
Node in a red black tree that stores a value.
It has color, a left, right, and parent pointer.

Isaac Buitrago
'''

class Node:

    def __init__(self, key, color):

        self.parent = None

        self.left = None

        self.right = None

        self.key = key

        self.color = color


    def __str__(self):

        return str(self.key)