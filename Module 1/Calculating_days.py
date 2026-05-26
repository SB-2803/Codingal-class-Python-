num = int(input("Enter the Number of Days : "))

year = int(num // 365)
week = int((num % 365) // 7)
days = int ((num % 365) % 7)

print("Total number of year(s):",year)
print("Total number of week(s):",week)
print("Total number of day(s):",days)
