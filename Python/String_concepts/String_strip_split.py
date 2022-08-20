#------------------------------------------------------
#strip() and split() function
#
#Syntax
# string.strip([char])
#------------------------------------------------------


string="Vignesh"

#strip()

print(f"String striped : {string.strip('nesh')}")

#by default it takes out spaces

string1="python course for python study"

print(f"String strips spaces by default:{string1.strip()}")


#lstrip()

print(f"String lstrips spaces by default:{string1.lstrip('python')}")

#rstrip()

print(f"String rstrips spaces by default:{string1.rstrip('study')}")



#split()

print(f"String after splitting: {string1.split()}")

split_comma="python,c,C++"

print(f"String splitting with specific character: {split_comma.split(',')}")
