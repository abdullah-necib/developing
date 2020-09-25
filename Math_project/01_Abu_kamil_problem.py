#book counting solution
#the first when y and t' are even
counter = 0
for y in range(2,59,2):
    for z in range(3,52,3):
        for t in range(4,53,4):            
            if (3*(y/2) + 5*(z/3) + 7*(t/4)) < 100:   
                #print(y,' ',z,' ',t,' ',3*y/2 + 5*z/3 + 7*t/4)
                counter += 1
print(counter)
counter = 0
#the second when y and t' are odd
for y in range(1,60,2):
    for z in range(3,55,3):
        for t in range(2,51,4):            
            if (6*(y/4) + 5*(z/3) + 7*(t/4)) < 100:   
                #print(y,' ',z,' ',t,' ',3*y/2 + 5*z/3 + 7*t/4)
                counter += 1
print(counter)
