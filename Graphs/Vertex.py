

'''
Vertex with a unique identifier and adjacency list

Isaac Buitrago
'''
class Vertex:

    # construct a node with an id and distance
    def __init__(self, id):

        self.id = id    # identifier

        self.adj = {}   # Mapping of adjacent Vertices
                        # to distance from current Vertex

    # returns the string representation of the Vertex
    def __str__(self):

        return self.id

    '''
        
        Purpose:
            Generator function that provides the
            next vertex in the adjacency list for the Vertex
    '''
    def getConnections(self):

        for v in self.adj.keys():

            yield v



    def addNeighbor(self, nbr, weight=0):

        self.adj[nbr] = weight


    def getWeight(self, nbr):

        return self.adj[nbr]


