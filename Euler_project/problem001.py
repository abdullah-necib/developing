#Multiples of 3 and 5
#Problem 1
#python3.6 

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


max_number = 1000

multiply_3 = 0
multiply_5 = 0
multiply_15 = 0 #this is used because it is repeated between 3 and 5 since 3*5 = 15

def total(n):
    """this return the total from 1 to n"""
    return int(n*(n+1)/2)

#define the multiplyies
if max_number % 3 == 0:
    multiply_3 = int(max_number/3)-1
else:
    multiply_3 = int(max_number/3)

if max_number % 3 == 0:
    multiply_5 = int(max_number/5)-1
else:
    multiply_5 = int(max_number/5)

if max_number % 3 == 0:
    multiply_15 = int(max_number/15)-1
else:
    multiply_15 = int(max_number/15)
    
print(3*total(multiply_3) + 5*total(multiply_5) - 15* total(multiply_15))

