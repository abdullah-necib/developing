#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 05:23:19 2020

@author: abdullah
"""
from math import factorial
from itertools import combinations
from itertools import permutations
from itertools import product

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
    
    
def question_1a():
    base = list(range(1,7))
    mainlist = [[a,b,c,d] for a in base for b in base for c in base\
                for d in base]
    set21 = []
    set22 = []  
    for item in mainlist:    
        if sum(item) == 21: set21.append(item)        
        if sum(item) == 22: set22.append(item)
    fprint(set21)
    print(len(set21))
    fprint(set22)
    print(len(set22))
    
def question_1b():
    x = [chr(a) for a in range(65,91)]
    main2 = [a+b for a in x for b in x]
    main3 = [a+b for a in x for b in main2]
    cnt2 = 0
    cnt3 = 0
    for i in main2:
        if i[0]==i[-1]: cnt2 +=1
    for i in main3:
        if i[0]==i[-1]: cnt3 +=1
    print(cnt2)
    print(cnt2/len(main2))
    print(cnt3)
    print(cnt3/len(main3))

def question_2():
    base = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    types = ['D','H','C','S']
    types.sort()
    use2of4type = [list(a) for a in combinations(types, 2)]
    fprint(use2of4type)
    
    main = [a+b for a in types for b in base]
    space = [list(a) for a in combinations(main, 5)]
    # space = list(combinations(main,5))
    def test_a(item):
        result = True
        for element in item:
            if element[0] != item[0][0]:
                return False
            if element[-1] in ('A','0','J','Q','K'):
                return False
        return result
    def test_b(item):
        result = True
        string = ''.join(item)
        # print(string)
        if string.count('A') != 1:
            return False
        cond=[]
        for element in item:            
            if element[-1] == 'A': item.remove(element)
            else:     
                cond.append(element[0])
        
        cond.sort()
        if cond not in use2of4type:
            return False
            
        return result
    event_a =[x for x in space if test_a(x)]
    # fprint(event_a)
    print(len(event_a)/len(space))
 
        
    
# question_2()  akk is wrong

def zrief():
    result = 0
    for i in range(0,5):
        x = comb(6,i)*comb(4,4-i)/comb(10,4)
        result += x
        print(f'{i} {x} {result}')
    return result

def rBall_nBox(r,n):
    base = [x for x in range(r+1)]
    main_space = [list(x) for x in product(base,repeat = n) if sum(list(x))== r]
    fprint(main_space)


# for i in range(2,6):
    # rBall_nBox(6,i)


# for i in range(15):
#     temp = []
#     for j in range(i+1):
#         temp.append(comb(i,j))
#     print(str(temp))

rBall_nBox(7,3)

f = lambda x: comb(6,x)*(1/6**x)
print(f(2))