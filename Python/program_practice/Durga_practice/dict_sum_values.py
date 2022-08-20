'''
write a program to get dictionary input form user and print sum of values
'''

dict1=eval(input("Enter dictionary input: "))                #{'A':1,'B':5}


sum1=0

#using dict.values()
'''
for values in dict1.values():
    sum1=sum1+values                                        # 0+1,1+5 => 6
    print("Sum1 value after iteration",sum1)
print("Total sum of dictionary values={}".format(sum1))
'''

#using dict.items()
'''
for items in dict1.items():
    sum1=sum1+items[1]
    print("Sum1 value after iteration",sum1)
print("Total sum of dictionary values={}".format(sum1))
'''

#using sum method

print("sum of values={}".format(sum(dict1.values())))
