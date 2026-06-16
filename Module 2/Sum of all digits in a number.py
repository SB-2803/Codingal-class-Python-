num = int(input("Enter a number to find the sum of all its digits:"))
sum = 0
temp = num
while num>0:
    digit = num%10
    sum += digit
    num //= 10
print(sum,"is the sum of all digits in the number",temp)