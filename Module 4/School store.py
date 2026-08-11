#Create the stre's item names and stock counts
items = ['Pencils','Eraser','Notebook','Sharpener','Glue']
stock_counts = [12,0,5,8,3]

#Pair items with stock counts in a dictionary
inventory = {item: count for item,count in zip(items,stock_counts)}
print("Full inventory:",inventory)

#Filter only the items that are still in stock
in_stock_items = [item for item in items if inventory[item]>0]
print("In stock items:",in_stock_items)

#Ask the buyer what they want
chosen_item = input("Enter the item that you want to buy? ")

#Stop the buyer early if the item in not in stock or not available
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item,"not in stock:(")
    exit()

#Create prices and ask for markup amount
prices = [10,5,40,15,20]
markup = int(input("Enter the markup amount:"))

#Apply markup amount to every item in the list
marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked up prices:",marked_up_prices)

#Find the marked up price of the chosen item
item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("Price of",chosen_item,"is:",chosen_price)

#Reduce the stock after the purchase
inventory[chosen_item]-=1
print(chosen_item,"purchased!! Remanining stock:",inventory[chosen_item])