#Take input from the user
rows = int(input("Please enter the total number of rows:"))
number = 1 #initialize by 1

print("Floyd's Triangle:")
#outer loop for number of rows
for i in range(rows):
    #inner loop for number of columns
    for j in range(i+1):
        #display result
        print(number, end= " ")
        number+=1
    print()