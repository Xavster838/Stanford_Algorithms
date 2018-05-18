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
from Graph import Graph


def __main__():
    #1: get Graph
    #2: create order function
    #3: run through first loop of Kosaraju's algorithm
    #   hold onto new order
    #:  get forward graph
    #:  run DFS again but with correct order
    
    #test graph
    pathToTextFile = "../test_graph_text.txt"
    test1 = Graph(pathToTextFile)
    node1 = test1.getNode(0)
    #check if correct
    print(node1.getEdges())
    

#!!!!!!!!!!!!!!   LOOK INTO THIS
if __name__ == "__main__": 
    #Tells computer to thread the targetted function main
    thread = threading.Thread(target = __main__)   
    thread.start()
    #Tells computer to start the new thread
    __main__()                          
#!!!!!!!!!!!!!!


# ============================    Define Classes to Use    ==========================#
class Kosa_node(Node):
    
    #observe no need for __init__ because same data as regular node
    def setLeader(self, inst):
        self.leader = inst 
    def getLeader(self):
        return self.leader


class Kosaraju_Graph(Graph):
    
    def __init__(self, graph_text, isRev = False):
        Graph.__init__(self, graph_text)
        
    
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
