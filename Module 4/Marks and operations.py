marks = input("Enter you marks:")
total_marks = int(input("Enter the total marks for each subject:"))
L = [int(i) for i in marks.split(",")]
print("Original marks:",L)

#variable to store the sum of the list
total_sum = 0
for i in L:
    total_sum+=i

#finding the average of the list
avg = total_sum/len(L)

print("Sum of all the marks:",total_sum)
print("Its average:",avg)

prod = 1
#finding the product of the list
for i in L:
    prod *= i
print("Product of all the marks obtained is:",prod)

#Sorting the list
L.sort()
print("Sorted marks(ascending order):",L)

#printing the smallest element
print("Lowest mark is:",L[0])

#printing the largest element
print("Highest element is:",L[-1])

#finding average percentage of all the marks
avg_p = total_sum/(len(L)*total_marks)*100
print("Average percentage is:",avg_p)