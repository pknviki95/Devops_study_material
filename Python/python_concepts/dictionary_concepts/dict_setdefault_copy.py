#------------------------------------
#   setdefault(),copy()
#------------------------------------


dict1={1:'viki',2:'guru',3:'vijay',4:'siva'}

#dict.setdefault(key,value)

#Case1: Key is absent in dictionary:

dict1.setdefault(5,'raju')

print("Updatred dict1 with setdefault:{}".format(dict1))    #key:value updated if key is not present


#Case2: Key is present in dictionary:

print("setdefault returns value of key :{}".format(dict1.setdefault(1,'ravi')))         #key:value is not updated if key is present and returns value of the key

print("current dict1 value:{}".format(dict1))





#dict.copy()

#Aliasing is not right way to copy values to seperate variable as it affects both variable as it shares same memory address 
#To overcome this copy() is used as it updates the variable with seperate memory address (i.e) cloning

dict2=dict1
print(dict1,dict2)
dict1[7]='don'
print("Aliasing of both variable: \ndict1 {}\ndict2 {}".format(dict1,dict2))
print("Memory address of variable: \ndict1={}\ndict2={}".format(id(dict1),id(dict2)))


'''
dict2=dict1.copy()

dict1[7]='rin'
dict2[7]='tom'

print("The current value of dict1:{}\n Memory address of dict1={}".format(dict1,id(dict1)))
print("The current value of dict2:{}\n Memory address of dict2={}".format(dict2,id(dict2)))
'''
