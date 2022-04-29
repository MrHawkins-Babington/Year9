#date stage 3

import calendar
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
d2 = today.strftime("%d")
d3 = today.strftime("%m")
d4 = today.strftime("%Y")

#this prints out the current date
print( d1)
