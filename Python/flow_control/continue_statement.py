#------------------------------
# Continue Statement:
#------------------------------
# Syntax:
#foor loop:
#
#   for x in sequence: 
#       if condition: 
#           continue 
#----------------------------

#--------------------------
#while loop
#
#while condition: 
#   if condition: 
#       continue 
#---------------------------



#for loop:

for x in range(10):
    if x%2==0:
        #print("The numbers are even number:{}".format(x))
        continue
    print("The numbers are odd numbers:{}".format(x))

#while loop:

i=0

while i<=10:
    i+=1
    if i%2==0:
        continue
    else:
        print("Continue that prints odd number:{}".format(i))
print("Thanks for the numbers!")


#continue without loop

h=0

if h<=0:
    h+=1
    continue

