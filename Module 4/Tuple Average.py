#tuple of numbers
numbers = (10,20,30,40,50)
total_sum = 0
counter = 0

#Calculate sum
for i in numbers:
    total_sum += i
    counter += 1

#Calculate average
avg = total_sum/counter

print("Tuple:",numbers)
print("Average:",avg)