#-------------------------------------
# Range Datatype
# Syntax:
#       range(value)
#-------------------------------------


range_value=range(10)

print("Range value is from: {}".format(range_value))  #range(0,10)

#The range elements can be accessed through loop

for x in range_value:
    print("Range elements: {}".format(x))


#Range with start and end value:

range_value_1=range(2,15)

print("Range_value_1:{}".format(range_value_1))

for x in range_value_1:
    print("Range elements: {}".format(x))

#The range with start,end,step value:

range_value_1=range(2,15,2)

print("Range_value_1:{}".format(range_value_1))

for x in range_value_1:
    print("Range elements: {}".format(x))
