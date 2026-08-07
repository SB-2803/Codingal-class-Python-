#Different types of sets in python
#Set of integers
s = {1,2,3}
print(s)

#Set of mixed datatypes
s = {1.3,"Hello",(1,2,3)}
print(s)

#Set can't have duplicates
set1 = {1,2,6,3,2,8,1,9,7,2}
print(set1)

#We can make set from a list
s = set([1,2,3,4])
print(s)

#remove a number from a set
nset = set([0,1,2,3,4,5])
print("Original set:",nset)
nset.pop()
print("After removing the first element from the set:",nset)