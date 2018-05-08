#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:07:34 2018
top_5_scc.py
find top 5 Strongly Connected Components of a given directed graph
@author: XaviGuitart
"""

#============================   First change system settings to allow for deeper recursion   ===============================#
import sys,threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)            #Set the thread stack size


def main():
    #1: get Graph
    #2: create order function
    #3: run through first loop of Kosaraju's algorithm
    #   hold onto new order
    #:  get forward graph
    #:  run DFS again but with correct order
    
    #test graph
    pathToTextFile = "../test_graph_test.txt"
    test1 = Graph(textFile)
    node1 = test1.getNode[0]
    #check if correct
    print(node1.getEdges())
    

#!!!!!!!!!!!!!!   LOOK INTO THIS
thread = threading.Thread(target = main)   #Tells computer to thread the targetted function main
thread.start()                             #Tells computer to start the new thread
#!!!!!!!!!!!!!!


##=================== TEST  =================#
import os
from os import path
basepath = os.getcwd()
textFile = "test_graph_text"
textFile = path.abspath(path.join(basepath, "..", textFile))
f = open( textFile, "r")
f.close()

##=================== TEST  =================#

# ============================    Define Classes to Use    ==========================#

"""
Node Class
create class for each node of a graph, g
Data:     
          name:  numerical value index
          leader (for kodaraju's two-pass scc algorithm), 
          edges: list of edges that leave it

Functions:
          _init_(num)
          setLeader
          getLeader
          addEdge
          getEdges
"""
class Node:
    name = None
    leader = None
    edges = []
    def __init__(self, numName, edge):
        self.name = numName
        self.edges.append(edge)
        
    def setLeader(self, inst):
        self.leader = inst        
    def addEdge(self, inst):
        self.edges.append(inst)
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
""" 
class Graph:
    _nodes = []
    _visited = None
    
    def __init__(self, graph_text, isRev=False):
        
        readIn = open( graph_text , mode = 'r' )
        isRev = 1 * isRev                                # 0 if false, 1 if True
        for line in readIn:
            #line vertices and edges stored at line[0] and line[2]
            #node and edge defined by whether reading in Graph or GraphRev
            #Implement logic to do this for us
            nodeName = int( line[ 2 * (isRev % 2) ])           #Logic for new node
            edgeName = int( line[2 * ((1 + isRev) % 2)] )      #Logic for new Edge
            
            #check if node exists
            if(nodeName < len(self._nodes)):
                self._nodes[nodeName].addEdge(edgeName)
            else:
                newNode = Node( nodeName, edgeName )
                self._nodes.append( newNode )
            
        #once done getting all lines --> create boolean for visited
        self.visited = [False] * len(self._nodes)

        
    def addNode(self, newNode):
        self._nodes.append( newNode )
    
    def getNode(self,n):
        return self._nodes[n]
    def reset(self):
        self._visited = [False] * len(self._nodes)
    
#========================    Define Functions    =======================#            

"""
dfs:
run depth first search on a directed graph, also implementing the variables
needed to find the strongly connected components using Kosaraju's 
well known Two-Pass Algorithm
"""
def dfs( G, i):
    #edge case: not passing graph or integer
    if not isinstance(G, Graph):
        raise RuntimeError("instance", G, "not of class Graph")
    if( not isinstance(i, int)):
        raise RuntimeError("instance ", i, "not an integer")
    G.setExplored(i)
    t = 0
    for j in G.getVertex(i):
        if( not G.visited(j) ):
            dfs(G, j)
    order[i] = t 
    t += 1

"""
dfs_loop
2nd part of Kosaraju's well known Two-Pass DFS algorithm for finding strongly
connected components in a directed graph.
"""
def dfs_loop( G ):
    graphLen = len(G.getNodes())
    order = range( 0, graphLen )
    if( not isinstance(G, Graph) ):
        raise RuntimeError("instance", G, "not of class Graph")
    G.setOrder( 0 )
    G.setLeader( None )
    
    for i in G.getVertices():
        if( not G.visited(i) ):
            G.setLeader(i)
            dfs(G, i)
