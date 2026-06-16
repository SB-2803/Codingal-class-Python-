#Take input from the user
num = int(input("Enter a number:"))

#Initialize sum
sum = 0

#Find the sum of the cube of each digit
temp = num
while temp>0:
    digit = temp%10 # 1 % 10 = 1
    sum += digit**3 #sum = 27 + 125 = 152 + 1 = 153
    temp //= 10      #1//10 = 0

#display the result
if num == sum:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")
