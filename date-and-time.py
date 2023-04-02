# work on date and time assuming they logged in already
from datetime import date
day = date.today().day; month = date.today().month; year = date.today().year
if(month == 1): month = "January"
elif(month == 2): month = "February"
elif(month == 3): month = "March"
elif(month == 4): month = "April"
elif(month == 5): month = "May"
elif(month == 6): month = "June"
elif(month == 7): month = "July"
elif(month == 8): month = "August"
elif(month == 9): month = "September"
elif(month == 10): month = "October"
elif(month == 11): month = "November"
else: month = "December"

print("today's date:",month,day,year)