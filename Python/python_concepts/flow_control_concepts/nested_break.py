#----------------------------
# nested break
#----------------------------

#nested for break

for x in range(3):
    for y in range(3):
        if x==y:
            break
        print("The not-equal value of x:{} and y:{}".format(x,y))

#nested while break

i=0

while i<3:
    j=0
    while j<3:
        if i==j:
            break
        j+=1
    i+=1
    print("The value of i:{} and j:{}".format(i,j))

