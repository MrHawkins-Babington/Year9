#date stage 5

import calendar
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
d2 = today.strftime("%d")
d3 = today.strftime("%m")
d4 = today.strftime("%y")
d5 = calendar.day_name[today.weekday()]

print("Today's date =", d1)
print("The current day =", d2)
print("The current month =", d3)
print("The current year is", d4)
print("Today is a ",d5)

monthNow = d3
monthNow = int(monthNow[1])
print(monthNow)



