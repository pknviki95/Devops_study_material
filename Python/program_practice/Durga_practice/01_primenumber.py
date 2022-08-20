'''
Write a program to print prime numbers less than equal to number
'''


number=int(input("Enter the number: "))


i=1

while i<=number:
    is_prime=True
    for x in range(2,number):
        if number%x==0:
            is_prime=False
            break
    i+=1
if is_prime==True:
    print("prime")
else:
    print("Not prime")

