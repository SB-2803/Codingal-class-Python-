print("Today we will check whether the character you enter is an alphabet or not. To do so please enter the following:")
name = input("Enter your name:")
ctr = input("Enter any character:")
ascii_val = ord(ctr)
if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
    print("The character you entered is an alphabet.")
else:
    print("The character you entered is not an alphabet.")
