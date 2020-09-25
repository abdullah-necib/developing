import itertools as it
from math import factorial
import time

committies = [set(x) for x in it.combinations('abcdef',3)]
groups = list(it.combinations(committies,7))

def comb(n,m): return factorial(n)/(factorial(m)*factorial(n-m))

def cond(group):
    result = []
    for i in range(len(group)):
        for j in range(i+1,len(group)):
            if len(group[i].intersection(group[j])) == 1:
                result.append([group[i],group[j]])
                
    return result
        


def test(n):
    for i in groups:    
        con = cond(i)
        if len(con) == n:
            elements.append([i,con])
            

for i in range(1,20):
    print(i)
    start = time.time()
    elements = []
    test(i)
    print('there is {} elements'.format(len(elements)))
    print('{:.3f} sec'.format(time.time()-start))
    print(30*'--')
