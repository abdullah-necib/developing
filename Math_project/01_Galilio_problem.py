from itertools import combinations
from copy import deepcopy

three_dice = [[a,b,c] for a in range(1,7) for b in range(1,7) for c in range(1,7)]
three_dice_no_order = []

for i in three_dice:
    i.sort()
    if i not in three_dice_no_order:
        three_dice_no_order.append(i)

def count_sum(l):
    range_list = list(range(3,19))
    result = []
    for i in range_list:
        counter = 0
        for f in l:
            if sum(f) == i:
                counter +=1
        result.append(counter)            
    return [range_list,result]
#print the aggregations for sum of three_dice with repeating 
test = count_sum(three_dice)
for i in range(0,len(test[0])):
    print('{0:2} {1:3} {2:4.4f}'.format(test[0][i],test[1][i],test[1][i]/(len(three_dice))))
#print the aggregations for sum of three_dice_no_order
print('-'*40)
test = count_sum(three_dice_no_order)
for i in range(0,len(test[0])):
    print('{0:2} {1:3} {2:4.4f}'.format(test[0][i],test[1][i],test[1][i]/len(three_dice_no_order)))
  
#test the occurence of specific combination from three_dice if we ignore the order  
x = deepcopy(three_dice)
for i in x:
    i.sort()
print('occurence of {0} is {1}'.format([2,2,4],x.count([2,2,4])))