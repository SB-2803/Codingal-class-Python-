print("Today we will calculate whether you can buy your desired item in your budget or not.To do so fill the following:")
name = input("Enter your Name:")
item = input("Enter the item that you want to buy:")
cost = int(input("Enter the cost of 1 item you want to buy:"))
Q = int(input("Enter the quantity of the item that you want to buy:"))
B = int(input("Enter your budget:"))

Total_Cost = (cost*Q)
print("\nYour total expenditure will be", Total_Cost)
Budget = (Total_Cost//B)
if(Total_Cost % B) == 0 and (Total_Cost % B)>0:
    print("\nThe item fits in your budget." )
else:
    print("\nThe item does not fit in your budget.")
    more = Total_Cost - B
    print("You need Rupee",more,"to buy what you want.")
