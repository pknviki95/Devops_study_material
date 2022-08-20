'''
write a program to break the execution if the price of product is greater than 500
'''


item_price=[10,20,40,90,150,620,300,540,98,700,940]

for x in item_price:
    if x>500:
        print("Neglect the item as rate is {} which is greater than 500".format(x))
        break
    else:
        print("Selected items {} as it is lower than 500".format(x))


