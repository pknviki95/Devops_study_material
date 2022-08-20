'''
write a program to print odd numbers between 0 to 10 using range
'''
#count=0
for i in range(20):
    if i%2!=0:
        print("{} is odd number".format(i))
    elif i%2==0:
        print("{} is even number".format(i))

