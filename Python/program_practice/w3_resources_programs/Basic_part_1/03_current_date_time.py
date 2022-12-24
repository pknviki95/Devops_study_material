'''
3. Write a Python program to display the current date and time.
'''

#-----------------------------------------------------------------------------------------------
#   datetime.datetime.<method> - It is used to work on date and time using python
#       Based on above requirement:
#               datetime.datetime.now() - It returns current date and time of host machine
#------------------------------------------------------------------------------------------------


import datetime

current_date_time=datetime.datetime.now()
print("current date and time:\n{}".format(current_date_time))