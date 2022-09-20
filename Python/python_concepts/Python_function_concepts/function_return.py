'''
Return Statement:
'''
# Write a program to return sum of two numbers





def ret_sum(num1,num2):
    return num1+num2

total=ret_sum(int(input("Enter num1: ")),int(input("Enter num2: ")))
print("total={}".format(total))


# Default value of return statement is None

def hello():
    print("How are you!")

x=hello()
print("The default value of return :",x)
