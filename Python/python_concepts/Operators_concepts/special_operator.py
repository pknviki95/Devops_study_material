#--------------------------------------
# Identity operator => is , is not
# Membership operator => in , not in
#--------------------------------------

#Identity operator

a=10
b=10
c=20

print("Address of a:{}\nAddress of b:{}\nAddress of c:{}".format(id(a),id(b),id(c)))


print("a is equal to b: {}".format(a is b))
print("a is equal to c: {}".format(a is c))

#is not

print("a is not equal to b:{}".format(a is not b))
print("a is not equal to c:{}".format(a is not c))

l1=[10,20,30,40]
l2=[10,20,30,40]

print(id(l1),id(l2))
print(l1 is l2)

print(l1==l2)
print(id(l1),id(l2))
print(l1 is l2)

#membership operator

#in

print("Value is in l1:{}".format(10 in l1))

#not in

print("Value is not in l1:{}".format(50 not in l1))


