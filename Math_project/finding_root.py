def my_gen(a,b,n):
    """this function is giving a root for a*b"""
    counter = 0
    while counter < n:        
        yield(a,b)        
        a,b = (a+b)/2, 2*a*b/(a+b)
        counter += 1

def my_root(a,b):
    """this function is giving a root for a*b"""    
    while a != b:        
        yield(a,b)        
        a,b = (a+b)/2, 2*a*b/(a+b)
        counter += 1
        

for i in range(10):
    f = [(x,y) for x,y in my_gen(3,i,10)]
    print(f[0],'  ',f[-1])
