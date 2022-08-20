#------------------------------------------------------------------------------------------------------------
# Dictionary operation:
#   clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
#
#------------------------------------------------------------------------------------------------------------


dict1={1:'viki',2:'guru',3:'vijay',4:'siva'} 


key=dict1.keys()

print("Key elements {} and return type {}".format(key,type(key)))

values=dict1.values()

print("value elements {} and return type {}".format(values,type(values)))

items=dict1.items()         #list of tuples

print("items elements {} and return type {}".format(items,type(items)))


#Accessing dictionary element through looping

for i in key:               #key=dict1.keys()
    print(i)


for j in values:            #values=dict1.values()
    print(j)

for k,v in items:           #items=dict1.items()
    print(k,v)              #k=key v=value     (i.e) dict_items return list of Tuples which intern elements can be individually accessed by k,v
