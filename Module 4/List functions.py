L = [4,5,1,2,9,7,10,8]
print("Original list:",L)

#variable to store the sum of the list
sum = 0
for i in L:
    sum+=i

#finding the average of the list
avg = sum/len(L)

print("Sum:",sum)
print("Average:",avg)

#Sorting the list
L.sort()
print("Sorted list(ascending order):",L)

#printing the smallest element
print("Smallest element is:",L[0])

#printing the largest element
print("largest element is:",L[-1])

sum = 1
#finding the product of the list
for i in L:
    sum *= i
print("Product of all ements of the list is:",sum)