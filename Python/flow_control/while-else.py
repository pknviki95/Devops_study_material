#--------------------------------------
# while-else
#
# Syntax:
#
# while condition:
#   STATEMENT
# else:
#   STATEMENT
#--------------------------------------


#while-else without break

i=1

while i<=6:
    if i%2==0:
        print("{} is Even number".format(i))
    i+=1
else:
    print("The number {} is odd".format(i))


#while-else with break

i=1

while i<=6:
    if i%2==0:
        print("{} is Even number".format(i))
        break
    i+=1
else:
    print("The number {} is odd".format(i))
