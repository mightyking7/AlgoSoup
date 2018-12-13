from RBTree import *
import sys

print("Welcome\nThis program allows you to create nodes,\ndelete nodes, and search for nodes in a Red Black Tree.\n")

rbTree = RBTree()

print("Red Black Tree created\n")

while True:

    key = input("Input key value to insert in the tree, 'q' to quit operation: ")

    if key == 'q':

        print("\nGoodbye")

        break

    else:

        try:
            key = int(key)

            rbTree.insert(key)

        except ValueError as e:

            print("Key must be a whole integer")

