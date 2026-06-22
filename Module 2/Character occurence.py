#take input of a word
string = input("Please enter a word:")
#take input of a character
char = input("Please enter your own character:")

i = 0
count = 0
#loop will to find the occurence of character
while(i < len(string)): #gives us total number of characters in the string.
    if(string[i] == char):
        count = count + 1
    i = i + 1

#Display the output
print("The total number of times", char, "ocuured in the word", string, "is", count)

     