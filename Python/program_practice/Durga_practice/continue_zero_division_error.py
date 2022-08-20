'''
Write a program to skip value floor divisible by zero from list and divide other value
'''

list_1=[12,4,6,8,0,10,40,0,0,0,3]

for x in list_1:
    if x==0:
        print("The current value has 0,Skipping that part")
        continue
    print("Divisible value 100//{}={}".format(x,100//x))
