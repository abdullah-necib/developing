#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 06:04:24 2020

@author: abdullah
"""

from itertools import combinations
from math import factorial

def comb(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

def birthday_problem(k):
    """this is from third licture in statistics 101 """
    return 1-factorial(365)/(factorial(365-k)*(365**k))

def comb_iteration(n):
    for i in range(n+1):
        print(comb(n,i))
def fprint(x):
    print(50*'-')
    count = 1
    for i in x:
        print(f'{count:3} >>  {i}')
        count +=1
    print(50*'-')
    
def fprint_with_set(x):
    print(50*'-')
    
    count = 1
    for i in x:
        temp = set(i)
        print(f'{count:3} >>  {i} >> {temp}')
        count +=1
    print(50*'-')
    
def remove_order_qty(S):
    """for this (a,a,b) == (a,b,b)"""
    sets = []
    result = []
    for i in S:
        if set(i) not in sets:
            sets.append(set(i))
            result.append(i)
    return sets, result

def remove_order(S):
    """for this (a,a,b) == (a,b,a) != (a,b,b)"""
    result = []
    for i in S:
        temp = i.copy()
        temp.sort()
        if temp not in result:
            result.append(temp)
    return result

X = ['a','b','c','d','e']
S5 = [[a,b,c,d,e] for a in X for b in X for c in X for d in X for e in X]
S4 = [[a,b,c,d] for a in X for b in X for c in X for d in X]
S3 = [[a,b,c] for a in X for b in X for c in X]
S2 = [[a,b] for a in X for b in X]
# =============================================================================
# case for equal k element for every set
# =============================================================================
S5_similar = [i for i in S5 if i[0]==i[1]==i[2]==i[3]==i[4]]
S4_similar = [i for i in S4 if i[0]==i[1]==i[2]==i[3]]
S3_similar = [i for i in S3 if i[0]==i[1]== i[2]]
S2_similar = [a for a in S2 if a[0] == a[1]]
# =============================================================================
# case for replacement but no order
# =============================================================================

fprint(S5_similar)
co = [list(a) for a in combinations(X, 5)]
difference = []
for i in remove_order(S5):
    if i not in remove_order(S5_similar) and i not in co:
        difference.append(i)
fprint(co)   
print('the differences are:')     
# fprint_with_set(difference)

difference_sub_2 = [i for i in difference if len(set(i)) == 2]
difference_sub_3 = [i for i in difference if len(set(i)) == 3]
difference_sub_4 = [i for i in difference if len(set(i)) == 4]
fprint_with_set(difference_sub_2)
fprint_with_set(difference_sub_3)
fprint_with_set(difference_sub_4)

    