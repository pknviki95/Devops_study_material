'''
write program to get key based on values and values based on key
'''

dict1={1:'viki',2:'guru',3:'vijay',4:'siva',5:'viki'} 

'''
key=int(input("Enter key element: "))
if key in dict1:
    print("The key {} has value {}".format(key,dict1[key]))
else:
    print("The key {} is not present in dict1".format(key))
'''

values=input("Enter value element: ")
available=False
for k,v in dict1.items():
    if v==values:
        print("available key {} for {}".format(k,v))
        available=True

if available==False:
    print("The value {} is not present in dict1".format(values))
    


