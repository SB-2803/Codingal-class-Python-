# Taking input from user
print("Enter marks obtained in the following 4 subjects :")
Maths = int(input("Maths :"))
eng = int(input("English :"))
sci = int(input("Science :"))
hindi = int(input("Hindi :"))

#Let us calculate the percentage of the marks
sum = Maths + eng + sci + hindi
print("Sum of marks of Maths, Eng, Sci and Hindi is:", sum)

per = (sum/400)*100

print(end = "Percentage of Marks = ")
print(per, "%")