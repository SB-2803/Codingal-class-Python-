#Take input from user
a = input("Enter a word:")

#program to check break keyword
for i in a:
    if (i == "a" or i == "A"): #condition 1
        #display result
        print("A is found")
        break #break statement
    else:
        print("A not found")