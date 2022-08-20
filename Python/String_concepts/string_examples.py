########################################
#String Examples
########################################
#Empty String

empty_str=""

print(f"str:{bool(empty_str)}")

#string initialization with space
space=" "
print(f"String initialization with space:{bool(space)}")

# single quotes for word:

my_name='Vignesh'
print(f"My name is : {my_name}",type(my_name))

# Double quotes foe sentence:

my_place="I am from Ramanathapuram"
print(f"where you live : {my_place}",type(my_name))

# Triple quotes for sentences:

sentence='''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

print(f"Sentences : {sentence}",type(sentence))


# Multiple string printing using f-string:

print(f"This is for new line printing: \nmy name is : {my_name}\n my place is: {my_place}\n my sentence is : {sentence}")

print(f"This is for new tab printing: \n is  my name is : {my_name}\t my place is: {my_place}\t my sentence is : {sentence}")

#String immutable

string="Guru"
str[0]="R"
