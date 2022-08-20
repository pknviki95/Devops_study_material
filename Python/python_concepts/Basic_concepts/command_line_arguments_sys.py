# case 1:

'''
import sys

print("Command line output:{}".format(sys.argv))

print("Command line output argv[0]:{}".format(sys.argv[0]))
print("Command line output argv[1]:{}".format(sys.argv[1]))
print("Command line output argv[2]:{}".format(sys.argv[2]))
'''
#case 2
#from sys import argv

#case 3

from sys import *

print("Command line output:{}".format(argv))

#length of command line arguments:

print("print length of argument: {}".format(len(argv)))

print("Command line output argv[0]:{}".format(argv[0]))
print("Command line output argv[1]:{}".format(argv[1]))
print("Command line output argv[2]:{}".format(argv[2]))

print(argv[0]+argv[1])

print(argv[100])

