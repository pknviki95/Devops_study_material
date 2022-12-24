#----------------------------------------------------------
#   datetime.date.<method>
#----------------------------------------------------------


#To get the current date using date class

import datetime
# This returns current date
current_date=datetime.date.today()
print("The current date :{}".format(current_date))

# To print specific date using date class

specific_date=datetime.date(1995,8,31)     #datetime.date(year,month,day)
print(specific_date)

#To print specific year,date,day of a date using year,month,day method

print("Year of date:{}".format(specific_date.year))
print("Month of date:{}".format(specific_date.month))
print("day of the date:{}".format(specific_date.day))

print(datetime.date(2000,7,31).year)