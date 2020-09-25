#Even Fibonacci numbers
#problem 2
#python3.6 used

def generate_Fibonacci(max_number):
    Fibonacci = [1,2]
    index = 0
    i = 0
    while True :
        i = Fibonacci[index] + Fibonacci[index +1]
        if i > max_number :
            break
        Fibonacci.append(i)
        index += 1
    return Fibonacci

print(generate_Fibonacci(4000000))
Fibonacci  = generate_Fibonacci(4000000)
even_sum = 0
for i in Fibonacci :
    if i % 2 == 0:
        even_sum += i

print(even_sum)
    
