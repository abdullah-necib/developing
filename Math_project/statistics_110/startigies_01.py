#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 05:23:19 2020

@author: abdullah
"""
from math import factorial
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

def write_to_file(lst, filename='test.log',mode='w'):
    l= len(str(len(lst)))
    with open(filename, mode) as f:
        count = 1
        for i in lst:
            f.write(f'{count:{l}} >> {i}\n')
            count += 1
    print(f'done writing to file: {filename}')
    
    
def comb(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

def perm(n,r):
    return factorial(r)*comb(n,r)

def birthday_problem(k):
    """this is from third licture in statistics 101 """
    return 1-factorial(365)/(factorial(365-k)*(365**k))

def comb_iteration(n):
    for i in range(n+1):
        print(comb(n,i))
def fprint(x):
    print(50*'-')
    count = 1
    for i in x:
        print(f'{count:3} >>  {i}')
        count +=1
    print(50*'-')
    
    
def question_1a():
    base = list(range(1,7))
    mainlist = [[a,b,c,d] for a in base for b in base for c in base\
                for d in base]
    set21 = []
    set22 = []  
    for item in mainlist:    
        if sum(item) == 21: set21.append(item)        
        if sum(item) == 22: set22.append(item)
    fprint(set21)
    print(len(set21))
    fprint(set22)
    print(len(set22))
    
def question_1b():
    x = [chr(a) for a in range(65,91)]
    main2 = [a+b for a in x for b in x]
    main3 = [a+b for a in x for b in main2]
    cnt2 = 0
    cnt3 = 0
    for i in main2:
        if i[0]==i[-1]: cnt2 +=1
    for i in main3:
        if i[0]==i[-1]: cnt3 +=1
    print(cnt2)
    print(cnt2/len(main2))
    print(cnt3)
    print(cnt3/len(main3))

def question_2():
    base = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    types = ['D','H','C','S']
    types.sort()
    use2of4type = [list(a) for a in combinations(types, 2)]
    fprint(use2of4type)
    
    main = [a+b for a in types for b in base]
    space = [list(a) for a in combinations(main, 5)]
    # space = list(combinations(main,5))
    def test_a(item):
        result = True
        for element in item:
            if element[0] != item[0][0]:
                return False
            if element[-1] in ('A','0','J','Q','K'):
                return False
        return result
    def test_b(item):
        result = True
        string = ''.join(item)
        # print(string)
        if string.count('A') != 1:
            return False
        cond=[]
        for element in item:            
            if element[-1] == 'A': item.remove(element)
            else:     
                cond.append(element[0])
        
        cond.sort()
        if cond not in use2of4type:
            return False
            
        return result
    event_a =[x for x in space if test_a(x)]
    # fprint(event_a)
    print(len(event_a)/len(space))
 
        
    
# question_2()  akk is wrong

def zrief():
    result = 0
    for i in range(0,5):
        x = comb(6,i)*comb(4,4-i)/comb(10,4)
        result += x
        print(f'{i} {x} {result}')
    return result

def rBall_nBox(r,n):
    """r is the quantity of balls"""
    base = [x for x in range(r+1)]
    main_space = [list(x) for x in product(base,repeat = n) if sum(list(x))== r]
    fprint(main_space)


# for i in range(2,6):
    # rBall_nBox(6,i)


# for i in range(15):
#     temp = []
#     for j in range(i+1):
#         temp.append(comb(i,j))
#     print(str(temp))

# rBall_nBox(3,5)

# f = lambda x: comb(6,x)*(1/6**x)
# print(f(2))



def exercise_1_9_1(word='MISSISSIPPI'):
    base = [x for x in word]
    base.sort()    
    print(f'base is :{base}')
    permut = permutations(base,len(base))
    set_result = set(permut)
    lst_result = [''.join(x) for x in set_result]
    lst_result.sort()
    
    with open('test_mississippi.log','a') as f:
        count = 1
        for i in lst_result:
            f.write(f'{count: 6} >> {i}\n')
            count += 1
    print(len(lst_result))
    
def exercise_1_9_3():
    # perm = combinations(list(range(1,11)),5)
    # fprint(perm)
    perm2 = list(combinations_with_replacement(list(range(1,11)), 5))
    prod = list(product(range(1,11),repeat=5))
    def accepted(lst):
        result = True
        for i in range(0,len(lst)-1):
            if lst[i]==lst[i+1]: return False
        return result
    # perm3 = [x for x in perm2 if accepted(x)]
    prod_row = [x for x in prod if accepted(x)]
    write_to_file(perm2)
    # write_to_file(perm3,'test_row.log')
    write_to_file(prod_row,'test_row.log')


# exercise_1_9_3()

def accepted(lst):
    result = True
    for i in range(0,len(lst)-1):
        if lst[i]==lst[i+1]: return False
    return result
    
def check_3_time(lst):
    result = False
    for i in lst:
        if lst.count(i) == 3:
            return True
    return result

# =============================================================================
# this is for exercise : 3 from first chapter
# =============================================================================
# x = product([1,2,3,4,5,6,7,8,9,10],repeat=5)
# # set_x = set(x)
# # lst_x = list(x)
# count = 1
# count_sub = 1
# with open('test.log','w') as f:
#     for i in x:
#         t =''.join([str(f) for f in i])
#         s = set(i)
#         if accepted(i): 
#             # if: len(s) == 3 and not check_3_time(i):
#                 # if 1 in i and 2 in i and 3 in i :
#                     # if i.count(1) == 2 and i.count(2) == 2:
#                         f.write(f'{count:4} >> {t}  accepted {count_sub}\n')
#                         count_sub +=1
#         # else:
#         #     f.write(f'{count:4} >> {t}\n')
#         count += 1
# =============================================================================
# exercise 3 finished here
# =============================================================================
    
# x = product([1,2,3,4],repeat=4)    
# print(50*'-')
# lst_cnt = 1
# count = 1
# count_1 = 1
# count_2_a = 1
# count_2_b = 1
# count_3 = 1
# count_accept = 1
# for i in x:
#     s = set(i)
#     l = list(i)
#     if len(s) == 1:
#         print(f'{lst_cnt:3}: {count:4} >> {i} ########### ONE {count_1}')
#         count_1 +=1
#         lst_cnt += 1
#     elif len(s) == 2:
#         a = s.pop()
#         if l.count(a) == 1 or l.count(a) == 3:
#             print(f'{lst_cnt:3}: {count:4} >> {i} ########### TWO  AAA_B {count_2_a}')
#             count_2_a +=1
#             lst_cnt += 1
#         elif l.count(a) == 2 and not accepted(l):
#             print(f'{lst_cnt:3}: {count:4} >> {i} ########### TWO  AA_BB {count_2_b}')
#             count_2_b += 1
#             lst_cnt += 1
#         elif l.count(a) == 2 and accepted(l):
#             print(f'{lst_cnt:3}: {count:4} >> {i} ACCEPTED {count_accept}')
#             count_accept +=1
#             lst_cnt +=1
            
#     elif len(s) == 3:
#         if accepted(l):
#             print(f'{lst_cnt:3}: {count:4} >> {i} ACCEPTED {count_accept}')
#             count_accept +=1
#             lst_cnt +=1
#         else:
#             print(f'{lst_cnt:3}: {count:4} >> {i} ########### THREE  AA_BB {count_3}')
#             count_3 += 1
#             lst_cnt +=1
#     elif len(s) == 4:
#         if accepted(l):
#             print(f'{lst_cnt:3}: {count:4} >> {i} ACCEPTED {count_accept}')
#             count_accept +=1
#             lst_cnt +=1
                 
#         #     print(f'{count:4} >> {i}  accepted {count_sub}')
#         #     count_sub +=1
#         # else:
#         #     print(f'{count:4} >> {i}')
#     count += 1
    

# print(count_1-1)
# print(count_2_a-1)
# print(count_2_b-1)
# print(count_3-1)
# print(count_accept-1)
# print(count_1+count_2_a+count_2_b+count_3)


def check_for_exercise8(lst):
    original = list(range(1,13))
    temp = []
    for i in lst:
        for j in i:
            temp.append(j)
    temp.sort()
    if temp == original:
        return True
    return False

# x = list(range(1,13))
# fprint(x)
# base = [list(a) for a in combinations(x, 4)]
# fprint(base)
# test = [a for a in combinations(base, 3)]
# count =1
# for i in test:
#     if check_for_exercise8(list(i)):
#         print(f'{count} >>> {i}')
#         count += 1
    
# print('Well done')

# x = [list(a) for a in combinations([1,2,3,4,5], 2)]
# fprint(x)

def exercise_1_17():
    f = ['a1','a2','a3','b1','b2','b3']
    x =[a for a in permutations(f,len(f))]
    # fprint(x)
    def flipBin(test ='111000'):
        result = test.replace('1','T')
        result = result.replace('0','1')
        return result.replace('T','0')
    
    def get_flag(a,model='111000',with_flip = True):
        temp = ''
        for i in a:
            if i.startswith('a'): temp +='1'
            else : temp += '0'
        if with_flip:
            if temp == model or temp == flipBin(model): return True
        else:
            if temp == model: return True
        return False
    count = 1
    for i in x:
        if get_flag(i,'101010'):
            print(f'{count} >> {i}')
            count +=1
        
    
    
    
# exercise_1_17()

# for i in range(2,10):
#     print(f'{i} comb({2*i},{i}) = {comb(2*i,i)}')


def question_19(n=5,k=2):
    base = list(range(1,n+1))
    cmb = [a for a in combinations(base, k)]
    fprint(cmb)

question_19(6,4)
