'''
Write a program to implement nested collection and access Supermarket data
'''

supermarket={'store1':{'name':'Durga general stores','items':[{'name':'soap','quantity':20},{'name':'brush','quantity':30},{'name':'paste','quantity':40}]},'store2':{'name':'Ranga general stores','items':[{'name':'polish','quantity':20},{'name':'harpic','quantity':30},{'name':'water','quantity':40}]}}

print(supermarket.get('store1').get('name'))    
print(supermarket.get('store1').get('items')[0].get('name'))

for dict_1 in supermarket.get('store1').get('items'):
    print(dict_1.get('name'))
    print(dict_1.get('quantity'))

print(supermarket.get('store2').get('items'))

# To get quantity of items in store2:

name_input=input("Enter the name of item to search in store2: ")

for dict_2 in supermarket.get('store2').get('items'):
    if name_input==dict_2.get('name'):
        print("The quantity for name:{} is {}".format(name_input,dict_2.get('quantity')))
