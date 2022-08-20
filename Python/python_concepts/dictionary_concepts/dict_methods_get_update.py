#------------------------------------------------------------------------------------------------------------
# Dictionary operation:
#   clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
#
#------------------------------------------------------------------------------------------------------------


dict1={1:'viki',2:'guru',3:'vijay',4:'siva'}

#get method

#dict.get(key)

key=int(input("Enter the key value: "))
print("dict1 value of key : {}".format(dict1.get(key)))

#get method for absent keys to return with specific default value

#dict.get(key,default_value)

print("dict1 value of key : {}".format(dict1.get(key,'Key is absent')))

#Update method
#dict.update(dict_1)

dict2={5:'ram',6:'don'}
dict1.update(dict2)
print("Updateing the dict1 with dict2 value : {}".format(dict1))


