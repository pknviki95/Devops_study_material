'''
write a program to print number of occurance of each vowels in the given string
'''

string=input("Enter the string: ")

vowels={'a','e','i','o','u'}

dict1={}

for char in string:
    if char in vowels:
        dict1[char]=dict1.get(char,0)+1

print("Total number of vowels in string:{}".format(dict1))
