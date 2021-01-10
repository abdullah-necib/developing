x = list(range(10))
print(x)

from math import factorial
test = lambda x: (factorial(365)/factorial(365-x))/(365**x)
for i in range(100):
    print(f'{i} value {1-test(i):.6f}')