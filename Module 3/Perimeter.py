def per_square(P):
    return 4*P

def per_rectangle(P,Q):
    return 2*(P+Q)

def per_triangle(P,Q,R):
    return P+Q+R

def cir_circle(P):
    return 2*3.14*P

#Now we will take input from the user
print("Please select the operation you want to perform:")
print("1.Perimeter of square")
print("2.Perimeter of rectangle")
print("3.Perimeter of a triangle")
print("4.Circumference of a circle")

choice = int(input("Please enter choice(1/2/3/4):"))

while choice not in (1,2,3,4):
  print("This is an invalid input!!")
  choice = int(input("Please enter a valid choice(1/2/3/4):"))

if choice == 1:
    num1 = int(input("Please enter the side:"))
    print("Perimeter of the square with side",num1,"=",per_square(num1))
elif choice == 2:
    num1 = int(input("Please enter the length:"))
    num2 = int(input("Please enter the breadth:"))
    print("Perimeter of the rectangle with sides",num1,"and",num2,"=",per_rectangle(num1,num2))
elif choice == 3:
   num1 = int(input("Please enter the first side:"))
   num2 = int(input("Please enter the second side:"))
   num3 = int(input("Please enter the third side:"))
   print("Perimeter of the triangle with sides",num1,",",num2,"and",num3, "=",per_triangle(num1,num2,num3))
elif choice == 4:
    num1 = int(input("Please enter the radius of a circle:"))
    print("Circumference of the circle with sides",num1, "=",cir_circle(num1))  

    