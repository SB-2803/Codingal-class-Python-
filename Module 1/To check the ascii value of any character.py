print("Today will check the ascii value of the character you enter.")
name = input ("Enter your name:")
ctr = input("Enter any 1 character of your choice to check its ascii value:")
ascii = ord(ctr)
print("The ascii value of the character you entered is",ascii)
if (65 <= ascii <= 90) or (97 <= ascii <= 122):
    print("It is an alphabet.")
elif (48 <= ascii <= 57):
    print("It is a number.")
else:
    print("It is a special character.")
print("Thank you for your cooperation!!")
 