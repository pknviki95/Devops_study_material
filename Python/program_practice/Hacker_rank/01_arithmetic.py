'''
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a//b . 
The second line should contain the result of float division, a/b .

No rounding or formatting is necessary.
'''

a = int(input("Enter the number for a: "))
b = int(input("Enter the number for b: "))

#Integer division/floor division

print("floor division:{}".format(a//b))

#float Division

print("division:{}".format(a/b))
