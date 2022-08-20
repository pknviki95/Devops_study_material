#-----------
# and,or not
#-----------


#Logical operator with boolean type

#and 

print("Both True operand returns:{}".format(True and True))
print("True and False operand returns:{}".format(True and False))
print("Both False operand returns:{}".format(False and False))


a=10
b=20
c=30

print("Both True operand returns:{}".format(a<b and b<c))
print("True and False operand returns:{}".format(a<b and b>c))
print("Both False operand returns:{}".format(a>b and b>c))

#or

print("Both True operand returns:{}".format(True or True))
print("True or False operand returns:{}".format(True or False))
print("Both False operand returns:{}".format(False or False))


print("Both True operand returns:{}".format(a<b or b<c))
print("True or False operand returns:{}".format(a<b or b>c))
print("Both False operand returns:{}".format(a>b or b>c))


#not

print("Both True operand returns:{}".format(not(True or True)))
print("True or False operand returns:{}".format(not(True or False)))
print("Both False operand returns:{}".format(not(False or False)))


print("Both True operand returns:{}".format(not(a<b or b<c)))
print("True or False operand returns:{}".format(not(a<b or b>c)))
print("Both False operand returns:{}".format(not(a>b or b>c)))

#Logical Operator for Non-Boolean type

#and

print("The non boolean and returns:{}".format(10 and 5))    #Returns 5 as first operand non-zero value (True);In and operation it return y value :5
print("The non boolean and returns:{}".format(0 and 5))     # Returns 0 as first operand zero value (False);In and operation it return x value :0
print("The non boolean and returns:{}".format("" and 5))    # Returns "" as first operand zero value (False);In and operation it return x value :""


#or

print("The non boolean and returns:{}".format(10 or 5))    #Returns 10 as first operand non-zero value (True);In or operation it return x value :10
print("The non boolean and returns:{}".format(0 or 5))     # Returns 5 as first operand zero value (False);In or operation it return y value :5
print("The non boolean and returns:{}".format("" or 5))    # Returns 5 as first operand zero value (False);In or operation it return y value :5
