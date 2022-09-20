'''
Write a program to print square of input value
'''

def sqr_value(value):
    
    #return square value of input
    return value**2

return_value=sqr_value(int(input("Enter the value: ")))
print("The square of value : {}".format(return_value))