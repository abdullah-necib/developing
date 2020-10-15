from itertools import permutations 
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
   



# print(type(perm_a_2))


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
def shooting():
    hit = [1  for x in range(20)]    
    # suppose there is fails like 0 in the following place
    hit[2]=hit[6]=hit[9]=hit[14]=hit[19] = 0    
    event_prob = [sum(hit[0:i])/i  for i in range(1,len(hit)+1) ]
    for i in range(len(hit)):
        print(f'{i+1} :   {hit[i]} ==> '+'{0:.3f}'.format(event_prob[i]))
    pyplot.plot(list(range(20)),event_prob)
    pyplot.show()


def fun(a):
    return 0.5*(2/3)**a

def test_random_variable_exchange():
    x = [a for a in range(1,11)]
    fx = [a/55 for a in x]
    Fx = [sum(fx[0:i]) for i in x]
    Fx2 = [a*(a+1)/110 for a in x]
    y = [3*a +2 for a in x ]
    fy = [(a-2)/165 for a in y]
    Fy = [sum(fy[0:i]) for i in range(1,11)]
    Fy2 = [(a-2)*(a+1)/990 for a in y]
    
    print(f'x list is:\n{x}\n')
    print(f'fx list is:\n{fx}\n')
    print(f'Fx list is:\n{Fx}\n')
    print(f'Fx2 list is:\n{Fx2}\n')
    
    print(f'y list is:\n{y}\n')
    print(f'fy list is:\n{fy}\n')
    print(f'Fy list is:\n{Fy}\n')
    print(f'Fy2 list is:\n{Fy2}\n')
    print(40*'-')
    from scipy.stats import describe
    print(f'description of fx: {describe(fx)}\n\n')
    xMean_base = [x[i]*fx[i] for i in range(10)]
    print(xMean_base)
    print(sum(xMean_base))
    print(sum(fx))
    print(40*'-')
    
    
# test_random_variable_exchange()


def test_generating_random_var(choices, probablities, repeat=100):
    from numpy.random import choice
    result =[]    
    for i in range(repeat):
        result.append(choice(choices,p= probablities))
    for i in choices:
        print(f'for the choice: {i} it is repeated {result.count(i)}')
    from scipy.stats import describe
    print(describe(result))
        
    
# test_generating_random_var([1,2,3], [0.3,0.5,0.2],1000)

def test_bernoulli():
    from scipy.stats import bernoulli
    p=0.5
    mean, var, skew, kurt = bernoulli.stats(p,moments='mvsk')
    print(f'mean ={mean}')
    print(f'variance= {var}')
    print(f'Skew = {skew}')
    print(f'kurt = {kurt}')


# test_bernoulli()

def test_binomial():
    from scipy.stats import binom
    n=3
    p=5/15
    r_values = list(range(n+1))
    mean, var = binom.stats(n,p)
    dist = [binom.pmf(r,n,p) for r in r_values]
    for i in range(n+1):
        print(f'{r_values[i]} \t {dist[i]}')
    print(f'Mean = {mean}')
    print(f'var = {var}')
    pyplot.plot(r_values, dist)
    
# test_binomial()

def test_poission(u):
    from scipy.stats import poisson
    r_values = list(range(10))
    dst = poisson.pmf(r_values, u)
    for i in r_values:
        print(f'{i} >>> {dst[i]}')
    pyplot.plot(r_values, dst)
    return dst
    
# print(1-sum(test_poission(3)[:3]))



# =============================================================================
# Start with continues distributions
# =============================================================================

def c_uniform():
    from scipy.stats import uniform
    z = uniform(0,12)
    print(z.stats())
    print(z.mean())
    print(z.var())
    print(z.cdf(5))

# c_uniform()

# this is not negative exponent dist but it may be transfer
def c_negative_exp():
    from scipy.stats import expon
    z = expon(0.5)
    print(z.mean())
    print(z.var())
    
    
# c_negative_exp()

def c_normal_disc():
    from scipy.stats import norm
    x = [a/100 for a in range(-1000,1000)]
    z= norm()
    y = [z.pdf(a) for a in x]

    # pyplot.plot(x,y)
    print(z.mean())
    print(z.var())
    print(z.cdf(1.57))
    print(z.cdf(1.28)-z.cdf(-2.01))
    print(z.ppf(0.975)*30+80)
    
c_normal_disc()