
import InvalidVertex

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


    '''
        Return:
            The string representation of the Vertex
    '''
    def __str__(self):

        return self.id

    '''
        
        Purpose:
            Generator function that provides the
            next vertex in the adjacency list for each Vertex
            
        Parameters:
        
        Notes:
        
        Return:
    '''
    def getConnections(self):

        for v in self.adj.keys():

            yield v

    '''
        Purpose:
            Adds the neighbor with an associated weight
            to the adjacency dictionary for the vertex

        Parameters:
            nbr - Neighbor to add to the adjacency dictionary
            weight - Weight of edge to neighbor
            
        Return:
            void
    '''
    def addNeighbor(self, nbr, weight=0):

        self.adj[nbr] = weight

    '''

        Purpose:
            Returns the weight of the edge to the neighbor

        Parameters:
            nbr - Neighbor of vertex

        Notes:
            Raises InvalidVertex if the vertex is not a neighbor
            
        Return:
            weight of edge to neighbor
    '''
    def getWeight(self, nbr):

        weight = self.adj.get(nbr, None)

        if weight == None:
            raise InvalidVertex("%s is not a neighbor of %s" %(nbr, self))

        return weight

    '''
        Purpose:
            Get the id of the Vertex
        Parameters:
        
        Return:
            void
    '''
    def getId(self):

        return self.id




