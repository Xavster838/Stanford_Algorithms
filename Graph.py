#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:55:48 2018
Node Class
create class for each node of a graph, g
Data:     
          name:  numerical value index
          leader (for kodaraju's two-pass scc algorithm), 
          edges: list of edges that leave it
                 initially null because may add edges later as text file 
                 is random in the ordering of nodes/edges it lists

Functions:
          _init_(num)
          addEdge
          addEdges
          getEdges
          
@author: XaviGuitart
"""
class Node:
    def __init__(self, numName, edge=None):
        self.name = numName
        self.edges = [edge]
    
    def addEdge(self, inst):
        self.edges.append(inst)
    def addEdges(self, newEdges):
        self.edges.extend(newEdges)
    def getEdges(self):
        return self.edges



"""
Graph Class
create graph to store Nodes
Date:    list of nodes
         list of booleans checking if already seen
             Note: boolean list implemented to quickly reset the graph for situations
                   such as kosaraju's double pass algorithm
         list of order:
             List of how to run through 

Functions:
          _init_():    create graph or gRev from text file
          addNode()
          getGraph( string or other data structure of read text file) 
          getGrev( string or list of read text file )
              Note: gets input from input file in the opposite order of the regular graph
          getNode(n) : Access node n
          reset(): reset all visited to False

Possible Edge Cases:
    1. empty text file
    2. text file with wrong ordering (i.e. more than 2 indices per line)
        May be safe to assume this will never happen

@author: XaviGuitart
"""
class Graph:
    
    def __init__(self, graph_text, isRev=False):
        self.nodes = []
        self.visited = []
        readIn = open( graph_text , mode = 'r' )
        isRev = 1 * isRev                                # 0 if false, 1 if True
        for line in readIn:
            nodeName = int( line[ 2 * (isRev % 2) ])           #Logic for new node
            edgeName = int( line[2 * ((1 + isRev) % 2)] )      #Logic for new Edge
            
            if( nodeName < len(self.nodes) ):
                #need to add plural edges
                # - 1 BECAUSE ZERO BASED INDEXING
                self.nodes[nodeName - 1].addEdges( edgeName )
            else:
                #USE LIST COMPREHENSION
                newNodes = [ Node(count) for count in range(len(self.nodes) + 1, nodeName) ]
                self.nodes.extend( newNodes )
                newNodes[nodeName - 1].addEdge(edgeName)
        #once done getting all lines --> create boolean for visited
        self.visited = [False] * len(self.nodes)

        
    def addNode(self, newNode):
        self.nodes.append( newNode )
    
    def getNode(self,n):
        return self.nodes[n]
    def reset(self):
        self.visited = [False] * len(self.nodes)


###         Test      ###
test = Graph('/Users/XaviGuitart/Documents/computer_science/stanford_algorithms/algs2/test_graph_text.txt')

