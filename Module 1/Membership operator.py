math = int(input("Enter your marks in maths:"))
eng = int(input("Enter your marks in english:"))
hindi = int(input("Enter your marks in hindi:"))
sci = int(input("Enter your marks in science:"))
comp = int(input("Enter your marks in computer:"))

Total = math + eng + hindi + sci + comp
print("Your total marks out of 500 is",Total)

avg = int(Total / 5)
print("Your average marks of all 5 subjects is", avg)

validrange = range(0 , 101)

if avg not in validrange:
    print("Invalid Input!!")
elif avg in range(91 , 101):
    print("Your grade is A1.")
elif avg in range(81 , 91):
    print("Your grade is A2.")
elif avg in range(71 , 81):
    print("Your grade is B1.")
elif avg in range(61 , 71):
    print("Your grade is B2")
elif avg in range(41 , 61):
    print("Your grade is C1")
elif avg in range(21 , 41):
    print("Your grade is C2")
elif avg in range(0 , 21):
    print("Your grade is D.")
