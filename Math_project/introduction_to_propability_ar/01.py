from itertools import permutations 
import numpy as np


def have(x,y):
    """ does x have y inside it or not and should have the same index as well"""
    for i in y:
        if i not in x or (i in x and x.index(i) != y.index(i)):
            return False
    return True
base_a = ['a1','a2','a3','a4','a5']

perm_a = permutations(base_a)
perm_a_2 = list(permutations(base_a,2))
print(type(perm_a_2))


# cnt = 0
# for i in perm_a:
#     cnt += 1
#     print(f'{cnt} value is: {i}')
# cnt = 0
# for i in perm_a_2:
#     cnt +=1s
#     print(f'{cnt} value is: {i}')

# cnt = 0
# idx = 2
# for i in perm_a:
#     if have(i, perm_a_2[idx]):
#             cnt += 1
#             print(f'{cnt} {perm_a_2[idx]} inside: {i}')
            
            
            
# برنامج بسيط لحساب المتوسط للاصاية للهدف لاستخراج
# احتمالية اصابة الهدف من مدفعية

hit = [1  for x in range(20)]

# suppose there is fails like 0 in the following place
hit[2]=hit[6]=hit[9]=hit[17]=0

event_prob = [sum(hit[0:i])/i  for i in range(1,len(hit)+1) ]
for i in range(len(hit)):
    print(f'{i+1} :   {hit[i]} ==> '+'{0:.3f}'.format(event_prob[i]))

import matplotlib.pyplot as pyplot

pyplot.plot(list(range(20)),event_prob)
pyplot.show()


