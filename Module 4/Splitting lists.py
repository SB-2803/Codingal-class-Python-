#Original list
my_list = [10,20,30,40,50,60,70]

#Finding the middle index
mid = len(my_list)//2

#Splitting the list
first_half = my_list[:mid]
second_half = my_list[mid:]

print("Original List:",my_list)
print("First Half:",first_half)
print("Second Half:",second_half)