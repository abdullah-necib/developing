from itertools import permutations
myList = [chr(x) for x in range(65,69)]
print(myList)

per = list(permutations(myList))
print('count permutations: ',len(per))
for i in per:
    print(i)