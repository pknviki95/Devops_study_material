'''
function parameters

def function_name(parameters):

function_name(arguments)
'''

def std_wish(std_name):                             #std_name -> parametrs gets value from arguments
    print("Hi {},Wish you a happy life!".format(std_name))

student_name=input("Enter student Name: ")
std_wish(student_name)

#function with no argument declaring parameter

#NOTE:
#If parameters are declared without arguments is throws Typeerror

def param(no_param):
    print("The parameter is passed")

param()