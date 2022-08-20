##########################################################
#Formatted printing
#
# syntax:
#    {} - This is updated based on variable count with in quotes
#
#    print("{}".format(var1))
##########################################################

x=1
y=2.5
z="hello"

print("x value is:{},y value is:{},z value is:{}".format(x,y,z))


##################
# f-string printing
#
# Syntax:
#    print(f"{}")
##################

print(f"x value is:{x},y value is:{y},z value is:{z}")

##################################
# print with sep and end parameter
##################################
lsit_value=[1,2,3]

#end with \n
for i in lsit_value:
    print(f"lsit_value: {i}",end='\n', sep='---')

#end with \t
for i in lsit_value:
    print(f"lsit_value: {i}",end='\t', sep='---')


#for formatting a date
print('09','12','2016', sep='-')

#====================
# rawstring
#
# Syntax:
#   print(r' ')
#====================

print('\\system07\C$\new')

print(r'\\system07\C$\new')

