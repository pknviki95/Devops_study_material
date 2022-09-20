'''
Write function to get Students name and print wish message with his name
'''
def std_wish(std_name):
    print("Hi {},Wish you a happy life!".format(std_name))

student_name=input("Enter student Name: ")
std_wish(student_name)