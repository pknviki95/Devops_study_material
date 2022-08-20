#--------------------------------------------------
#Syntax:
#    [true_value] if condition else [false_value]
#--------------------------------------------------


#ternary

a=10;b=20
c=30 if a>b else 40  # true_value if condition else false_value
print("Ternary value : {}".format(c))



#Nested Ternary program

first_number=int(input("Enter first number: "))
second_number=int(input("Enter Second number: "))

print("Both number is same") if first_number==second_number else print("First number is smaller than second_number") if first_number<second_number else print("First number is Greater than second_number")

