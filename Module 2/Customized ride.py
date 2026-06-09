print("Select your ride:")
print("1.Bike")
print("2.Car")
#take input of 1 or 2
#select your ride
choice = int(input("Enter your choice:"))
#User entering option 1
if (choice == 1):
    print("What type of bike do you want:")
    print("1.Scooty\n")
    print("2.Scooter\n")
    choice2=int(input("Enter your choice in bike:"))
    if choice2 == 1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")
elif (choice == 2):
    print("What type of car do you want:")
    print("1.Sedan\n")
    print("2.XUV\n")
    choice2=int(input("Enter your choice in car:"))
    if choice2 == 1:
        print("You have selected Sedan")
    else:
        print("You have selected XUV") 
else:
    print("Invalid input!!")  
