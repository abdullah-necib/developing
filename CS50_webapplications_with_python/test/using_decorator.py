def outline(f):
    def outfunction(*args):
        # print(f)
        print('start production')
        f(*args)
        print('execution finish')
    return outfunction

@outline
def my_funtion(x):
    print(x)
    print('this is from the function')

my_funtion(100)