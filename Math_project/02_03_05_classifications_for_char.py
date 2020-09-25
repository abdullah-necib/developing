from itertools import  combinations
import re
places = list(range(11))

comb = list(combinations(places,4)) # choosing 4 of 11 place
temp = ['B'] * 11

result =[]
#fill the positions with A and B
for i in comb:
    for index in i:
        temp[index] = 'A'
    result.append(''.join(temp))
    temp = ['B'] * 11
  
result_4A = []
result_2A_2A = []
pattern_4A = '.AAAA*'
p1 = re.compile(pattern_4A)
patter_2A_2A = 'B*AAB+AA'
p2 = re.compile(patter_2A_2A)
for i in result:
    if p1.match(i):
        result_4A.append(i)
    if p2.match(i):
        result_2A_2A.append(i)
counter = 0        
for i in result_2A_2A:
    print(counter, '  ', i)
    counter +=1
        
