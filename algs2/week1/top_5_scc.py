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
threading.stack_size(67108864)


def main():
    
    

#!!!!!!!!!!!!!!   LOOK INTO THIS
thread = threading.Thread(target = main)
thread.star()
#!!!!!!!!!!!!!!


"""
dfs:
run depth first search on a directed graph, also implementing the variables
needed to find the strongly connected components using Kosaraju's 
well known Two-Pass Algorithm
"""
def dfs( graph g, node i ):
    g.setExplored(i)
    for j in g.getVertex(i):
        if( !g.visited(j) ):
            dfs(g, j)
    g.setOrder( i , t )
    g.incrementOrder()

"""
dfs_loop
2nd part of Kosaraju's well known Two-Pass DFS algorithm for finding strongly
connected components in a directed graph.
"""
def dfs_loop( graph g ):
    g.setOrder( 0 )
    g.setLeader( NULL )
    
    for i in g.getVertices():
        if( !g.visited(i) ):
            g.setLeader(i)
            dfs(g, i)


# ============================    Define Classes to Use    ==========================#

"""
Node Class
create class for each node of a graph, g
Data:     name, 
          leader (for kodaraju's two-pass scc algorithm), 
          order ( for kodaraju's two-pass scc algorithm ),
          edges: list of edges that leave it
          visited: boolean for whether or not the node has been visited

Functions:
          _init_(num)
          setLeader
          setOrder
          setVisited
          getLeader
          getOrder
          getVisited
"""
class Node:
    name = None
    leader = None
    order = None
    edges = []
    
    
    def __init__(self, numName )
        self.name = numName
        self.leader = None
        self.order = 



    

            
            