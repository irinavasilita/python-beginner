'''
Exercise to practice modules and datetime
'''
# Import the datetime module
from datetime import datetime

# Create a date using year, month, and day as arguments
birthday = datetime(1998, 8, 5)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())

# Create a date using datetime.now()
now = datetime.now()
print(now)
print(now - birthday)

# Parse a date using strptime
# Go to https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior for reference
parsed_date = datetime.strptime('Jan 15, 2022', '%b %d, %Y')
print(parsed_date)

# Render a date as a string using strftime()
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
