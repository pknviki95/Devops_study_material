'''
Write a program to continue with execution by skipping the product greater than 500 rupees
'''

item_price=[10,20,40,90,150,620,300,540,98,700,940]


for x in item_price:
    if x>500:
        print("The item {} is greater than 500".format(x))
        continue
    print("The item {} is lesser than 500".format(x)) 
