"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# with sys.args, the file name is the arg at [0], so there is technically one arg
# .textCalendar
cal = calendar
cal.setfirstweekday(calendar.SUNDAY)
d = datetime.now()

# if len(sys.argv) == 1:
#     month = d.month
#     currentYear = d.year
#     print(cal.monthcalendar(currentYear, month), f"Month and year: {month}, {currentYear}")
if len(sys.argv) == 1:
    month = d.month
    currentYear = d.year
    print(cal.month(currentYear, month))

elif len(sys.argv) == 2:
    month = int(sys.argv[1])
    currentYear = d.year
    print(cal.month(currentYear, month))

elif len(sys.argv) == 3:
    month = int(sys.argv[1])
    currentYear = int(sys.argv[2])
    print(cal.month(currentYear, month))