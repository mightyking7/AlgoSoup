'''
    Driver program that creates a Graph
    with vertices and utilizes Dijkstras
    algorithm to compute the shortest path
    from a source to each vertex.
'''


from Graph import *
from Vertex import *


'''
    Create Vertices
'''
def main():

    v1 = Vertex("A")

    v2 = Vertex("B")

    v3 = Vertex("C")

    v4 = Vertex("D")

    v5 = Vertex("E")

    # list of vertices
    l = []

    v1.addNeighbor(v2, 5)

    v1.addNeighbor(v3, 3)

    v2.addNeighbor(v5, 1)

    v2.addNeighbor(v4, 4)

    v3.addNeighbor(v4, 6)

    v3.addNeighbor(v5, 7)

    v5.addNeighbor(v4, 2)

    v5.addNeighbor(v2, 1)

    l.append(v1)
    l.append(v2)
    l.append(v3)
    l.append(v4)
    l.append(v5)

    graph = Graph(l)

    graph.dijkstras(v1)


main()