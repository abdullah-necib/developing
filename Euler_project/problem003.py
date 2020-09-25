#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from time import time
def primes_under_n(n):
    """this fuction will find all primes numbers that less than n"""
    result = [1,2,3]
    i = 5
    while i < n+1:
        is_prime = True
        for prime in result[1:]:            
            if i % prime == 0:
                is_prime = False
                break
        if is_prime :
            result.append(i)
        i = i +2
    """    
    for i in range(5,n+1,2):
        is_prime = True
        for prime in result[1:]:            
            if i % prime == 0:
                is_prime = False
                break
        if is_prime :
            result.append(i)"""
    return result

def factors(n):   
    """find the factors of numbers"""
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    root = int(n**0.5)
    #print(root)
    primes = primes_under_n(root)
    #print(primes)
    factors = []
    for p in primes[1:]:
        #print(p)
        while n % p == 0:
            factors.append(p)
            n = int(n/p)
    if n > 1:
        factors.append(n)        
    factors.insert(0,1)
    factors.sort()
    return factors



"""test purpose only"""
start_time = time()
#for i in range(100000):
#    print('{0} has this factors {1}'.format(i,factors(i)))
print('start calculation ........')
#print(10000,' has ',factors(10000))
print(600851475143,' has ',factors(600851475143))
#print(primes_under_n(100000))
progress_time = time()-start_time
print('{0:.2f} sec'.format(progress_time))



