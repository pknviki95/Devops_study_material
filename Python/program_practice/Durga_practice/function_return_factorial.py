'''
Write a program to return factorial of a give integer value
'''

from math import *

def fact(value):

    return factorial(value)


input_value=int(input("Enter integer value: "))
return_value=fact(input_value)
print("The factorial value of {} is : {}".format(input_value,return_value))
