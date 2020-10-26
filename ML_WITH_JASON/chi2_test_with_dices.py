#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:37:24 2020

@author: abdullah
"""
import random as rd
from scipy.stats import chi2 as kai
count = 30
S = [(a,b,c,d) for a in range(1,7) for b in range(1,7)\
        for c in range(1,7) for d in range(1,7)]
    
exp1 = [rd.randrange(1,7) for i in range(count)]
exp2 = [rd.randrange(1,7) for i in range(count)]
exp3 = [rd.randrange(1,7) for i in range(count)]
exp4 = [rd.randrange(1,7) for i in range(count)]
exp = [x+y+z+b for x in exp1 for y in exp2 for z in exp3 for b in exp4]
event =list(set(exp))
obs = [exp.count(a) for a in event]

# print(f'\n\nevents are: {event}')
# print(f'Observations are: {obs}')
# pyplot.plot(event,obs)

# n = len(exp)
# rv = norm()
# print(rv.cdf(2))
expect = []
for i in range(len(event)):
    temp = [a for a in S if sum(a)==event[i]]
    expect.append(len(temp)*len(exp)/len(S))
    
chi_2 = [(1/expect[i])*(obs[i]-expect[i])**2 for i in range(len(obs))]

for i in range(len(event)):
    print('event: {0:2} Observaton: {1:6} Expectation: {2:8} chi2: {3:10.3f}'.\
          format(event[i],obs[i],expect[i],chi_2[i]))
        
print(f'\nsum of chi2 is: {sum(chi_2)}')

print(1-kai(len(obs)-1).cdf(sum(chi_2)))