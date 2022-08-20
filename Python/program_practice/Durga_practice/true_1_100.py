'''
Write a program to check if number is between 1 to 100
'''

a=int(input("Enter the number: "))

if a>=1 and a<=100:
    print("The number {} is between 1 to 100".format(a))
else:
    print("The number {} is not between 1 to 100".format(a))
