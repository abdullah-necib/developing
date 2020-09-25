#this program is used to generate the couples of even groups 2 x 2
from itertools import combinations
from time import time

def test_length(*args, n):#old way and useless
    """if the length of args == n return true"""
    result = []
    for i in args:
        if i[0] not in result :
            result.append(i[0])
        if i[1] not in result:
            result.append(i[1])
    return len(result) == n

def find_couples_by_remove(N = 6):#old way and useless
    """generate all combinations then eliminate unmatched elements for couples"""
    original = list(combinations(range(N),2))
    all_comb = list(combinations(original,int(N/2)))
    result = []
    for i in all_comb:
        if test_length(*i,n = N):
            result.append(i)
    return result

def couples(N= 6):
    """find a couples in fatest way"""    
    length = 1#this is the length of the result
    for i in [x for x in range(3,N,2)]:        
        length *= i
    
    print(length)

#test1/2: create all combinations then eliminate the not required elements:
start = time()    
for i in find_couples_by_remove(N=8):
    print(i)
print('finished')
print('{:.3f}'.format(time()-start))

couples(8)
