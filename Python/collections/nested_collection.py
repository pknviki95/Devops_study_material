#---------------------------------------
#   Nested collection
#---------------------------------------



#list of tuples:

#Accessing lements inside NEsted collection


l1=[(10,20,30),(40,50,60)]


print("printing first index value of list of tuple:{}".format(l1[0]))
print("printing second index value of list of tuple:{}".format(l1[1]))


print("printing first index value of list and second index value of tuple:{}".format(l1[0][2]))
print("printing second index value of list and second index value tuple:{}".format(l1[1][2]))


#collection inside Dictionary

d={'cars':('Innova','Honda','santro'),'mobile':('samsung','nokia','oppo')}

print(d.keys())
print(d.values())

print("printing the dictionary key's zeroth index values:{}".format(d['cars'][0]))
print("printing the dictionary key's second index values:{}".format(d['mobile'][2]))

#using d.get(key)

print(d.get('cars')[2])

#Dictionary of list values: (POSSIBLE)

d1={'cars':['Innova','Honda','santro'],'mobile':['samsung','nokia','oppo']}

print(d1.keys())
print(d1.values())

print("printing the dictionary key's zeroth index values:{}".format(d1['cars'][0]))
print("printing the dictionary key's second index values:{}".format(d1['mobile'][2]))

#Dictionary of list key: (NOT POSSIBLE)
'''
d2={['Innova','Honda','santro']:(10,20,30),'mobile':['samsung','nokia','oppo']}

print(d2.keys())
print(d2.values())

print("printing the dictionary key's zeroth index values:{}".format(d2['cars'][0]))
print("printing the dictionary key's second index values:{}".format(d2['mobile'][2]))
'''
#Set of tuples

s2={(1,2,3),(4,5,6)}

print("print set of tuples:{}".format(s2))

#Set of lists

s1={[1,2,3],[4,5,6]}

print("print set of set:{}".format(s1))