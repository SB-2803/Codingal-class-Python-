a = int(input("Enter a value:"))
b = int(input("Enter a value2:"))
c = int(input("Enter a value3:"))

avg = (a + b + c) / 3
print("Average =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higer than %d, %d, %d"%(avg, a, b , c))
elif avg > a and avg > b:
    print("%d is higher than only %d and %d"% (avg, a ,b))
elif avg > b and avg > c:
    print("%d is just higher than %d and %d"% (avg, b, c))
elif avg > c and avg > a:
    print("%d is only higher than %d and %d"% (avg, c, a))
elif avg > a:
    print("%d is only higher than %d"% (avg, a))
elif avg > b:
    print("%d is only higher than %d"% (avg, b))
elif avg > c:
    print("%d is only higher than %d"% (avg, c))
else:
    print("Invalid input!!")   
