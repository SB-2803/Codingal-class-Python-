CP = int(input("Enter the Cost price:"))
SP = int(input("Enter the Selling price:"))

if(SP > CP):
    pt = SP - CP
    print("Profit of Rupee", pt, "was incurred.")
else:
    loss = CP - SP
    print("Loss of Rupee", loss, "was incurred.")