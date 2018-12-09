'''
    Driver program that creates a Graph
    with vertices and utilizes Dijkstras
    algorithm to compute the shortest path
    from a source to each vertex.
'''


import sys
from Graph import *
from Vertex import *

def main():

    v1 = Vertex("A")

    v2 = Vertex("B")

    v3 = Vertex("C")

    l = []

    v1.addNeighbor(v2, 4)

    v1.addNeighbor(v3, 8)

    v3.addNeighbor(v2, 2)

    l.append(v1)
    l.append(v2)
    l.append(v3)

    graph = Graph(l)


    graph.dijkstras(v1)


main()