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

print(d['cars'][0])
print(d['mobile'][2])

#using d.get(key)

print(d.get('cars')[2])
