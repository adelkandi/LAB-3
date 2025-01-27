"""
Author: Adel Kandi
Date: 2025-01-26

This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
"""

print("Welcome to the Shopping Cart Program!")




price = []
name = []
quantity =[]

# Step 1: Ask the user for the number of items , quantity, price
while len(name) < 3:
    try :
        for i in range(3):
            item_name = input("What is the name of this item: ")
            name.append(item_name)
            item_price = int(input(f'What is the price of  the item {name[i]}: '))
            price.append(item_price)
            item_quantity = int(input(f"What is the quantity other item {name[i]}: "))
            quantity.append(item_quantity)

    except ValueError :
        print("Please give a digit number as 1 2 3 Try again")  # if the user enters wrong data it will show him this message

# Step 2: Calculate the total coast of the items
total_coast = 0 # initialize the coast to value = 0

# Print the items with their prices in order:
for i in range (len(price)):
    print(f"Item {name[i]}  coast : {price[i] * quantity[i]}")

for i in range(len(price)):
    total_coast = price[i]*quantity[i] + total_coast

print(f"The total coast: {total_coast}")  # Display the total coast of the items.


