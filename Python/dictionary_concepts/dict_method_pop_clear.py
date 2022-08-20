#--------------------------------------------
#   pop(),popitem(),clear()
#-------------------------------------------


dict1={1:'viki',2:'guru',3:'vijay',4:'siva'}



#dict.pop(key)


print("The pop removes and return value of the key : {}".format(dict1.pop(1)))
print("current value: {}".format(dict1))

#Note:

#print("The pop removes and return value of the key : {}".format(dict1.pop(5)))     #key is absent it throws keyerror
#print("current value: {}".format(dict1))


#dict.pop(key,default_value)

print("The pop removes and return value of the key : {}".format(dict1.pop(7,'Guest')))

print("current value: {}".format(dict1))



#dict.popitem()

print("The popitem removes arbitrary items and return items removed from dictionary : {}".format(dict1.popitem()))
print("current value: {}".format(dict1))


#Note:
dict2={}

#print(dict2.popitem())              #it returns key error if popitem used in empty dictionary



#dict.clear()

dict3={1:'viki',2:'guru',3:'vijay',4:'siva'}

dict3.clear()

print("returns empty dictionary: {}".format(dict3))
