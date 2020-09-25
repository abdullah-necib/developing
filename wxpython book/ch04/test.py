class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


    def __str__(self):
        return '{0} {1} , Age is: {2}'.format(self.fname,self.lname,self.age)

if __name__ == '__main__':
    p = Person('abd','necib',42)
    print(p)
    setattr(p, 'age',35)
    print(p)
    setattr(p,'test',10)
    print(p.test)
    print(p.__dict__)
    x = list(range(10))
    x.test =50
    print(x)

