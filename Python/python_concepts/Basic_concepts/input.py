'''
input() fn
'''



val=input("Enter the value: ")
print(val,type(val))  #input() always returns string type


a=input("Enter the value a: ")
b=input("Enter the value b: ")

cal=a+b

print(cal,type(cal))

# To convert string Expression to integer (i.e) to perform arithmetic operation using input fn() 

a=eval(input("Enter the value a: "))
b=eval(input("Enter the value b: "))

cal=a+b

print(cal,type(cal))

# To convert input value to integer datatype

int_val1=int(input("Enter the value: "))
int_val2=int(input("enter the value: "))

ans=int_val1+int_val2
print(ans,type(ans))
