#Create class
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #Method to print points in coordinate format
    def __str__(self):
        return("({0},{1})".format(self.x,self.y))

#Create object
x1 = int(input("Enter the coordinate for x:"))
y1 = int(input("Enter the coordinate for y:"))
p1 = Point(x1,y1)
print(p1)