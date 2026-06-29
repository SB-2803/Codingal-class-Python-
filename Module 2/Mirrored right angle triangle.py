# Define the number of rows for the triangle
rows = int(input("Enter the number of rows:"))

# Outer loop to handle the number of rows
for i in range(1, rows + 1):
    
    # First inner loop to print the leading spaces
    for j in range(rows - i):
        print(" ", end="")
        
    # Second inner loop to print the stars
    for k in range(i):
        print("*", end="")
        
    # Move to the next line after completing each row
    print()



