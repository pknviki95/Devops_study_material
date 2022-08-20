'''
Write a program to sum first n number
'''

sum_value=0

number=int(input("Enter the number: "))

i=1   #iteration control

while i<=number:
    sum_value+=i
    i+=1
print("Sum_value: ",sum_value)
