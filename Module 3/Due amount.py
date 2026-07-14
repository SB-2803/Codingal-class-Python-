def due_amt(bill_amt,amt_paid):
    return bill_amt - amt_paid

def tip_paid(bill_amt,amt_paid):
    return amt_paid - bill_amt

bill_amt = int(input("Enter your bill amount:"))
amt_paid = int(input("Enter the amount you paid to the cashier:"))

if bill_amt == amt_paid:
    print("No due payment")
elif bill_amt<amt_paid:
    print("You are very generous!! You gave",tip_paid(bill_amt,amt_paid),"as a tip.")
else:
    print("You have to pay",due_amt(bill_amt,amt_paid),"to the cashier!!")