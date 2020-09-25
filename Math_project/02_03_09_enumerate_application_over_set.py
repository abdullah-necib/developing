def check_range(myList,N):
    right = True
    for i in range(N):
        if i not in myList:
            return False
    return right
    
N=6
NN = N**N
app_result = []
counter_set = [0]*N
for number in range(NN):
    q = number
    #print('number is: ', number)
    temp = []
    for i in range(N):
        r = q % N
        #print('r: ',r,' q: ',q,' i: ',i,' index is: ',N-i-1)
        q = int( q /N)
        temp.append(r)
    #counting the touch of the element in the result set
    for i in temp:
        counter_set[i] += 1
    #print('counter set is: ',counter_set)
    app_result.append(temp.copy())

app_result.sort() 
counter = 1
for i in app_result:
    if check_range(i,N):
        print(counter,': ',i)
        counter +=1

print('-'*30)
print(counter_set)