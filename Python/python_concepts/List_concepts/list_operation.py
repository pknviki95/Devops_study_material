#-------------------------------------------------------------------------------------------------------
# List Operations:
#   count(),index(),append(),copy(),insert(),pop(),reverse(),sort(),sorted(),clear(),extend()i,remove()
#-------------------------------------------------------------------------------------------------------


# list functions

my_value= [1,2,3.5,'viki',[1,2],2,5,8] 
print(f"List functions: \n {dir(my_value)}")


#count(value)

print(f"count value of list_elemet: {my_value.count(2)}")

#index(value)

print(f"Print the index value of list element: {my_value.index(3.5)}")

#index(value,index_value)

print(f"Print index value of list element from specific index: {my_value.index(2,3)}")

'''
#clear()

lsit1=[1,2,3,4,5]

print(f"clearing the list elements:{list1.clear()}")
print(list1)
'''

#copy()

list_1=[1,2,3,4,5]
list_2=list_1
print(f"list variable memory address with assignment operator: list_1,list_2{id(list_1),id(list_2)}")
list_2=list_1.copy()
print(f"Printing memory address after list copy:list_1,list_2{id(list_1),id(list_2)}")

#append(value)

list_2.append(25)
print(f"Append at the end on list_2:{list_2}")

list_2.append([21,22])
print(f"Append list element into list: {list_2}")

#extend(value)

list_2.extend((23,45))
print(f"extending the list_elements with_extend: {list_2}")


#insert(index_position,value)

list_2.insert(1,45)
print(f"Inserting the valuein first index: {list_2}")


#remove(value)

list_2.remove(45)
print(f"Removing list elements: {list_2}")

#pop()

list_2.pop()
print(f"printing list after removing last element using pop(): {list_2}")

#reverse()

list_2.reverse()
print(f"Reversed list elements: {list_2}")

#sort()
list_sort=[1,2,3,4,5,7,6,9,8]
list_sort.sort()
print(f"Sorting the list elements in Ascending order: {list_sort}")

#sort(reverse=True)

list_sort.sort(reverse=True)
print(f"Sorting the value in Descending order: {list_sort}")

#Sort Operation only applicable for SAME DATATYPES

list_eg=[[5,4],[1,2],1]
lst_eg=list_eg.sort()
print(list_eg)
