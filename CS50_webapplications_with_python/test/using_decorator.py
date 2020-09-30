# use this website:
#  https://realpython.com/primer-on-python-decorators/#:~:text=Decorators%20provide%20a%20simple%20syntax,function%20without%20explicitly%20modifying%20it.

# function with args
def outline(f):
    def outfunction(*args):  #here we define only the args for the called function 
        # print(f)
        print('start production')
        f(*args)
        print('execution finish')
    return outfunction

# define wrapper function without args
def another_outline(func):
    def wrapper(): #here there is no args
        print('here another wrapper')
        func()
        print('end of selection')
    return wrapper  #this line is important 



@outline
def my_funtion(x):
    print(x)
    print('this is from the function')

@another_outline
def func1():
    print('helllllllllllllllllo')

func1()   
my_funtion(100)