"""
Author: Adel Kandi
Date: 2025-01-26

This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
"""

print("Welcome to the Shopping Cart Program!")






# Step 1: Ask the user for the number of items , quantity, price
# Creat a function named shopping_cart():
def shopping_cart():
    price = []
    name = []
    quantity = []
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
    total_cost = 0 # initialize the coast to value = 0

    # Print the items with their prices in order:
    for i in range (len(price)):
        print(f"Item {name[i]}  cost : {price[i] * quantity[i]}")

    for i in range(len(price)):
        total_cost = price[i]*quantity[i] + total_cost

    print(f"The total cost: {total_cost}")  # Display the total coast of the items.

    if total_cost > 100:
        discount = total_cost * 0.1
        total_cost -= discount
        print(f"\nYou saved ${discount:.2f} with a 10% discount!")
        print(f"Discounted Total: ${total_cost:.2f}")

####################################


shopping_cart() # Run the program for the first time

while True:

    # Main variables : name of the item, price and quantity
    #price = []
    #name = []
    #quantity =[]

    restart = input("\nWould you like to shop again? (yes/no): ").lower()
    if restart == "yes":
        shopping_cart()
    else:
        print("Thank you for shopping with us!")
        break


