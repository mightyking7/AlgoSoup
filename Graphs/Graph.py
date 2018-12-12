
import sys
import InvalidVertex
from Vertex import *

'''
Graph with vertices

Isaac Buitrago
'''
class Graph:


    '''
        Purpose:
            Constructor for Graph
    '''
    def __init__(self):

        self.vertices = {}  # Mapping of vertex Id to vertex

        self.sptSet = {}    # Shortest path tree set



    '''
        Purpose:
            Prints vertices in the graph and their associated weights
    '''
    def printGraph(self):

        print("%-10s %8s %10s" %("Vertex", "Weight", "Vertex"))

        for k, v in self.vertices.items():

            for nbr in v.getConnections():
                print("  %s           %d         %s" % (k, v.getWeight(nbr), nbr))

    '''
        Purpose:
            Creates a new vertex in the graph
            
        Parameters:
            key - key for the new vertex
    '''
    def addVertex(self, key):

        v = Vertex(key)

        self.vertices[key] = v

    '''
        Purpose
            Creates a connection with a weight 
            between two vertices in the graph.
            
        Parameters:
            src - Id of source vertex
            dest - Id of destination vertex
            weight - Weight between two vertices, must be an integer
    '''
    def addWeight(self, src, dest, weight=0):

        v1 = self.vertices.get(src, None)
        v2 = self.vertices.get(dest, None)

        if v1 == None:

            raise InvalidVertex("%s is not a vertex in the Graph" %(v1))

        elif v2 == None:

            raise InvalidVertex("%s is not a vertex in the Graph" %(v2))

        v1.addNeighbor(v2, weight)

    '''
        Purpose
            Computes index of vertex with minimum distance from
            source that is not in the SPT set.
            
        Parameters
            dist - list of distances from source vertex
            
        Returns:
            Id of the vertex with minimum distance from source
    '''
    def minDistance(self, dist):

        minDistance = sys.maxsize

        # find vertex with shortest distance not in SPT set
        for k in self.vertices.keys():

            if self.sptSet[k] == False and dist[k] < minDistance:

                minDistance = dist[k]

                minKey = k

        return minKey

    '''
        Purpose:
            Compute the shortest path from source 
            to each vertex of the graph.
      
        Parameters:
            src - source vertex to run algorithm on
            
        Notes:
            Prints solution once the algorithm is complete
            
        Return:
            List of shortest path from the source to the sink
    '''
    def dijkstras(self, src):

        # distance from src for each vertex
        dist = {key: sys.maxsize for key in self.vertices}

        # initialize the SPT set
        self.sptSet = {key: False for key in self.vertices}

        # init src to zero
        dist[src] = 0

        # find the shortest path for each vertex
        for i , j in self.vertices.items():

            # obtain key of vertex with the minimum distance
            key = self.minDistance(dist)

            # update distance for each adjacent vertex
            vertex = self.vertices[key]

            self.sptSet[vertex.getId()] = True

            # iterate over adjacent vertices
            for v in vertex.getConnections():

                vId = v.getId()

                vertexId = vertex.getId()

                if self.sptSet[vId] == False and dist[vId] > dist[vertexId] + vertex.getWeight(v):

                    dist[vId] = dist[vertexId] + vertex.getWeight(v)


        self.printSolution(dist)


    '''
        Purpose:
            Compute the shortest path from source to 
            sink for each vertex in the graph.
      
        Parameters:
            src - source vertex
            
        Notes:
            
        Return:
            List of shortest path from the source to the sink
    '''
    def printSolution(self, dist):

        print("%-10s %8s" %("Vertex", "Distance"))

        for k, v in dist.items():

            print("  %s           %d" %(k, v))
