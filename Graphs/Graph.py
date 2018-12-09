
import sys
from Vertex import *

'''
Graph with vertices
'''
class Graph:

    # constructor for Graph
    def __init__(self, vertices):

        self.vertices = vertices                        # list of vertices in graph

        self.sptSet = {key: False for key in vertices}  # Shortest path tree set

    '''
        Purpose:

        Parameters:

        Notes:

        Return:
    '''
    def addVertex(self, key):

        v = Vertex(key)

        self.vertices.append(v)

    '''
    Computes index of vertex with minimum distance from
    vertex that is not already in SPT set.
    '''
    def minDistance(self, dist):

        minDistance = sys.maxsize

        # find vertex with shortest distance not in SPT set
        for i, v in enumerate(self.vertices):

            if self.sptSet[v] == False and dist[v] < minDistance:

                minDistance = dist[v]

                minIndex = i

        return minIndex

    '''
        Purpose:
            Compute the shortest path 
            from source to sink for each vertex 
            in the graph.
      
        Parameters:
            src - source vertex
            
        Notes:
            
        Return:
            List of shortest path from the source to the sink
    '''
    def dijkstras(self, src):

        # distance from src for each vertex
        dist = {key: sys.maxsize for key in self.vertices}

        # init src to zero
        dist[src] = 0

        # find the shortest path for each vertex
        for i, value in enumerate(self.vertices):

            # obtain index of vertex the minimum distance
            u = self.minDistance(dist)

            # update distance for each adjacent vertex
            vertex = self.vertices[u]

            # iterate over adjacent vertices
            for v in vertex.getConnections():

                if self.sptSet[v] == False and dist[v] > dist[vertex] + vertex.getWeight(v):

                    dist[v] = dist[vertex] + vertex.getWeight(v)


        self.printSolution(dist)


    '''
        Purpose:
            Compute the shortest path 
            from source to sink for each vertex 
            in the graph.
      
        Parameters:
            src - source vertex
            
        Notes:
            
        Return:
            List of shortest path from the source to the sink
    '''
    def printSolution(self, dist):

        print("Vertex\tDistance")

        for k, v in dist.items():

            print("%s\t%d" %(k, v))
