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


def write_to_file(lst, filename='test.log', mode='w'):
    l = len(str(len(lst)))
    with open(filename, mode) as f:
        count = 1
        for i in lst:
            f.write(f'{count:{l}} >> {i}\n')
            count += 1
    print(f'done writing to file: {filename}')


def comb(n, r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))


def perm(n, r):
    return factorial(r)*comb(n, r)


def birthday_problem(k):
    """this is from third licture in statistics 101 """
    return 1-factorial(365)/(factorial(365-k)*(365**k))


def comb_iteration(n):
    for i in range(n+1):
        print(comb(n, i))


def fprint(x):
    print(50*'-')
    count = 1
    for i in x:
        print(f'{count:3} >>  {i}')
        count += 1
    print(50*'-')


def question_1a():
    base = list(range(1, 7))
    mainlist = [[a, b, c, d] for a in base for b in base for c in base
                for d in base]
    set21 = []
    set22 = []
    for item in mainlist:
        if sum(item) == 21:
            set21.append(item)
        if sum(item) == 22:
            set22.append(item)
    fprint(set21)
    print(len(set21))
    fprint(set22)
    print(len(set22))


def question_1b():
    x = [chr(a) for a in range(65, 91)]
    main2 = [a+b for a in x for b in x]
    main3 = [a+b for a in x for b in main2]
    cnt2 = 0
    cnt3 = 0
    for i in main2:
        if i[0] == i[-1]:
            cnt2 += 1
    for i in main3:
        if i[0] == i[-1]:
            cnt3 += 1
    print(cnt2)
    print(cnt2/len(main2))
    print(cnt3)
    print(cnt3/len(main3))


def question_2():
    base = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    types = ['D', 'H', 'C', 'S']
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
            if element[-1] in ('A', '0', 'J', 'Q', 'K'):
                return False
        return result

    def test_b(item):
        result = True
        string = ''.join(item)
        # print(string)
        if string.count('A') != 1:
            return False
        cond = []
        for element in item:
            if element[-1] == 'A':
                item.remove(element)
            else:
                cond.append(element[0])

        cond.sort()
        if cond not in use2of4type:
            return False

        return result
    event_a = [x for x in space if test_a(x)]
    # fprint(event_a)
    print(len(event_a)/len(space))


# question_2()  akk is wrong

def zrief():
    result = 0
    for i in range(0, 5):
        x = comb(6, i)*comb(4, 4-i)/comb(10, 4)
        result += x
        print(f'{i} {x} {result}')
    return result


def rBall_nBox(r, n):
    """r is the quantity of balls"""
    base = [x for x in range(r+1)]
    main_space = [list(x)
                  for x in product(base, repeat=n) if sum(list(x)) == r]
    fprint(main_space)
    return main_space


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
    permut = permutations(base, len(base))
    set_result = set(permut)
    lst_result = [''.join(x) for x in set_result]
    lst_result.sort()

    with open('test_mississippi.log', 'a') as f:
        count = 1
        for i in lst_result:
            f.write(f'{count: 6} >> {i}\n')
            count += 1
    print(len(lst_result))


def exercise_1_9_3():
    # perm = combinations(list(range(1,11)),5)
    # fprint(perm)
    perm2 = list(combinations_with_replacement(list(range(1, 11)), 5))
    prod = list(product(range(1, 11), repeat=5))

    def accepted(lst):
        result = True
        for i in range(0, len(lst)-1):
            if lst[i] == lst[i+1]:
                return False
        return result
    # perm3 = [x for x in perm2 if accepted(x)]
    prod_row = [x for x in prod if accepted(x)]
    write_to_file(perm2)
    # write_to_file(perm3,'test_row.log')
    write_to_file(prod_row, 'test_row.log')


# exercise_1_9_3()

