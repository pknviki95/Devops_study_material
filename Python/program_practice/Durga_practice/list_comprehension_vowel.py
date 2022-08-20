'''
Write a program to get unique vowel in the word
'''

vowels=['a','e','i','o','u']

word=input("Enter the word: ")\

list1=[x for x in vowels if x in word]
print("List1 value={} and length of list1={}".format(list1,len(list1)))
