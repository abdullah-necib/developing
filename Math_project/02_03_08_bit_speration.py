from itertools import combinations
def find_seperated_1s(N= 7, k=2):
    combList = list(combinations(range(N),k))
    result = []
    temp = [0]*N
    #print(temp)
    for sublist in combList:
        add = True
        for i in sublist:
            #filter for seperating 1s
            if sublist.index(i) +1 < len(sublist):
                if i +1 == sublist[sublist.index(i)+1] :
                    add = False
            temp[i] = 1
        if add:
            result.append(temp.copy())
        
               
        temp = [0] *N
    result.sort(key = lambda x : x[-1])
    return result

def print_summary(myList):
    counter = 1
    counter0 = 0
    counter1 = 0
    for i in myList:
        print(counter ,': ', i)
        counter +=1
        if i[-1] == 0: counter0 +=1
        else: counter1 +=1            
    print('end with zeros count: ',counter0)
    print('end with ones are: ',counter1)
    print('-'*30)

print_summary(find_seperated_1s(7,2))

