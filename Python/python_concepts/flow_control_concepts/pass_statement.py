#-----------------------------
#   pass statement
#-----------------------------


#pass statement with conditions

x=int(input("Enter the number: "))

if x<10:
    print("The value is {}".format(x))

else:
    pass


#pass statement with for statement

for i in range(x):
    pass
else:
    print("Executing else statement")


#pass statement with class

class A:
    pass

class B:
    print("printing class B")

#pass statement with function

def fun1(f):
    pass

fun1(10)
