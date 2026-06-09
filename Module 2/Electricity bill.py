#Take input of number of units consumed from the user
units = int(input("Please enter the number of units you consumed this month:"))

#check conditions of units consumed
#Then calculate amout and surcharge accordingly
#surcharge is the tax value
#check for units less than 50

if(units < 50):
    amt = units * 2.60
    tax = 25
elif(units<=100):
    amt = 130 + ((units - 50)*3.25)
    tax = 45
elif(units <= 200):
    amt = 130 + 162.50 + ((units - 100)*5.26)
    tax = 35
else:
    amt = 130 + 162.50 + 526 + ((units - 200)*8.45)
    tax = 75

total = amt + tax
print("\nAmount =",amt)
print("Tax on that amount =",tax)
print("\nElectricity Bill = %.2f"%total)
 