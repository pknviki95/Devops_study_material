'''
write a program to enter name and marks into a dictionary and display in our screen
'''

#empty dictionary
data={}
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("enter the name : ")
    mark=eval(input("enter the mark: "))
    
    #Adding key:value to dict
    data[name]=mark

print("Student date : {}".format(data))

print("="*25)
print('name'+'\t\t'+'mark')
print("="*25)

for j in data:
    print(j,'\t\t',data[j])
