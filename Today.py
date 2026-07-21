from datetime import date, datetime

#calling the today
#function of date class
today = date.today()
now = datetime.now()
print("Today's date is:",today)
print("Right now the time is:",now)

#Printing date's components
print("\nDate component like year, month and day are:",today.year, today.month, today.day)