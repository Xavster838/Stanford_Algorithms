#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:49:12 2018

@author: XaviGuitart
"""

def recursive_mult( in1 , in2 ):
    
    len1 = len( str(in1) )
    len2 = len( str(in2) )
    
    #basecase: n or m == 1
    if( len1 == 1 or len2 == 1):
        return int(in1) * int(in2)
    
    n = max(len1, len2)
    nHalf = n//2

    a =  in1 // (10**nHalf) 
    b =  in1 % (10**nHalf) 
    c =  in2 // (10**nHalf) 
    d =  in2 % (10**nHalf) 
    
    #recursive calls
    ac = recursive_mult(a , c)
    bd = recursive_mult(b , d)
    z = recursive_mult( a + b  ,  c + d)
    last = int(z) - int(ac) - int(bd)
    
    answer = ( ((10 ** (nHalf*2)) * int(ac)) + ((10 ** ( int(nHalf) ) ) * last) + bd)
    
    if( answer != in1 * in2 ):
        print(" NONONONO \n")
        print(' Missed Calculation: a: ' + str(a) + '. b: ' + str(b) + 
                         '. c: ' + str(c) + '. d: ' + str(d) + '.')
        print('\n')
        print ('in1: ' + str(in1) + 'in2: ' + str(in2))
        
        print('/n')
        print(' my answer: ' )
    
    return answer


c1 = 3141592653589793238462643383279502884197169399375105820974944592
c2 = 2718281828459045235360287471352662497757247093699959574966967627

print( recursive_mult( c1 , c2 ) )



ans = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184



