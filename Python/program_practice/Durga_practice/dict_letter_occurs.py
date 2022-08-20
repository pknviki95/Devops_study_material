'''
write a program to find the number of occurance of each letter in a string
'''

string=input("Enter the string: ")

dict1={}

for char in string:
    dict1[char]=dict1.get(char,0)+1  #get method to gwt value of key dict1[v]=0+1 => here key is v and value is 1 updates to dict1 as dict1[v1] is used for assigning
print(dict1)



'''
char => viki

dict1.get(char,0)+1 
    - The key v is not present so it returns 0 value 1 then updates key value to dict1 by dict1[char]
    - likewise it add i and k into dict1
    -again when it comes with i dict1.get(char,0) => dict1.get(i,0) key i is already present in dict1 wih value 0 so 0+1 it updates value=2 to existing key
'''

