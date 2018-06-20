# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:26:03 2017

@author: tenai
"""


'''
 BFS a graph traversal algorithm:
 properties: 
           -Visited vertex from source
           -Distance of vertext from source
           
           Queue-FIFO is used to implement BFS
           


# Given a Graph --- G = (V,E)

# Objects

Vertex: 
      name
      neighbors = list{}


Graph:


'''


class Vertex:
    
    def __init__(self, n):
        self.name = n
        self.neighbors = list()# Use list to  implement Graph
        self.distance = 9999 ## start with infinite distance
        self.color = 'black' # unvisited vertex with black color
        
    def add_neighbor(self, v):
        
        vset = set(self.neighbors) ## extract all neighbors
        
        if v not in vset:
            self.neighbors.append(v)
            self.neighbors.sort() # always store the vertex's neighbors as sorted lists


class Graph:
    
    vertices = {} #set of vertices of Graph
    
    def add_vertex(self, vertex):
        
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
            
    
    def add_edge(self, u, v):
        
        if u in self.vertices and v in self.vertices: # check if vertices belong to graphs
            
            for key, value in self.vertices.items(): ## loop through all vertices of graph
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
                    
    def print_graph(self):
        
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))
            
    
    ## now Implement BFS algorithm
    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
                self.vertices[v].distance = vert.distance + 1
                q.append(v)

        while len(q) > 0:
                u = q.pop(0)
                node_u = self.vertices[u]
                node_u.color = 'red'

                for v in node_u.neighbors:
                        node_v = self.vertices[v]
                        if node_v.color == 'black':
                                q.append(v)
                                if node_v.distance > node_u.distance + 1:
                                        node_v.distance = node_u.distance + 1
                    
        

## Using the Program
g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))
    

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DF', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
        
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
    
g.bfs(a)
g.print_graph()

