#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Random_Contraction_Algorithm
Description:
    given a text file of inputs representing an adjacency list,
    compute the minimum cut and return the number of crossing edges.
    
Further Notes:
    part 4 of Stanford Algorithms course offered on Coursera.

Created on Fri Mar 23 16:10:21 2018
@author: XaviGuitart
"""

#Class Vertex
#represents a vertex of a graph in the form of an adjacency list
#data: v: list representing the initial vertex and any other vertices contracted
#         with it
#      e: list of edges incident to the vertex.
from numpy import setdiff1d
class vertex:
    def __init__(self, inst.v, inst.e):
        self.v = [v]
        self.e = {e}
    
    def merge(v2):
        #add vertices such that no duplicates
        self.v = list( set(self.v + v2.v) ) 
        # add edges and remove self loops
        #note: parallel edges are alright
        self.e += v2.e
        self.e = setdiff1d(self.e, self.v, assume_true = True)


def random_contraction( adj_list ):
    size = len(adj_list.v)
    #Edge_case: 0 or 1 node
    if(size <= 1):
        print("graph size less than 1: too small")
        return 0
    
    while( size > 2 ):
        #pick random vertex and edge from that vertex
        curV = chooseRandom(size - 1)
        curE = chooseRandom( len(adj_list.e)-1 )
        #merge
        curV.merge(curE)
        
        #need to delete edge from adj_list
        adj_list.pop(curE)
        #be careful of losing edges here
        
    
def chooseRandom( r, l=0 ):
    from random import randint
    return randint(l, r)


def textInput( textFile ):
    






        
    
    
