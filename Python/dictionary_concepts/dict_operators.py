#Arithmetic operator  -> Not possible
'''
dict1={1:'viki',2:'guru'}

dict2={3:'viki',4:'siva'}

print(dict1*3)

print(dict1+dict2)
'''

#Equality Operator -> Possible


#Dictionary with same value returns True

dict1={1:'viki',2:'guru'}
dict2={1:'viki',2:'guru'}
print(dict1==dict2)

#Dictionary with Different key value returns False

dict3={1:'viki',2:'guru'}
dict4={3:'viki',4:'siva'}
print(dict3==dict4)



#Membership operator

print(1 in dict3)

print(4 in dict1)
