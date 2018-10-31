'''
Node in a red black tree that stores a value.
It has color, a left, right, and parent pointer.
'''

NIL = 0

BLACK = 1

RED = 2

class Node:

    def __init__(self, value, color):

        self._parent = None

        self._left = None

        self._right = None

        self._value = value

        self._color = color


