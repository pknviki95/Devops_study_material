#----------------------------------
# Dictionary Datatype:
# syntax:
#   dict={key:value}
#----------------------------------




#Empty Dictionary

d={}

#print(dir(d))

print("Type of d: {}".format(type(d)))
print("Empty dictionary: {}".format(bool(d)))

#Dictionary with key:value


d1={1:'viki'}

print("dictionary with elements: {}".format(bool(d1)))


#To create dict value from other collections using dict() function:

#List of tuples to dict()

list1=[(100,'A'),(200,'B'),(300,'C')]
print("List of Tuple element: {} with the type of list1:{}".format(list1,type(list1)))


dict1=dict(list1)
print("Converting List of Tuple element: {} with the type of dict1:{}".format(dict1,type(dict1)))

#list of list to dict()

list2=[[2,'viki'],[3,'siva'],[5,'guru']]

print("List of list element: {} with the type of list2:{}".format(list2,type(list2)))

dict2=dict(list2)
print("Converting List of list element: {} with the type of dict2:{}".format(dict2,type(dict2)))

#Tuples of list to dict()

tuple1=([2,'viki'],[3,'siva'],[5,'guru'])

print("Tuples of list  element: {} with the type of Tuple1:{}".format(tuple1,type(tuple1)))

dict3=dict(tuple1)
print("Converting Tuples of list element: {} with the type of dict3:{}".format(dict3,type(dict3)))


#sets of tuple to dict()

set1={(100,'A'),(200,'B'),(300,'C')}

print("sets of Tuples element: {} with the type of set1:{}".format(set1,type(set1)))

dict4=dict(set1)
print("Converting sets of list element: {} with the type of dict4:{}".format(dict4,type(dict4)))


#tuple of tuple to dict()

tuple2=((100,'A'),(200,'B'),(300,'C'))

print("Tuple of Tuples element: {} with the type of tuple2:{}".format(tuple2,type(tuple2)))

dict5=dict(tuple2)
print("Converting Tuples of Tuples element: {} with the type of dict5:{}".format(dict5,type(dict5)))

#Tuple of set to dict()

tuple3=({100,'A'},{200,'B'},{300,'C'})

print("Tuples of set  element: {} with the type of tuple3:{}".format(tuple3,type(tuple3)))

dict6=dict(tuple3)
print("Converting Tuple of sets element: {} with the type of dict6:{}".format(dict6,type(dict6)))


#list of set to dict()

list3=[{2,'viki'},{3,'siva'},{5,'guru'}]

print("List of set element: {} with the type of list3:{}".format(list3,type(list3)))

dict7=dict(list3)
print("Converting List of set element: {} with the type of dict7:{}".format(dict7,type(dict7)))

'''
NOTE:
    Set of list {[]} -> Not possible
    List of sets [{}] -> Possible
'''

#set of lists to dict()

set2={[2,'viki'],[3,'siva'],[5,'guru']}

print("set of list element: {} with the type of set2:{}".format(set2,type(set2)))

dict8=dict(set2)
print("Converting set of list element: {} with the type of dict8:{}".format(dict8,type(dict8)))
