#######################################
# Return stament for multiple values
#######################################

#NOTE:
# Returning multiple values is only applicable in python
# it returns tuples of value as the comma seperated value without braces is considered as tuple
# it can return other datatypes based on braces



def calcul(value1,value2):
    total=value1+value2
    diff=value1-value2
    mult=value1*value2

    return {1:total,2:diff,3:mult}


#addition,Subtraction,multiplication=calcul(10,20)

calculation=calcul(10,20)
'''
# type of individual variable returned from Function

print("Addition value: ",addition,type(addition))
print("Subtraction value: ",Subtraction,type(Subtraction))
print("multiplication value: ",multiplication,type(multiplication))
'''

#type of single variable return multiple values from function

print("calculation: ",calculation,type(calculation))
