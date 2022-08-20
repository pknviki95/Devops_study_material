#------------------------------------------------------------------
# List comprehension
#   syntax:
#       list= [ expression for i in iterable if condition==True]
#------------------------------------------------------------------





list1=[x for x in range(1,11)]
print(list1)


#even number square value

list2=[x**2 for x in range(1,11) if x%2==0]
print(list2)

#range values squared in list

n=int(input("Enter the number: "))
list3=[x**2 for x in range(1,n)]
print(list3)

#divisible by 10

list4=[x for x in range(1,n) if x%10==0]
print(list4)


#Create new list which from l1 and l2 (i.e) the value present in l1 not in l2 into new list

l1=[10,20,30,40]
l2=[10,40,50,60,70]

list5=[ x for x in l1 if x not in l2]
print(list5)


#Create new list which from l1 and l2 (i.e) the value present in l1 and l2 into new list

list6=[ x for x in l1 if x in l2]
print(list6)

#create a list with first element of string in list

value=['viki','guru','ram']

list7=[x[0] for x in value]
print(list7)



string="A quick brown fox jumped over a lazy dog"
words=string.split()
print(words)
list_str=[[word.upper(),len(word)] for word in words]
print(list_str)
