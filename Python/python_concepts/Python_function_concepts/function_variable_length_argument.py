'''

Variable-length argument is used to pass n number of values as arguments

*args -These are Non-Keyword Arguments

**kwargs - These are Keyword Arguments.

'''

'''
#steps by step difference between *args and keyword-arguments and keywords argument using **kwargs

#*args

def variable_length(*args,y,**kwargs):
    print(args,type(args))
    print(y,type(y))
    print(kwargs,type(kwargs))
    print("hello")
variable_length([1,2],3,4,5,y=10,z=3)


#*args and keyword-arguments

def variable_length(*args,y):
    print(args,type(args))
    print(y,type(y))
    print("hello")


variable_length([1,2],3,4,5,y=10)


#*args and keyword-arguments and keywords argument using **kwargs

def variable_length(*args,y,**kwargs):
    print(args,type(args))
    print(y,type(y))
    print(kwargs,type(kwargs))
    print("hello")


variable_length([1,2],3,4,5,y=10,z=3)
'''

#Usage of *args and **kwargs simultaneously


def variable_length(*args,**kwargs):
    print(args)
    print(kwargs)

#possible function call (i.e) positional 1st argument keyword 2nd argument
#variable_length(10,2,a=4,b=5)

#Not-possible function call  (i.e) keyword 1st argument positional 2nd argument
#variable_length(a=4,b=5,10,2)


#Syntax for variable-length for *args and **kwargs simultaneously


def fun(**kwargs,*args):
    print(kwargs,args)

fun(1,2,a=10)