def accepted(lst):
    result = True
    for i in range(0, len(lst)-1):
        if lst[i] == lst[i+1]:
            return False
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
    original = list(range(1, 13))
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
    f = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3']
    x = [a for a in permutations(f, len(f))]
    # fprint(x)

    def flipBin(test='111000'):
        result = test.replace('1', 'T')
        result = result.replace('0', '1')
        return result.replace('T', '0')

    def get_flag(a, model='111000', with_flip=True):
        temp = ''
        for i in a:
            if i.startswith('a'):
                temp += '1'
            else:
                temp += '0'
        if with_flip:
            if temp == model or temp == flipBin(model):
                return True
        else:
            if temp == model:
                return True
        return False
    count = 1
    for i in x:
        if get_flag(i, '101010'):
            print(f'{count} >> {i}')
            count += 1


# exercise_1_17()

# for i in range(2,10):
#     print(f'{i} comb({2*i},{i}) = {comb(2*i,i)}')


def question_19(n=5, k=2):
    base = list(range(1, n+1))
    cmb = [a for a in combinations(base, k)]
    # fprint(cmb)
    cnt = 1
    middle_numbers = [a[2] for a in cmb]
    summary = []
    for a in middle_numbers:
        if a not in summary:
            summary.append(a)
    for i in cmb:
        print(f'{cnt} >> {i}   >> {i[2]}')
        cnt += 1
    for a in summary:
        print(f' {a} appears: {middle_numbers.count(a)}')


# question_19(10,5)


def question_20a(n=6, k=2):
    x = list(range(1, n+1))
    cmb = [a for a in combinations(x, k)]
    last_numbers = [a[-1] for a in cmb]
    summary = []
    cnt = 1
    for a in last_numbers:
        if a not in summary:
            summary.append(a)
    for i in cmb:
        print(f'{cnt} >> {i}   >> {i[-1]}')
        cnt += 1
    for a in summary:
        print(f' {a} appears: {last_numbers.count(a)}')


# question_20a(5,3)

def question_20a_abd(n=6, k=2):
    x = list(range(1, n+1))
    cmb = [a for a in combinations(x, k)]
    first_numbers = [a[0] for a in cmb]
    summary = []
    cnt = 1
    for a in first_numbers:
        if a not in summary:
            summary.append(a)
    for i in cmb:
        print(f'{cnt} >> {i}   >> {i[0]}')
        cnt += 1
    for a in summary:
        print(f' {a} appears: {first_numbers.count(a)}')

# question_20a_abd(5,2)
# rBall_nBox(5, 3)
# =============================================================================
# question No 20 start
# =============================================================================
# result =0
# n,r,k = 5,4,3
# for i in range(0,r+1):
#     temp = comb(n+i,k+i)
#     print(f'C({n+i},{k+i}) is {temp}')
#     result += temp
# print(f'for n={n}, r={r}, k={k} result is: {result}')
# print(__file__)
# print('\n\n\n')

# cnt =1
# for i in rBall_nBox(6, 3):
#     if i.count(6) == 0:
#         print(f'{cnt} >> {i}')
#         cnt +=1

# =============================================================================
# question 20 finish
# =============================================================================


def question21(n, k):
    if k == 1 or n == k:
        return 1
    else:
        return question21(n-1, k-1) + (k * question21(n-1, k))


# print(question21(6,2))


# n = 10
# result =0
# for i in range(1,n+1):
#     result += i**3

# print(result)
# f= lambda x: 6* comb(x+1,4) + 6* comb(x+1,3) + comb(x+1,2)
# print('result is: ',f(10))


def question23(n=10):
    base = [a for a in product(list(range(2, n+1)), repeat=3)]
    required = [a for a in base if a[0]+1 == a[1] and a[0]+2 == a[2]]
    fprint(required)


# question23()

# f2 = lambda x : (factorial(x)**2)/factorial(2*x)
# for i in range(1,6):
#     print(f2(i))

