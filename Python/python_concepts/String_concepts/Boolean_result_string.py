#--------------------------------------------------------
# Boolean result Operation:
#  This is used to find the Boolean result of string
# (i.e) True or False result
#--------------------------------------------------------

string="Python"

#satrtswith()

print(f"String startswith: {string.startswith('p')}") #It throws False as it has 'p'

#characters of string should match with the string (i.e) Python is case-sensitive

print(f"String startswith: {string.startswith('P')}")

print(f"String startswith: {string.startswith('Pyt')}")

#endswith()

print(f"String endswith: {string.endswith('n')}")

#islower()

print(f"String is lowercase: {string.islower()}") 

#isupper()

print(f"String is Uppercase: {string.isupper()}")

#isdecimal()

dec="01234"

print(f"String is decimal: {dec.isdecimal()}")

#isalpha()

print(f"String is alphabet: {string.isalpha()}")

#isalnum()

alnum="01234abcd"

print(f"String is alphanumeric: {alnum.isalnum()}")

#isdigit()

digit="01234^2"

print(f"String is digit: {digit.isdigit()}")


#isnumeric()
numeric="\u2165"           # \u- Unicode implementation                            
print(f"String is numeric: {numeric.isnumeric()}")

#isspace()

space=" "
print(f"String is space: {space.isspace()}")
space1=""
print(f"String is Space1: {space1.isspace()}")

#istitle()

print(f"String is title: {string.istitle()}")

#isascii()
ascii='A'
print(f"String is ASCII: {ascii.isascii()}")

#isprintable()

printable="Vignesh\twaran"
print(f"String is printable: {printable.isprintable()}")

printable1="Vigneshwaran95@gmail.com"
print(f"String is printable1: {printable1.isprintable()}")
