#Initialze Dictionary
dic = {'Codingal':2,'is':3,'best':4,'for':2,'coding':1}

num = int(input("Enter any number from 1 to 4: "))

#using loop
#selective key values in dictionary
res = 0
for key in dic:
    if dic[key] == num:
        res += 1

#Printing result
print("The number of times",num,"came is:",res)