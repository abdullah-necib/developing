#python3.6
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

from time import time
def create_list(max_number = 1000):
    """create production list like (a,b,str(a*b))"""
    product_list = [[a*b,str(a*b),a,b] for a in range(100,max_number) for b in range(100,max_number)]
    return product_list
    
start = time()

def check_palindorme(a):
    """check PALINDORME in abcba or abccba as string list form is (a,b,str(a*b))"""
    if len(a[1]) == 5:
        return a[1][:2] == a[1][3:][::-1]
    else:
        return a[1][:3] == a[1][3:][::-1]
        
        
#print(check_palindorme([1,2,'12421']))
#print(check_palindorme([1,2,'124421']))

result = []
for i in create_list():
    if check_palindorme(i):
        result.append(i)
        
result.sort()
print(len(result))
print(result[-1])
     
progress = time() - start
print('progress : {0:.2f} sec'.format(progress))

print('this is test purpose only')
