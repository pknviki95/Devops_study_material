

# Both non-default

def default(a,b):
    print("Both non-default")

default(1,2)


# Both Default

def default(a=2,b=3):
    print("Both default")

default(1,2)

# 1st parameter non-default and 2nd parameter default 

def default(a,b=3):
    print("1st parameter non-default and 2nd parameter default")

default(1,2)

# 1st parameter default and 2nd parameter non-default 

def default(a=3,b):
    print("1st parameter non-default and 2nd parameter default")

default(1,2)
