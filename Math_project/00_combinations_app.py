from time import time
from itertools import combinations

def factorial(number = 5):
    """find the factorial of a number"""
    if number <= 1: return 1
    else:
        result = 1
        for i in range(2,number+1): result *= i
        return result
    
def comb(a,b):
    """find the combination value"""
    if a >= b: return int(factorial(a)/(factorial(b)*factorial(a-b)))
    else: return 1
    

x = list(range(6))
def my_combination(myList = x , number = 3):
    result = []
    point = myList[:number].copy() ;    end = myList[-number:].copy()    
    our_range = list(range(number))[::-1]
    result.append(point.copy())
    while point != end:
        for index in our_range:
            if point[index] < end[index]:
                new_index = myList[myList.index(point[index]) + 1]
                point[index] = myList[new_index]
                result.append(point.copy())
                break
            elif point[index] == end[index] and \
            index > 0 and \
            point[index-1] < end[index-1]:
                #print('we are in the next level ', point, ' index is: ', index)
                new_index = myList[myList.index(point[index-1]) +1 ]
                point[index-1:] = myList[new_index:new_index + number - index +1]
                result.append(point.copy())
                break
            else:
                continue    
    return result

def compare(a_list, b_list):
    """used only to compare betweeen 2 list for combinations result"""
    if len(a_list) == len(b_list):
        index = 0
        while index < len(a_list):
            print('a_list {0} b_list {1} Equals: {2}'.format(a_list[index],b_list[index],a_list[index] == list(b_list[index])))
            index +=1
    else: print('these two list are not comparable')

base = 3
myList = list(range((base+1)**2))
n = base *2 +1
test1 = my_combination(myList,n)
"""
for i in test1:
    print(i)
    
print(len(test1))
"""


def print_all_comb(number = 4):
    counter = 1
    for i in range(number+1):
        print(counter , ': ',comb(number,i))    
        counter += 1

def test_for_diagonal(a):
    result = 0
    for i in range(a):
        print(i+1,' ',a-i,' ',(i+1)*(a-i))
        result += (i+1)*(a-i)
    print('result is: ',result)
        
test_for_diagonal(6)