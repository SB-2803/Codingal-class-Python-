from datetime import date

for m in range(1, 13):
    month_name = date(2026,m,1)
    # The :%B inside the brackets formats the date as a full month name
    print(f"{month_name:%B}")