

my_value= [1,2,3.5,'viki',[1,2]]

#length of the list

print(f"Length of the list: {len(my_value)}")

#Positive index value

print(f"Positive index value: {my_value[0]}")

#Negative index value

print(f"Negative index value: {my_value[-2]}")

#print except first and last element of list

print(f"Print except first and last: {my_value[1:-1]}")

#print with step

print(f"Print with step: {my_value[0:4:2]}")


#Modifing the list index value

my_value[2]='siva'

print(f"Modifying index value:{my_value}")

#Nesting of lists

print(f"Nesting of lists accessing the substring of index string value: {my_value[2][1]}")

#Modifying nested index value

my_value[4][1]=3

print(f"Modifying specific nested list index value:{my_value}")


#list concatenation
my_value_2=[1,2]
print(f"list concatenation: {my_value+my_value_2}")

#Multiple list 

print(f"list multiple : {my_value_2*2}")
