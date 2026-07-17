try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    result = num1/num2
    print("Result is:",result)
    print("Result is:",result2)

except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed!")
except ValueError:
    print("ValueError: Please enter numerical value!")
except NameError as ex:
    print("NameError: The exception is",ex)
except:
    print("Other error: Some error has occurred!")
finally:
    print("I will execute no matter what happens!!")