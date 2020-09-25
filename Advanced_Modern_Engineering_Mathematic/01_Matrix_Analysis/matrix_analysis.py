import sympy as sy
from sympy import Symbol, pprint,sqrt,cos,sin

A = sy.Matrix([[1,2,4],[1,3,-1],[2,-1,4]])
B = sy.Matrix([[1,2,4],[1,0,-1],[2,-1,0],[1,1,1]])
a4 = sy.Matrix([[2,-2,4,-2],[2,1,10,7],[-4,4,-8,4],[4,-1,14,6]])

def SubTransposed(m):
    return m - m.transpose()

def SumMatrixElements(matrix):
    result = 0
    for a in matrix:
        result += a
    return result

def GetCofactors(matrix):
    return sy.Matrix(matrix.cols, matrix.cols,[ matrix.cofactor(i,j) \
                                                for i in range(matrix.cols)\
                                                for j in range(matrix.cols)])
    

a11 = Symbol('a11')
a12 = Symbol('a12')
a13 = Symbol('a13')
a21 = Symbol('a21')
a22 = Symbol('a22')
a23 = Symbol('a23')
a31 = Symbol('a31')
a32 = Symbol('a32')
a33 = Symbol('a33')


test = sy.Matrix([[a11,a12],[a21,a22]])

def create_test(a11,a22):
    a12 = sqrt(1-a11**2)
    a21 = -a22*a12/a11
    return sy.Matrix([[a11,a12],[a21,a22]])

def get_length(m):
    return sqrt(m[0]**2+m[1]**2)

def faddeev(matrix):
    n = [x+2 for x in range(matrix.shape[0]-1)]
    I_matrix = sy.eye(matrix.shape[0])   
    A_matrix = []
    A_matrix.append(matrix)
    B_matrix = []
    B_matrix.append([])
    P_values = []
    P_values.append(matrix.trace())       
        
    for i in n:
        #pprint(A_matrix[-1])
        #pprint(B_matrix[-1])
        #pprint(P_values[-1])
        #print(50*'-')
        B_temp = A_matrix[-1] - (P_values[-1]*I_matrix)
        #pprint(B_temp)
        B_matrix.append(B_temp)
        A_temp = matrix*B_temp
        #pprint(A_temp)
        A_matrix.append(A_temp)
        P_values.append(A_temp.trace()/i)
        #print(P_values)
        
    #pprint(A_matrix[-1])
    #pprint(B_matrix[-1])
    #pprint(P_values[-1])
    #print(50*'-')    
        
    print('A matrix are like:')
    pprint(A_matrix)
    print('B matrix are like:')
    pprint(B_matrix)
    print('lambda values are like:')
    pprint(P_values)
    return (A_matrix,B_matrix,P_values)
        
test = sy.Matrix([[1,1,-2],[-1,2,1],[0,1,-1]])        
faddeev(test)
#faddeev(A)

x= Symbol('x')
test_x = sy.Matrix([[1-x,2,4],[1,3-x,-1],[2,-1,4-x]])
test_x2 = sy.Matrix([[1-x,1,-2],[-1,2-x,1],[0,1,-1-x]])  
print(test_x2.det())
    