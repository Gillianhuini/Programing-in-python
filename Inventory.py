#Write a Python program that simulates a simple inventory system(The program should allow users to add items to the inventory specify their quantities and update the quantities of the items are already present.Additionally users should be able to retrieve information about a specific item in the inventory by entering its nameFinally implement a feature that calculates and displays the lotalquantity of all items in the inventory)
# Create an empty dictionary to store inventory items
inventory = {}

while True:
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        
        if name in inventory:
            inventory[name] += quantity  # Update existing item
        else:
            inventory[name] = quantity  # Add new item
        
        print(f"{name} now has {inventory[name]} in stock.")

    elif choice == "2":
        name = input("Enter item name: ")
        
        if name in inventory:
            print(f"{name}: {inventory[name]} in stock.")
        else:
            print(f"{name} is not in inventory.")

    elif choice == "3":
        total = sum(inventory.values())
        print(f"Total quantity of all items: {total}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
