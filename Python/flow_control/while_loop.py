#-------------------------------
# while:
#
# syntax:
#       while condition:
#            statement
#-------------------------------


#while with condition printing

i=0

while i<10:
    print("{} time Hello!".format(i))
    i+=1


#while with string:

string="Vignesh"

value=input("Enter the character: ")
j=0
while j<len(string):
    if value in string:
        print("The value {} is in string {}".format(value,string))
        j+=1
    else:
        print("The value {} is not in string {}".format(value,string))
        j+=1
