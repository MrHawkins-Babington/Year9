#date stage 4

import calendar
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
d2 = today.strftime("%d")
d3 = today.strftime("%m")
d4 = today.strftime("%Y")
d5 = calendar.day_name[today.weekday()]

print("Today's date =", d1)
print("The current day =", d2)
print("the current month =", d3)
print("The current year =", d4)
print("Today is a ",d5)
