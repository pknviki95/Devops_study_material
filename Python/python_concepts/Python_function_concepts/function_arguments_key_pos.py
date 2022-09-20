

# Both positional


def fun(a,b):
    return "Both positional"

ret=fun(1,2)
print(ret)

# Both keyword

def fun(a,b):
    return "Both Keyword"

ret=fun(a=1,b=2)
print(ret)

# 1st argument positional and 2nd argument keyword

def fun(a,b):
    return "1st argument positional and 2nd argument keyword"

ret=fun(1,b=2)
print(ret)

# 1st argument keyword and 2nd argument positional

def fun(a,b):
    return "1st argument keyword and 2nd argument positional"

ret=fun(a=1,2)
print(ret)
