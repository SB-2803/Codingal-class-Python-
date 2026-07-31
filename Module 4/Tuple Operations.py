#Create a tuple with different data types
tuple1 = ("tuple",3,4.2,False)
print(tuple1)

#Create a tuple
tuplex = (1,2,3,4,5,6,7)

#tuples are immutable so we cannot add new elements 
#using merge of tuples with the + operator we can add an element and create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#Counting the number of occurrences of an element in a tuple
tuplex = (50,10,90,80,50,80,50,60)
print(tuplex.count(50))

#create a tuple
tupl1 = (3,6,7,8,9,5,1,3,4,7,2,1,0)
#used tuple[start:stop] the start index is inclusive and stop index is exclusive
slice = tupl1[3:5]
print(slice)
#If start index is undenfined, it will start from beginning
slice = tupl1[:6]
print(slice)