##########################################
# String : Slicing
#
# Syntax: str[start:end:step]
#
##########################################



#printing the sub-string from Positive index value

string="vignesh"

print(f"Printing zero index value:{string[0]}")
print(f"Printing second index value:{string[1]}")

#length of the string
print(f"Length of string: {len(string)}")

#printing the sub-string from Negative index value

print(f"printing values using negative index:{string[-1]}")

#printing from start of the string
print(f"Printing from zero index value:{string[0:]}")

#printing from specific index value of the string
print(f"Printing from 2nd index value:{string[2:]}")

#printing the string from Negative index value (Reverse of the string)

print(f"printing reverse of the string:{string[::-1]}")

#printing the string from Specific Negative index value

print(f"printing values from negative index -3:{string[-3:]}")

#slicing the string with specific index with step

# prints from 0 index ends at 5 th index with step 2
print(f"string index sliced value: {string[0:5:2]}")

#String Multiple printing

print(f"multiple print string:{string*2}")


#string Concatination
value="waran"
print(f"String concatination: {string+value}")

#str+int

print(f"string + int :{string+2}")

