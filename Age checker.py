try:
    age = int(input("Enter your age:"))
    if age%2==0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Please enter an integer!!")