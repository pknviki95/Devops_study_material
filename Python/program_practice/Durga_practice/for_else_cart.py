'''
write a program to check the cart value if greater than 500 and request for insurance with for-else break
'''

cart=[10,30,45,78,90,600,540,500,12]


for x in cart:
    if x>500:
        print("cart value:{} is greater than 500".format(x))
        break
    print("processing the item {}".format(x))
else:
    print("Congratulation for the purchase")

