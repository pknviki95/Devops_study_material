#-------------------
# nested continue
#-------------------

#nested for continue:

for x in range(3):
    for y in range(3):
        if x==y:
            continue
        print("The value of x:{} and y:{}".format(x,y))

#nested while continue:


i=0

while i<3:
    j=0
    i+=1
    while j<3:
        j+=1
        if i%2==0:
            continue
    print("The value of i:{} and j:{}".format(i,j))
#have some doubt in this
