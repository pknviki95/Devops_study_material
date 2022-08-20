#--------------------------------
# for-else
# syntax:
#
# for x in sequence:
#       STATEMENT
# else:
#       STATEMENT
#--------------------------------

#for-else without break statement                                #It executes else part atleast once as the for loop fails

for x in range(1,10):                                            #1,2,3,4,5,6,7,8,9
    if x%2==0:                                                   #2,4,6,8
        print("{} is even".format(x))
else:                                                            #9
        print("{} is odd".format(x))


#for-else with break statement                                    #It terminates entirely from for-else loop if the condition in if is True

for x in range(1,10):                                            #1,2,3,4,5,6,7,8,9
    if x%2==0:                                                   #2
        print("{} is even".format(x))
        break
else:                                                            #It exits the for-else loop as 2 is even
        print("{} is odd".format(x))

