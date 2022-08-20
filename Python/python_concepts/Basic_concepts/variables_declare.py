
#Integer

x=11
print("X value is:",x)
print(type(x))
print("x address is:",id(x))

#float
y=4.5
print("Y value is:",y)
print(type(y))
print("y address is:",id(y))
#complex
z=4+5j
print("Z value is:",z)
print(type(z))


#id() fn with same variable value -> same memory address

w=11
print("w address is:",id(w))


#Deleting a variable

del (w)
print(w)
