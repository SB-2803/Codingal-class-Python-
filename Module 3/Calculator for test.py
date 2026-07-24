def add(a,b):
    return a +b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    a/b
print("Choose one of the operations from below to perform it:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter your choice:")
try:
    n = float(input("Enter the first number:"))
    num = float(input("Enter the second number:"))
    if choice == "Add" or choice == "1":
       print(n,"+",num,"=",add(n,num))
    elif choice == "Subtract" or choice == "2":
       print(n,"-",num,"=",subtract(n,num))
    elif choice == "Multiply" or choice == "3":
       print(n,"*",num,"=",multiply(n,num))
    elif choice == "Divide" or choice == "4":
       print(n,"/",num,"=",divide(n,num))
except ValueError:
    print("Enter a valid interger!!")
except ZeroDivisionError:
    print("Cannot divide by Zero!!")