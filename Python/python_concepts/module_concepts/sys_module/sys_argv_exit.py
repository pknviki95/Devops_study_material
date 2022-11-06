#----------------------------------------------------------------------------------------------
#   sys.argv -> It is used to pass values at the run-time execution (command-line arguments)
#   sys.exit() -> It is used to exit the python execution/console
#----------------------------------------------------------------------------------------------


import sys

if len(sys.argv) != 3:
    print("The argument value needs 3 values")
    sys.exit()
else:
    for i in sys.argv:
        print(i)
