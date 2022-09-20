'''
The function has four type of arguments


- Positional arguments/Required arguments

- Keyword arguments

- Default arguments

- Variable-length arguments
'''


# Positional argument/Required arguments

def position(a,b):
    print("The value a: {} and b: {}".format(a,b))


position(1,2)
position(2,1)

#Positional error example
#position(1)


# Keyword arguments

def position(d,c):
    print("The value d: {} and c: {}".format(d,c))


position(c=1,d=2)

# Default arguments

#without argument value

def position(d=3,c=4):
    print("The value d: {} and c: {}".format(d,c))


position()


#with argument value

def position(d=3,c=4):
    print("The value d: {} and c: {}".format(d,c))


position(d=5,c=7)


# Variable-length argument

def total(*args):
    print(type(args))
    for i in args:
        print(i,"hello")

total()
total(1,2)
total(1,2,3,4)
