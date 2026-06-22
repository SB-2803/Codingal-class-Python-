#take input from user
num = int(input("Enter the number:"))
t = num
numLen = 0

#iterate the loop
while t>0:
    numLen = numLen + 1
    t = int(t/10)

if numLen>=4: #condition 1
    numLen = int(numLen/2)
    chk = 0
    while num > 0: #iterate loop 1
        rem = num % 10
        if chk == numLen:
            midOne = rem
        elif chk == (numLen - 1):
            midTwo = rem
        num = int(num/10)
        chk = chk + 1

    prod = midOne*midTwo #product of middle digits
    #display the result
    print("\nThe product of the middle digits is(" + str(midOne)+ "*" +str(midTwo)+") = ",prod)
else:
    print("\nIt is not a 4 or more than 4-digit number!!")
    

    
 