'''
Write a program to check whether the number is prime or not
'''

number=int(input("Enter the number: "))


is_prime=True

for x in range(2,number):
   #121 print(x)
    if number%x==0:
        is_prime=False
        break

if is_prime==True:
    print("Prime")
else:
    print("Not prime")
