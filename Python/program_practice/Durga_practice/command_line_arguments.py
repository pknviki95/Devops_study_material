'''
Command line arguments:

write a program to find 
    -Total length of command line argument input,
    -print total command line input
    - print individual arguments value
'''    

from sys import *

#length of arguments

print("Length of command line arguments:{}".format(len(argv)))

#Total command line arguments

print("Total of command line arguments:{}".format(argv))

#print individual arguments

print("Command line output argv[0]:{}".format(argv[0]))

print("Command line output argv[1]:{}".format(argv[1]))

print("Command line output argv[2]:{}".format(argv[2]))

