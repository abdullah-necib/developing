from itertools import permutations 
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from math import pi, e,sqrt, factorial
from numpy.random import choice
from scipy.stats import bernoulli,binom,poisson, uniform,norm , expon,gamma,chi2
from scipy.integrate import quad

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
    result =[]    
    for i in range(repeat):
        result.append(choice(choices,p= probablities))
    for i in choices:
        print(f'for the choice: {i} it is repeated {result.count(i)}')
    from scipy.stats import describe
    print(describe(result))
        
    
# test_generating_random_var([1,2,3], [0.3,0.5,0.2],1000)

def test_bernoulli():
    p=0.5
    mean, var, skew, kurt = bernoulli.stats(p,moments='mvsk')
    print(f'mean ={mean}')
    print(f'variance= {var}')
    print(f'Skew = {skew}')
    print(f'kurt = {kurt}')


# test_bernoulli()

def test_binomial():    
    n=5
    p=0.6
    r_values = list(range(n+1))
    mean, var = binom.stats(n,p)
    dist = [binom.pmf(r,n,p) for r in r_values]
    for i in range(n+1):
        print(f'{r_values[i]} \t {dist[i]}')
    print(f'Mean = {mean}')
    print(f'var = {var}')
    
    pyplot.plot(r_values, dist)
    print(sum(dist[:4]))
    
# test_binomial()

def test_poission(u):
    r_values = list(range(20))
    dst = poisson.pmf(r_values, u)
    
    for i in r_values:
        print(f'{i} >>> {dst[i]}')
    # pyplot.plot(r_values, dst)
    return dst
    
# print(1-sum(test_poission(6)[:17]))


# =============================================================================
# Start with continues distributions
# =============================================================================

def c_uniform():
    z = uniform(0,12)
    print(z.stats())
    print(z.mean())
    print(z.var())
    print(z.cdf(5))

# c_uniform()

# this is not negative exponent dist but it may be transfer
def c_negative_exp():
    z = expon(0.5)
    print(z.mean())
    print(z.var())
    
    
# c_negative_exp()

def c_normal_disc():
    x = [a/100 for a in range(-1000,1000)]
    z= norm()
    y = [z.pdf(a) for a in x]

    # pyplot.plot(x,y)
    print(z.mean())
    print(z.var())
    print(z.cdf(1.57))
    print(z.cdf(1.28)-z.cdf(-2.01))
    print(z.ppf(0.975)*30+80)
    
# c_normal_disc()

def factorial_Drowaing(n):
    x = [a for a in range(0,n+1)]    
    y = [factorial(a) for a in x]
    pyplot.plot(x,y)
    return y


def stirling_formala(n):
    from math import e, pi, sqrt
    return sqrt(2*pi*n)*((n/e)**n)

def test_fact_stirling(n):    
    a = factorial_Drowaing(n)[-1]
    b = stirling_formala(n)
    print(f'factorial({n}) = {a} stirling: {b} with {b/a}')
    
# for i in range(80):
#     test_fact_stirling(i)
    
    
def test_gamma_function(n):
    return quad(lambda x,n: (x**n)*(e**(-x))/x,0,np.inf,args=n)[0]

# a =test_gamma_fucntion(0.5)
# print(a[0]**2)
# print(pi)


def test_Euler_factorial(n):
    from scipy.integrate import quad
    return quad(lambda x,n: (x**n)*(e**(-x)),0,np.inf,args=n)[0]

def test_gamma_function(y,n):  
    gam = lambda x: (1/factorial(n-1))*(y**n)*(x**(n-1))*(1/e**(y*x))
    return quad(gam,0,10)
    
# print(test_gamma_function(0.5, 8)[0])

def test_gamma_pdf(y,n,t1,t2):
    rv= gamma(a=n,loc=0,scale = 1/y)
    print(rv.cdf(t2))
          
def chi_test(v1,v2):
    chi = lambda x:  (e**(-x/2))/2         
    return quad(chi,v1,v2)    

# print(f'chi_test result is: {chi_test()}')
          
def chi_discret(*args,mean = 10):
    result =0
    for i in args:
        # print(f'{i} {mean} --> {((i-mean)**2)/mean}')
        result += ((i-mean)**2)/mean
    return result


# a = chi_discret(93,116,103,103,93,97,94,95,101,105,mean=100)
# print(a)
# print(chi_test(a,np.inf))



print(1-chi2(1).cdf(3.84))

rv = norm(loc=120, scale=17)
print(rv.cdf(111))
print(rv.ppf(0))

