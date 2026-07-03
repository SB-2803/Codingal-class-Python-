import random
number = random.randint(1,50)
print(number)
i = 1


while i<=5 or number == user:
    
    user = int(input("Enter a number to guess the random number chosen by the computer:"))
    if (1<=number<=15):
        print("ice cold")
    elif (16<=number<=25):
        print("Cold")
    elif(26<=number<=35):
        print("Warm")
    else:
        print("Hot")
    i = i+1
for j in range(1,i+1):
    print("*")
