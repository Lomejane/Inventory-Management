# Store Inventory Management
store_inventory = {"soap", "shampoo", "conditioner", "facial wash"}

choose_action = input("Choose action (remove, add, or check availabilty): ").lower()

if choose_action == "remove":
    to_remove = input("Enter kitchen item to remove: ").lower()

    # to remove item in the store inventory
    if to_remove in store_inventory:
        store_inventory.remove(to_remove)
        print(f"You have removed {to_remove}!")
    print("Your store inventory:", store_inventory)

elif choose_action == "add":
    to_add = input("Enter item to add: ").lower()
    
    # to add item in the store inventory
    if to_add not in store_inventory:
        store_inventory.add(to_add)
        print(f"You have added {to_add} in the store inventory!")
    print("Your store inventory:", store_inventory)

elif choose_action == "check availability":
    to_check = input("Enter item to check availability: ")
    
    # to check item availability
    if to_check in store_inventory:
        print(f"You have {to_check} in the store!")

    print("Your store inventory:", store_inventory)

else:
    print("Invalid keywords! (remove, add, or check availability)")