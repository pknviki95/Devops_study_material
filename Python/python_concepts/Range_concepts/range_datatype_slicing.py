#Positive index value

range_value=range(1,10)

i=0

for x in range_value:
    print("The Range positive index value:{} on range_value:{}".format(i,x))
    i+=1


#Negative index value

range_value_negative=range(20,1,-5)

print(range_value_negative)

for x in range_value_negative:
    print("The Range negative index value:{}".format(x))


#Immutable

range_value_1=(10)

range_value[1]=0
