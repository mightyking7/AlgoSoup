'''
    Driver program that creates a Graph
    with vertices and utilizes Dijkstras
    algorithm to compute the shortest path
    from a source to each vertex.

    Isaac Buitrago
'''


from Graph import *
from Vertex import *

# Graph of nodes
graph = Graph()


'''
    Create Vertices.txt
'''
def main():

    src = None

    # create empty graph
    graph = Graph()

    # parse vertices, add them to the graph
    file = open("Vertices.txt", 'r')

    while True:

        line = file.readline()

        if line == "":
            break

        vertices = line.strip().split()

        for v in vertices:

            graph.addVertex(v)

    # parse connections, create connections in the graph
    file = open("Connections.txt", 'r')

    lineNum = 1

    while True:

        line = file.readline()

        if line == "":
            break

        (v1, w, v2) = line.strip().split()

        # save starting node for Dijkstra's shortest path algorithm
        if lineNum == 1:
            src = v1

        # add the weight to the graph,
        # throws an exception if vertex is not valid.
        try:
            graph.addWeight(v1, v2, int(w))

        except InvalidVertex as e:
            print(e.args[0])

        except ValueError:
            print("The given weight is not an integer")

        lineNum += 1


    graph.printGraph()

    graph.dijkstras(src)


main()
