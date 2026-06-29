input = input("Enter any character to convert it into its binary pattern:")
for char in input:
    print(bin(ord(char))[2:], end=" ")