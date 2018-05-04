#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:11:01 2018
MergeSort
Stanford Algorithms Assignment 3
Description:quicksort algorithm
Input:array of distinct characters
Output: sorted array and number of comparisons


@author: XaviGuitart
"""



'''
quickSort
Body function for quickSort Algorithm

'''
checkCount = 0

def quickSort( quickObj, size, r, l = 0 ):
    #base case n <=1
    if (size <= 1): 
        return quickObj
    global checkCount
    #first choose pivot
    p = choosePivot( quickObj.A, l, r )
    #preprocess: swap pivot element with leftmost element
    swap(quickObj.A, l , p)
    #partition
    partPoint = quickObj.partition( l, r )
    #quickSort further 2 halves
    quickSort( quickObj, partPoint - l , partPoint, l )
    quickSort( quickObj, r - (partPoint + 1), r, partPoint+1)


class quickSortA:
#    A = []
#    numComp = 0   
    def __init__(self, inst):
        self.A = inst
        self.numComp = 0

    def partition( self, l, r ):
        #Add size of subArray to numc comparisons
        self.numComp += r - l - 1
        #i = divider between less than left and greater than right
        i = l + 1
        pivot = self.A[l]
        for j in range((l+1),r) :
            if( self.A[j] < pivot ):
                swap(self.A, i, j)
                i += 1
            #else: do nothing
        swap( self.A, l, i-1 )
        return (i-1)

"""
Swap
"""
def swap( A, i, j ):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

"""
choosePivot
"""
def choosePivot( A, l, r ):
    #return chooseFirst( l, r )
    #return chooseLast( l, r)
    return chooseMed3( A, l, r)

def chooseRandom( l, r ):
    from random import randint
    return randint(l, r) 

def chooseFirst( l, r ):
    return l

def chooseLast( l, r ):
    return ( r - 1 )

def chooseMed3(inst, l, r):
    from numpy import median
    middle = (r - l) // 2 + l   
    if( ( r - l ) % 2 == 0 ):
        middle -= 1
    retNum = median( [ inst[l], inst[middle], inst[r-1] ] )
    if( inst[l] == retNum):
        return l
    elif( inst[middle] == retNum):
        return middle
    else:
        return r-1


"""
lineSepInput
Description: get data from line separated text files
             given by stanford algorithms class
Input:       line delimited text file
Ouput:       contents stored in an integer list
"""
def lineSepInput( textFile ):
    readIn = open( textFile , mode = 'r' )
    fileCont = []
    for line in readIn:
        fileCont.append( int(line) )
    return fileCont






