

#Adding/Assigning value to dicts keys:

dict1={}

print("Adding value to key...")

dict1[100]='viki'

print("Adding Dict1 value:{}".format(dict1))

#Accessing the value of key in dict:

dict2={1:'viki',2:'geuru',3:'gokul'}

print("Accessing the key value of dict...")

print("dict2[key] : {}".format(dict2[1]))
print("dict2[key] : {}".format(dict2[2]))
print("dict2[key] : {}".format(dict2[3]))

#Accessing the absent key value of dict throws keyerror
#print("dict2[key] : {}".format(dict2[4]))

#deleting key value in dict

#print("Deleting key in dict...")

#del dict2[1]

print("After deleting:{}".format(dict2))

print("Length of the dictionary: {}".format(len(dict2)))
