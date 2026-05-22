print("We will be changing the case of the user's input. But before that Let's look at an example given below. ")

#Printing a string
print("\nExample 1-")
text = str("congratulations!")
print(text)

#Changing the case of String
print("congratulations!".upper())

print("\nExample 2-")
text2 = str("HELLO")
print(text2)
print(text2.lower())

print("\nNow let us change the case of the user's input!!")

#input a string
user = str(input("Enter a String: "))
print(user.swapcase())

print("\nThank you!!!")