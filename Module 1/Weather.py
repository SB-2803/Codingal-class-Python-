print("Today we will find what clothes is best suitable for you to wear according to your surrounding weather. To do so fill the following:")
name=input("Enter your name:")
sex=input("Enter your gender:")
home=input("Enter the place where you live:")
climate=input("Enter the climate of the place where you live:")
month=input("Enter the month right now:")
weather=int(input("Enter whether it is hot or cold, in case of hot enter 1 and in case of cold enter 2: "))
if (weather == 1):
    print("You can wear shorts with a t-shirt. You are advised to wear cotton and light-coloured clothes.")
    print("If you are a female you can even wear a frock.")
else:
    print("You can wear full pants with a t-shirt and a sweater. A jacket would also be suitable.")
    print("In case of extreme cold you are advised to wear warm and woolen clothes with gloves and socks which are dark-coloured.")
print("Thank you for your cooperation. We hope our advise was helpful.")