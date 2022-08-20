'''
write a program to get user input for students name and mark and display in the terminal
'''

student={}
number=int(input("Enter the number of students: "))
        
for i in range(number):
    name=input("Enter students name: ")
    mark=int(input("Enter students mark: "))

    student[name]=mark
print(student)
print("="*25)
print("NAME\t\tMARKS")
print("="*25)

for k,v in student.items():
    print(k,'\t\t',v)


while True:
    name=input("Enter Students name: ")

    marks=student.get(name,-1)

    if marks==-1:
        print("The student name {} is not available".format(name))
        break
    else:
        print("The student name {} corresponding marks={}".format(name,marks))

print("Thanks for using the application")


