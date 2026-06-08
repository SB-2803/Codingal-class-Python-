num = int(input("Enter a Number(Numerator):"))
numb = int(input("Enter a Number(Denominator):"))

if num % numb == 0:
    print("\n",num,"is divisible by",numb)
else:
    print("\n",num,"is not divisible by",numb)