def question29_a():
    base = [x for x in product(list(range(1, 7)), repeat=4)]
    req21 = [a for a in base if sum(a) == 21]
    req22 = [b for b in base if sum(b) == 22]
    print(f'len 21 is: {len(req21)} and for 22 is: {len(req22)}')
    fprint(req21)
    fprint(req22)


# question29_a()
base = [x for x in combinations_with_replacement(list(range(1, 4)), 4)]
# fprint(base)
# a_5_1 = [x for x in base if len(set(x))== 1]
# a_5_2 = [x for x in base if len(set(x))== 2]
# a_5_3 = [x for x in base if len(set(x))== 3]
# a_5_4 = [x for x in base if len(set(x))== 4]
# a_5_5 = [x for x in base if len(set(x))== 5]
# fprint(a_5_4)
# test = [x for x in a_5_4 if x.count(1) != 0 and x.count(2) != 0 and x.count(3) !=0 and x.count(4) !=0]
# fprint(test)


def delete_element(x, a):
    temp = x.copy()
    temp.remove(a)
    return temp


def contains(container, includer, k):
    """used for testing if [1,2,3,4] contains [a,b] or not 
    used in question31(N,n,m,k)
    result is True / False"""
    cnt=0
    for i in includer:
        if container.count(i) != 0:
            cnt +=1
    if cnt >= k:
        return True
    return False


def contains_only_k(container, includer, k):
    """used to check if container and includer shared exactly and only k elements
    used in question31(N,n,m,k)
    result is: (True,Common) / (False ,[])"""
    cnt = 0
    common = []
    for m in includer:
        if m in container:
            cnt += 1
            common.append(m)
    if cnt == k:
        return True, common
    return False, common


def question31(N=10, n=7, m=5, k=2):
    N, n, m, k = N, n, m, k
    result1 = comb(n, k) * comb(N-n, m-k)
    result2 = comb(N, m)
    print(f'{result1} / {result2}')
    base_n = [x for x in combinations(list(range(1, N+1)), n)]
    base_m = [x for x in combinations(list(range(1, N+1)), m)]
    cnt = 1
    result = []
    with open(f'ch1_question31_{N}_{n}_{m}_{k}.log', 'w') as logfile:
        for m in base_m:
            for n in base_n:
                temp = []
                a, K = contains_only_k(n, m, k)
                if a:
                    temp.append(K)
                    temp.append(m)
                    temp.append(n)
                    logfile.write(f'{cnt} >> m is: {m} / n is: {n}\n')
                    cnt += 1
                    result.append(temp)
    return result

def question31_not_exactly(N=10, n=7, m=5, k=2):
    N, n, m, k = N, n, m, k
    # result1 = comb(n, k) * comb(N-n, m-k)
    # result2 = comb(N, m)
    # print(f'{result1} / {result2}')
    base_n = [x for x in combinations(list(range(1, N+1)), n)]
    base_m = [x for x in combinations(list(range(1, N+1)), m)]
    cnt = 1
    result = []
    with open(f'ch1_question31_not_exactly_{N}_{n}_{m}_{k}.log', 'w') as logfile:
        for m in base_m:
            for n in base_n:
                temp = []
                if contains(n,m,k):
                    temp.append(m)
                    temp.append(n)
                    logfile.write(f'{cnt} >> m is: {m} / n is: {n}\n')
                    cnt += 1
                    result.append(temp)
    return result

"""this is used for testing purpose for question31 function"""
# N,n,m,k = 10, 7, 5, 3
# result = question31(N,n,m,k)
# print(len(result))
# # test_m = [a for a in result if a[1] == tuple(range(1,m+1))]
# # fprint(test_m)
# test_n = [a for a in result if a[2] == tuple(range(1,n+1))]
# fprint(test_n)
# # test_k = [a for a in result if a[0] == list(range(1,k+1))]
# # fprint(test_k)

# # result = question31_not_exactly(N,n,m,k)
# # print(len(result))


