age = int(input("Enter your age:"))
if(3<=age<10):
    print("You are in primary school.")
elif(10<=age<=20):
    print("You are in middle or senior school.")
elif(20<age<=24):
    print("You are in my college.")
elif(22<age<=59):
    print("You are working to earn.")
elif(59<age<=110):
    print("You are a senior citizen.")
else:
    print("Invalid input!!")