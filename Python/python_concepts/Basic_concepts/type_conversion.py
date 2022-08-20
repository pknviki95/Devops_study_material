
'''
String Value to Integer value
'''

#Decimal

x="121"

print(type(x))
print("x=",x)
y=int(x)
print("Y=",y)
print(type(y))


#Octal

Octal="0o1073"

print("Octal=",Octal,type(Octal))

int_octal=int(Octal,base=8)
print("int_octal=",int_octal,type(int_octal))

#hexa

hexa="23b"

print("hexa=",hexa,type(hexa))

int_hex=int(hexa,base=16)
print("int_hex=",int_hex,type(int_hex))

'''
Integer to hexadecimal and octal

'''
#hexadecimal

x=121

print("x=",x,type(x))
print(hex(x),type(x))

#Octal

Octal=0o1073

print("Octal=",Octal,type(Octal))

print(oct(Octal),type(Octal))


'''
Integer to float value
'''

x=121
print(type(x))
print("x=",x)
print(float(x),type(x))

'''
Integer to complex
'''

r=10
i=12
print(r,type(r))
print(complex(r,i),type(r))


'''
Integer to Character
'''

x=121
print(x,type(x))
chr_val=chr(x)
print(chr_val,type(chr_val))

'''
Single character string to Integer
'''

val='a'
print(val,type(val))
ord_val=ord(val)
print(ord_val,type(ord_val))


'''
Integer to string
'''

x=121
print(x,type(x))
str_val=str(x)
print(str_val,type(str_val))

'''
eval() - It converts string expression to integer output
'''

string='1+2*7+24'

print(string,type(string))

eval_value=eval(string)
print(eval_value,type(eval_value))

'''
repr() - It evaluates integer Expression to string output
'''

int_exp=1+2*7+24

print(int_exp,type(int_exp))

repr_val=repr(int_exp)
print(repr_val,type(repr_val))