def question35():
    def verify(lst):
        temp = []
        for a in lst:
            temp.append(a[0])
        for i in temp:
            if temp.count(i) not in (2,4) :
                return False
        return True

    n = 8
    numbers = list(range(1,n+1))
    types = ['A','B','C']
    base = [t+str(n) for n in numbers for t in types]
    sample_space = [x for x in combinations(base,n)]
    # print(len(sample_space))
    experiment = [list(a) for a in sample_space if verify(a)]
    # fprint(experiment)

    cnt = 1
    with open('question35.log','w') as f:
        for i in experiment:
            f.write(f'{cnt} {i}\n')
            cnt +=1
    print(cnt-1)
    return experiment

    
# this was added because of for number 8 we may have 2-2-4/3-3-2/4-4
# i forget about 4-4 so the number wasn't correct

# exp = question35()
# temp = []
# for i in exp:
#     i.sort()
#     temp.append(i)

# temp.sort()
# with open('question35_224.log','w') as f:
#     for i in temp:
#         if i[:4] == ['A1','A2','A3','A4']:
#                     f.write(f'{i}\n')

# this is for question 36
# a = 1
# for i in range(1,6):
#     a *= comb(35-5*i,5)
# print(a/(6**30))

def question37():
    n=4
    base= [c+str(i) for c in ('A','B') for i in range(1,n+1)]
    base_factorial = [list(a) for a in permutations(base,8)]
    base = []
    for i in base_factorial:
        temp = i[0:i.index('A1')]
        if 'B1' in temp:
            temp = temp[0:i.index('B1')]
        if temp not in base:
            base.append(temp)
    with open('question37.log','w') as f:
        for i in base:
            f.write(f'{i}\n')
    return base



            
test =question37()
# result=0
# for i in range(0,49):
#     print(f'{i} perm(49,{i}) is {perm(49,i)}')
#     result += perm(49,i)
# print(result)

# for i in test:
#     i.sort()
# test_2=[]
# for i in test:
#     if i not in test_2:
#         test_2.append(i)
# test_B2 = [a for a in test_2 if 'B2' not in a]
# # fprint(test_B2)
# test_B2_A2 = [a for a in test_B2 if 'A2' not in a]
# fprint(test_B2_A2)

# for i in range(0,37):
#     print(f'{i+1} for i={i} P is: {comb(36,i)/comb(48,i)}')


def contiguity(lst, a,b):
    if lst.index(a) == lst.index(b) + 1 or lst.index(a) +1 == lst.index(b): return True
    return False

def question38(n=4,x=1,y=2):    
    base = [a for a in range(1,n+1)]
    exp = [a for a in permutations(base,n)]
    contiguity_list = [a for a in exp if contiguity(a,x,y)]
    # fprint(contiguity_list)
    print(len(contiguity_list))
    

# question38(10,1,2)
def count_couples(a):
    couples=0
    for i in a:
        if i%2 == 1 and i+1 in a:
            couples +=1
    return couples

def question39(n=6,k=6,j=2):
    base = [a for a in combinations(list(range(1,2*n+1)),k)]
    couples = [a for a in base if count_couples(a) == j]
    fprint(couples)

# question39(8,10,2)

# n,k,j = 6,6,2
# print(comb(n,j)*(2**(k-2*j))*comb(n-j,n+j-k))
# add comment for cheking what is done using git

def counting_elements_in_list(a):
    """count how many different element in a list"""
    counted = []
    for i in a:
        if i in counted : continue
        else:
            counted.append(i)
    return len(counted)

def question40(n=4,k=3):
    experiment = [a for a in combinations_with_replacement(range(1,n+1),k)]
    print(f'the whole experiment for {k} elements\nfrom {n} elements with replacement')
    fprint(experiment)
    print('ANALAYSING THE RESULT')
    print(30*'-')
    for i in range(1,k+1):
        print(f'sets that include {i} elements:')
        fprint([a for a in experiment if counting_elements_in_list(a) == i])

question40(4,4)











print('------ done -------------')