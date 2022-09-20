# Functions
# It is used for code reusability
#   Syntax:
#        def function_name(parameters)
#               
#        function_name(arguments)




def calculator(value1,value2):
    calculator_input=input("Enter your choice: ")
    if calculator_input == "+":
        return value1+value2
    if calculator_input == "-":
        return value1-value2
    if calculator_input == "*":
        return value1*value2
    if calculator_input == "/":
        return value1/value2


calculated_value=calculator(int(input("Enter value 1: ")),int(input("Enter value 2: ")))

print("calculated_value: {}".format(calculated_value))
