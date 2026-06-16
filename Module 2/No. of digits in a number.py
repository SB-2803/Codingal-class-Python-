num = int(input("Enter a number to find the number of digits in it:"))
counter = 0
temp = num
while num>0:
    digit = num%10
    counter += 1
    num //= 10
print(counter,"is the number of all digits in the number",temp)