#------------------------------------
# syntax:
#
# for loop: 
#for x in sequence: 
#    if condition: 
#       break 
#------------------------------------
#------------------------------------ 
#syntax:
#
#while loop: 
#while condition: 
#   if condition: 
#       break 
#-------------------------------------




#for loop:

for x in range(10):
    if x==9:
        print("breaking as the value:{} is equal to 9".format(x))
        break
    else:
        print("The value {} is not equal to 9".format(x))
print("The break comes out of loop as the condition passes")


#while loop

i=0

while i<10:
    if i==8:
        print("breaking value {} is equal to 8".format(i))
        break
    else:
        print("The value {} is not equal to 8".format(i))
    i+=1
print("The Break exits the loops as it passes in condition")


#Error in break
# break should be used only inside loop

y=10

if x<30:
    print("x is less than 30")
    break
else:
    print("x is greater than y")
