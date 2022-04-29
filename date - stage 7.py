#date stage 6

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
print("The current year is", d4)
print("Today is a ",d5)

monthNow = d3
monthNow = int(monthNow[1])
print(monthNow)

if monthNow == 1:
    month = "January"
    print("The current month is ",month)
elif monthNow == 2:
    month = "February"
    print("The current month is ",month)
elif monthNow == 3:
    month = "March"
    print("The current month is ",month)
elif monthNow == 4:
    month = "April"
    days = 30
    daysleft = days - int(d2)
    print("The current month is ",month)
    print(daysleft,"days left in ",month)
else:
    print("error")



