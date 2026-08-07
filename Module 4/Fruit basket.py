#Create 2 fruit baskets as sets
b1 = {'apple','grapes','mangoes','banana','kiwi'}
b2 = {'strawberry','mangoes','watermelon','grapes'}
print("Basket 1:",b1)
print("Basket 2:",b2)

#Add a new fruit to b1
b1.add("orange")
print("Basket 1 after adding orange:",b1)

#Finding common fruits in both baskets
common = b1.intersection(b2)
print("Fruits in both baskets:",common)

#Create an array of fruit counts using array module
import array as a
fruit_count = a.array('i',[1,3,5,2])
print("Fruit counts array:",fruit_count)

#Add new fruit to the array
fruit_count.insert(0,1)
fruit_count.append(6)
print("Fruit counts after adding items:",fruit_count)
#Counting how many times the no. 1 appears in the array
no = fruit_count.count(1)
print("Number of times 1 apperas:",no)

#Reversing the array
fruit_count.reverse()
print("Reversed fruit counts array:",fruit_count)
