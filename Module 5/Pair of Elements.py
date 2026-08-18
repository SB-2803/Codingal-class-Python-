#creating a class
class pair_elements:
    def two_sum(self,nums,target):
        #create an empty dictionary
        lookup = {}
        #iterate through the tuple
        for i,num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num],i)
            lookup[num] = i

#take input from user 
value = int(input("Enter the sum for which you want to make this search:"))
obj1 = pair_elements()
my_tuple = (10,70,90,80,40,20,30,50,60)
print("Number 1:%dand Number 2:%d"% obj1.two_sum(my_tuple,value))