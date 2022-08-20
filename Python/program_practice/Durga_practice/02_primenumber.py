'''
Write a program to print first n prime number
'''


number=int(input("Enter the number: "))


count=0

n1=2

while True:
    is_prime=True
    for x in range(2,n1):
        if n1%x==0:
            is_prime=False
            break
    if is_prime==True:
        print("{} isprime".format(n1))
        count+=1
    if count==number:
        break   
    n1+=1 
