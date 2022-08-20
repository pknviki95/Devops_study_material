#------------------------------------------------------------------------------
# Dictionary Comprehension
#   Syntax:
#       dict= {key: value for (key, value) in iterable if condition==True} 
#------------------------------------------------------------------------------



dict1={x:x**2 for x in range(1,10)}
print(dict1)
