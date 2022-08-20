#for loop in string:

string="Vigneshwaran M"

for x in string:
    print("Element value is: {}".format(x))

#for loop in list:

list_value=[1,2,3.5,'viki',{1:'viki'}]

for list_element in list_value:
    print("Element value is: {}".format(list_element))


#for loop in dict:

Dict_value={1:'viki',2:'siva',3:'vijay'}

for dict_element in Dict_value:
    print("Element value is: {}".format(dict_element))  # looping in Dictionary only takes key elements

    print("Element value of key is: {}".format(Dict_value[dict_element])) # it access the value element of key element while looping  (i.e) dict_variable[dict_key]

#for loop in range:

range_value_1=range(2,15,2)   #range(start,end,step)

for x in range_value_1:
    print("Range elements: {}".format(x))
