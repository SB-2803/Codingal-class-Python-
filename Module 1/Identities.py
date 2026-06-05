#Using the "is" identity operator.

# Example 1
x = 5
if type(x) is int:
    print("True.")
else:
    print("False")

# Example 2 
x = 5.0
if type(x) is not float:
    print("True.")
else:
    print("False.")

#Example 3
x = 20
y = 20
if x is y:
    print("x and y Same Identity.")

# Example 4
y = 30
if x is not y:
    print("x and y have Different Identity.")